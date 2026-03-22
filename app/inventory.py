from flask import Blueprint, render_template, request, send_file, current_app, abort # type: ignore
from flask_login import login_required # type: ignore
from app.utils import role_required, calculate_inventory

import pandas as pd # type: ignore
import numpy as np # type: ignore
import os
import uuid
import matplotlib.pyplot as plt # type: ignore

from reportlab.platypus import ( # type: ignore
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, Image
)
from reportlab.lib import colors # type: ignore
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # type: ignore
from reportlab.lib.units import inch # type: ignore
from reportlab.lib.pagesizes import A4 # type: ignore
from reportlab.graphics.shapes import Drawing # type: ignore
from reportlab.graphics.barcode import qr # type: ignore

inventory = Blueprint("inventory", __name__)


# ================= SAFE DATA LOAD =================
def load_data():
    try:
        file_path = os.path.join(current_app.root_path, "..", "data", "crop_production.csv")
        file_path = os.path.abspath(file_path)
        return pd.read_csv(file_path)
    except Exception as e:
        print("Data Load Error:", e)
        return pd.DataFrame()


# =====================================================
# INVENTORY PAGE
# =====================================================
@inventory.route("/inventory", methods=["GET", "POST"])
@login_required
def show_inventory():

    df = load_data()

    if df.empty:
        return "Dataset not available."

    states = sorted(df["State_Name"].dropna().unique())
    crops = sorted(df["Crop"].dropna().unique())

    safety = reorder = eoq = None
    risk_level = None

    if request.method == "POST":

        state = request.form.get("state")
        crop = request.form.get("crop")

        filtered = df[
            (df["State_Name"] == state) &
            (df["Crop"] == crop)
        ]

        demand_list = filtered["Production"].values

        if len(demand_list) > 0:

            safety, reorder, eoq = calculate_inventory(demand_list)

            avg_production = float(np.mean(demand_list))

            if avg_production > 50000:
                risk_level = "LOW"
            elif avg_production > 20000:
                risk_level = "MEDIUM"
            else:
                risk_level = "HIGH"
        else:
            safety = reorder = eoq = 0
            risk_level = None

    return render_template(
        "inventory.html",
        states=states,
        crops=crops,
        safety=safety,
        reorder=reorder,
        eoq=eoq,
        risk_level=risk_level
    )


# =====================================================
# DOWNLOAD PDF REPORT (SECURE)
# =====================================================
@inventory.route("/download_report", methods=["POST"])
@login_required
@role_required(["Admin", "Officer"])
def download_report():

    try:
        state = request.form.get("state")
        crop = request.form.get("crop")
        safety = request.form.get("safety")
        reorder = request.form.get("reorder")
        eoq = request.form.get("eoq")
        risk_level = request.form.get("risk_level")
    except:
        abort(400)

    df = load_data()

    if df.empty:
        abort(500)

    filtered = df[
        (df["State_Name"] == state) &
        (df["Crop"] == crop)
    ]

    production_data = filtered["Production"].values

    # ---------------- SAFE FILE PATH ----------------
    reports_folder = os.path.join(current_app.root_path, "reports")
    os.makedirs(reports_folder, exist_ok=True)

    unique_id = uuid.uuid4().hex[:6]

    chart_path = os.path.join(reports_folder, f"chart_{unique_id}.png")

    # ---------------- CREATE CHART ----------------
    if len(production_data) > 0:
        plt.figure()
        plt.plot(production_data)
        plt.title("Production Trend")
        plt.xlabel("Year Index")
        plt.ylabel("Production")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

    # ---------------- CREATE PDF ----------------
    filename = f"inventory_report_{unique_id}.pdf"
    file_path = os.path.join(reports_folder, filename)

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Heading1"],
        alignment=1,
        textColor=colors.darkblue
    )

    elements.append(Paragraph(
        "Government of India<br/>"
        "Ministry of Agriculture & Farmers Welfare<br/>"
        "Official Inventory Optimization Report",
        title_style
    ))

    elements.append(Spacer(1, 0.5 * inch))

    data = [
        ["State Name", state],
        ["Crop Name", crop],
        ["Safety Stock", safety],
        ["Reorder Point", reorder],
        ["EOQ", eoq],
        ["Risk Level", risk_level]
    ]

    table = Table(data, colWidths=[2.5 * inch, 3 * inch])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))

    if os.path.exists(chart_path):
        elements.append(Image(chart_path, width=5*inch, height=3*inch))

    # QR Code
    qr_code = qr.QrCodeWidget("https://gov-agri-portal.nic.in")
    bounds = qr_code.getBounds()
    d = Drawing(100, 100)
    d.add(qr_code)
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(d)

    doc.build(elements)

    return send_file(file_path, as_attachment=True)
