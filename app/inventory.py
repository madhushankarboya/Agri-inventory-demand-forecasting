from flask import Blueprint, render_template, request, send_file, current_app
from flask_login import login_required
from app.utils import role_required, calculate_inventory

import pandas as pd
import numpy as np
import os
import uuid
from datetime import datetime

# PDF Imports
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, Image
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode import qr

import matplotlib.pyplot as plt

inventory = Blueprint("inventory", __name__)


# =====================================================
# INVENTORY PAGE
# =====================================================
@inventory.route("/inventory", methods=["GET", "POST"])
@login_required
def show_inventory():

    df = pd.read_csv("data/crop_production.csv")

    states = sorted(df["State_Name"].unique())
    crops = sorted(df["Crop"].unique())

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
# DOWNLOAD PDF REPORT
# =====================================================
@inventory.route("/download_report", methods=["POST"])
@role_required(["Admin", "Officer"])
def download_report():

    state = request.form.get("state")
    crop = request.form.get("crop")
    safety = request.form.get("safety")
    reorder = request.form.get("reorder")
    eoq = request.form.get("eoq")
    risk_level = request.form.get("risk_level")

    df = pd.read_csv("data/crop_production.csv")

    filtered = df[
        (df["State_Name"] == state) &
        (df["Crop"] == crop)
    ]

    production_data = filtered["Production"].values

    # ---------------- Create Chart ----------------
    reports_folder = os.path.join(current_app.root_path, "reports")
    os.makedirs(reports_folder, exist_ok=True)

    chart_path = os.path.join(reports_folder, "temp_chart.png")

    if len(production_data) > 0:
        plt.figure()
        plt.plot(production_data)
        plt.title("Production Trend")
        plt.xlabel("Year Index")
        plt.ylabel("Production")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

    # ---------------- Create PDF ----------------
    filename = f"inventory_report_{uuid.uuid4().hex[:6]}.pdf"
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

    # Table
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
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER')
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))

    # Chart
    if os.path.exists(chart_path):
        elements.append(Paragraph("<b>Production Trend Chart</b>", styles["Normal"]))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Image(chart_path, width=5*inch, height=3*inch))
        elements.append(Spacer(1, 0.5 * inch))

    # QR
    verification_url = "https://gov-agri-portal.nic.in"
    qr_code = qr.QrCodeWidget(verification_url)
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    d = Drawing(100, 100, transform=[100.0/width, 0, 0, 100.0/height, 0, 0])
    d.add(qr_code)

    elements.append(Paragraph("<b>Scan for Verification</b>", styles["Normal"]))
    elements.append(d)

    doc.build(elements)

    return send_file(file_path, as_attachment=True)