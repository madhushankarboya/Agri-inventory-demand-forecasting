import os
from datetime import datetime
import numpy as np # type: ignore
import math
from flask_login import current_user # type: ignore
from functools import wraps
from flask import abort # type: ignore

LOG_FILE = "instance/activity.log"

# ----------------------------------
# ROLE BASED ACCESS
# ----------------------------------
def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            if not current_user.is_authenticated:
                abort(403)

            if current_user.role not in allowed_roles:
                abort(403)

            return f(*args, **kwargs)

        return wrapper
    return decorator


# ----------------------------------
# ACTIVITY LOGGING
# ----------------------------------
def log_activity(username, action):

    os.makedirs("instance", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {username} | {action}\n")


# ----------------------------------
# INVENTORY CALCULATION (SAFE VERSION)
# ----------------------------------
def calculate_inventory(demand_list):

    demand_array = np.array(demand_list)

    # 🔥 If no data
    if demand_array.size == 0:
        return 0, 0, 0

    mean = float(np.mean(demand_array))
    std = float(np.std(demand_array))

    safety_stock = 1.65 * std
    reorder_point = mean + safety_stock
    eoq = math.sqrt((2 * mean * 500) / 10)

    return int(safety_stock), int(reorder_point), int(eoq)