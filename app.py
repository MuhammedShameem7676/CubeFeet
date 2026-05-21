# app.py
from flask import Flask, request, render_template, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

# ----------------------------------------
# determine_output (same mappings)
# ----------------------------------------
def determine_output(a, b):
    try:
        a = int(a)
        b = int(b)
    except (TypeError, ValueError):
        return 0

    if a == 3:
        return {
            10: 0.1, 11: 0.2, 12: 0.2, 13: 0.2, 14: 0.3, 15: 0.3, 16: 0.4, 17: 0.4, 18: 0.5, 19: 0.5,
            20: 0.6, 21: 0.6, 22: 0.7, 23: 0.7, 24: 0.8, 25: 0.9, 26: 1.0, 27: 1.0, 28: 1.1, 29: 1.2,
            30: 1.3, 31: 1.4, 32: 1.4, 33: 1.5, 34: 1.6, 35: 1.7, 36: 1.8, 37: 1.9, 38: 2.0, 39: 2.1,
            40: 2.3, 41: 2.4, 42: 2.7, 43: 2.6, 44: 2.7, 45: 2.9, 46: 3.0, 47: 3.1, 48: 3.3, 49: 3.4,
            50: 3.5, 51: 3.7, 52: 3.8, 53: 4.0, 54: 4.1, 55: 4.2, 56: 4.4, 57: 4.6, 58: 4.7, 59: 4.9,
            60: 5.1, 61: 5.2, 62: 5.4, 63: 5.6, 64: 5.8, 65: 6.0, 66: 6.1, 67: 6.3, 68: 6.5, 69: 6.7,
            70: 6.9, 71: 7.1, 72: 7.3, 73: 7.5, 74: 7.7, 75: 7.9, 76: 8.1, 77: 8.4, 78: 8.6, 79: 8.8,
            80: 9.0, 81: 9.3, 82: 9.5, 83: 9.7, 84: 10.0, 85: 10.2, 86: 10.4, 87: 10.7, 88: 10.9, 89: 11.2, 90: 11.4
        }.get(b, 0)

    elif a == 4:
        return {
            10: 0.2, 11: 0.2, 12: 0.3, 13: 0.3, 14: 0.4, 15: 0.4, 16: 0.5, 17: 0.5, 18: 0.6, 19: 0.7,
            20: 0.7, 21: 0.8, 22: 0.9, 23: 1.0, 24: 1.1, 25: 1.2, 26: 1.2, 27: 1.3, 28: 1.4, 29: 1.6,
            30: 1.7, 31: 1.8, 32: 1.9, 33: 2.0, 34: 2.1, 35: 2.3, 36: 2.4, 37: 2.5, 38: 2.7, 39: 2.8,
            40: 3.0, 41: 3.1, 42: 3.3, 43: 3.4, 44: 3.6, 45: 3.7, 46: 3.9, 47: 4.1, 48: 4.3, 49: 4.4,
            50: 4.6, 51: 4.8, 52: 5.0, 53: 5.2, 54: 5.4, 55: 5.6, 56: 5.8, 57: 6.0, 58: 6.2, 59: 6.4,
            60: 6.6, 61: 6.9, 62: 7.1, 63: 7.3, 64: 7.6, 65: 7.8, 66: 8.0, 67: 8.3, 68: 8.5, 69: 8.8,
            70: 9.0, 71: 9.3, 72: 9.6, 73: 9.8, 74: 10.1, 75: 10.4, 76: 10.7, 77: 10.9, 78: 11.2, 79: 11.5,
            80: 11.8, 81: 12.1, 82: 12.4, 83: 12.7, 84: 13.0, 85: 13.3, 86: 13.6, 87: 14.0, 88: 14.3, 89: 14.6, 90: 14.9
        }.get(b, 0)

    elif a == 6:
        return {
            10: 0.3, 11: 0.3, 12: 0.4, 13: 0.4, 14: 0.6, 15: 0.6, 16: 0.7, 17: 0.8, 18: 0.9, 19: 1.0,
            20: 1.1, 21: 1.2, 22: 1.4, 23: 1.5, 24: 1.6, 25: 1.8, 26: 1.9, 27: 2.1, 28: 2.2, 29: 2.4,
            30: 2.5, 31: 2.7, 32: 2.9, 33: 3.1, 34: 3.3, 35: 3.5, 36: 3.7, 37: 3.9, 38: 4.1, 39: 4.3,
            40: 4.5, 41: 4.7, 42: 5.0, 43: 5.2, 44: 5.5, 45: 5.7, 46: 6.0, 47: 6.2, 48: 6.5, 49: 6.8,
            50: 7.1, 51: 7.3, 52: 7.6, 53: 7.9, 54: 8.2, 55: 8.5, 56: 8.8, 57: 9.2, 58: 9.5, 59: 9.8,
            60: 10.2, 61: 10.5, 62: 10.8, 63: 11.2, 64: 11.6, 65: 11.9, 66: 12.3, 67: 12.7, 68: 13.0,
            69: 13.4, 70: 13.8, 71: 14.2, 72: 14.6, 73: 15.0, 74: 15.4, 75: 15.9, 76: 16.3, 77: 16.7,
            78: 17.2, 79: 17.6, 80: 18.1, 81: 18.5, 82: 19.0, 83: 19.4, 84: 19.9, 85: 20.4, 86: 20.9,
            87: 21.4, 88: 21.8, 89: 22.3, 90: 22.9
        }.get(b, 0)

    elif a == 7:
        return {
            10: 0.3, 11: 0.4, 12: 0.5, 13: 0.5, 14: 0.6, 15: 0.7, 16: 0.8, 17: 0.9, 18: 1.1, 19: 1.2,
            20: 1.3, 21: 1.4, 22: 1.6, 23: 1.7, 24: 1.9, 25: 2.0, 26: 2.2, 27: 2.4, 28: 2.6, 29: 2.7,
            30: 2.9, 31: 3.1, 32: 3.3, 33: 3.5, 34: 3.8, 35: 4.0, 36: 4.2, 37: 4.5, 38: 4.7, 39: 5.0,
            40: 5.2, 41: 5.5, 42: 5.7, 43: 6.0, 44: 6.3, 45: 6.6, 46: 6.9, 47: 7.2, 48: 7.5, 49: 7.8,
            50: 8.1, 51: 8.5, 52: 8.8, 53: 9.1, 54: 9.5, 55: 9.8, 56: 10.2, 57: 10.6, 58: 11.0, 59: 11.3,
            60: 11.7, 61: 12.1, 62: 12.5, 63: 12.9, 64: 13.3, 65: 13.8, 66: 14.2, 67: 14.6, 68: 15.1,
            69: 15.5, 70: 16.0, 71: 16.4, 72: 16.9, 73: 17.3, 74: 17.8, 75: 18.3, 76: 18.8, 77: 19.3,
            78: 19.8, 79: 20.3, 80: 20.8, 81: 21.4, 82: 21.9, 83: 22.4, 84: 23.0, 85: 23.5, 86: 24.1,
            87: 24.6, 88: 25.2, 89: 25.8, 90: 26.4
        }.get(b, 0)

    elif a == 8:
        return {
            10: 0.4, 11: 0.4, 12: 0.5, 13: 0.5, 14: 0.7, 15: 0.8, 16: 0.9, 17: 1.1, 18: 1.2, 19: 1.3,
            20: 1.5, 21: 1.6, 22: 1.8, 23: 2.0, 24: 2.1, 25: 2.3, 26: 2.5, 27: 2.7, 28: 2.9, 29: 3.1,
            30: 3.3, 31: 3.5, 32: 3.8, 33: 4.0, 34: 4.3, 35: 4.5, 36: 4.8, 37: 5.1, 38: 5.3, 39: 5.6,
            40: 5.9, 41: 6.2, 42: 6.5, 43: 6.8, 44: 7.1, 45: 7.5, 46: 7.8, 47: 8.1, 48: 8.5, 49: 8.9,
            50: 9.2, 51: 9.6, 52: 10.0, 53: 10.4, 54: 10.8, 55: 11.2, 56: 11.6, 57: 12.0, 58: 12.4,
            59: 12.8, 60: 13.3, 61: 13.7, 62: 14.2, 63: 14.6, 64: 15.2, 65: 15.6, 66: 16.1, 67: 16.6,
            68: 17.1, 69: 17.6, 70: 18.1, 71: 18.6, 72: 19.1, 73: 19.7, 74: 20.2, 75: 20.8, 76: 21.3,
            77: 21.9, 78: 22.4, 79: 23.0, 80: 23.6, 81: 24.2, 82: 24.8, 83: 25.4, 84: 26.0, 85: 26.7,
            86: 27.3, 87: 27.9, 88: 28.6, 89: 29.2, 90: 29.9
        }.get(b, 0)

    elif a == 9:
        return {
            10: 0.4, 11: 0.4, 12: 0.5, 13: 0.5, 14: 0.8, 15: 0.9, 16: 1.0, 17: 1.1, 18: 1.3, 19: 1.4,
            20: 1.6, 21: 1.7, 22: 1.9, 23: 2.0
        }.get(b, 0)

    return 0



# -------------------------------------------------
# ROUTES
# -------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ================= TIMBER =================
@app.route("/timber")
def timber():
    return render_template("timber.html")


@app.route("/timberresult", methods=["POST"])
def timber_result():
    data = request.get_json(silent=True) or {}
    results = []

    for table in data.get("tables", []):
        rows_out = []
        total_cube = 0.0

        # ---------------------------------
        # 1. Build slabs (INCH CATEGORIES)
        # ---------------------------------
        prices = table.get("prices", [])
        if not prices:
            continue

        slabs = []
        for i, p in enumerate(prices):
            start = 0 if i == 0 else int(prices[i - 1]["feet"]) + 1
            end = int(p["feet"])  # inches limit

            slabs.append({
                "start": start,
                "end": end,
                "amount1": float(p["amount1"]),
                "amount2": float(p["amount2"])
            })

        # Last slab → infinity
        slabs.append({
            "start": slabs[-1]["end"] + 1,
            "end": float("inf"),
            "amount1": slabs[-1]["amount1"],
            "amount2": slabs[-1]["amount2"]
        })

        # ---------------------------------
        # 2. CATEGORY AGGREGATION
        # ---------------------------------
        category_cube = {}  # key = slab index, value = cube sum

        for r in table.get("rows", []):
            feet = int(r["feet"])
            inch = int(r["inch"])

            cube = determine_output(feet, inch)
            total_cube += cube

            rows_out.append({
                "feet": feet,
                "inch": inch,
                "cube": round(cube, 2)
            })

            # find category by inch
            for idx, slab in enumerate(slabs):
                if slab["start"] <= inch <= slab["end"]:
                    category_cube.setdefault(idx, 0.0)
                    category_cube[idx] += cube
                    break

        if not rows_out:
            continue

        total_cube = round(total_cube, 2)

        # ---------------------------------
        # 3. CALCULATE TOTAL AMOUNTS
        # ---------------------------------
        total_amount_1 = 0.0
        total_amount_2 = 0.0

        for idx, cube_sum in category_cube.items():
            slab = slabs[idx]
            total_amount_1 += cube_sum * slab["amount1"]
            total_amount_2 += cube_sum * slab["amount2"]

        total_amount_1 = round(total_amount_1, 2)
        total_amount_2 = round(total_amount_2, 2)

        now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        # ---------------------------------
        # 4. PUSH TWO RESULT TABLES
        # ---------------------------------
        results.append({
            "table_name": table.get("name", "Untitled Table"),
            "rows": rows_out,
            "total_cube": total_cube,
            "total_amount": total_amount_1,
            "datetime": now
        })

        results.append({
            "table_name": table.get("name", "Untitled Table"),
            "rows": rows_out,
            "total_cube": total_cube,
            "total_amount": total_amount_2,
            "datetime": now
        })

    if not results:
        return render_template(
            "timberresult.html",
            results=[],
            error="No valid data found. Please enter measurements and prices."
        )

    return render_template("timberresult.html", results=results)



# ================= CORE =================
@app.route("/core")
def core():
    return render_template("core.html")

@app.route("/coreresult", methods=["POST"])
def core_result():
    data = request.get_json(silent=True) or {}
    print("CORE DATA:", data)

    results = []

    for table in data.get("tables", []):
        rows_out = []
        total_cube = 0.0

        for r in table.get("rows", []):
            feet = int(r["feet"])
            inch = int(r["inch"])

            cube = determine_output(feet, inch)
            total_cube += cube

            rows_out.append({
                "feet": feet,
                "inch": inch,
                "cube": round(cube, 2)
            })

        if not rows_out:
            continue

        total_cube = round(total_cube, 2)

        prices = table.get("prices", [])

        if not prices:
            continue

        rate_1 = float(prices[0].get("amount1", 0))
        rate_2 = float(prices[0].get("amount2", 0))

        now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        results.append({
            "table_name": f"{table.get('name', 'Untitled Table')} ",
            "rows": rows_out,
            "total_cube": total_cube,
            "total_amount": round(total_cube * rate_1, 2),
            "datetime": now
        })

        results.append({
            "table_name": f"{table.get('name', 'Untitled Table')} ",
            "rows": rows_out,
            "total_cube": total_cube,
            "total_amount": round(total_cube * rate_2, 2),
            "datetime": now
        })

    # ✅ RETURN WHEN NO DATA
    if not results:
        return render_template(
            "coreresult.html",
            results=[],
            error="No valid data found. Please go back and enter measurements."
        )

    # ✅ RETURN WHEN DATA EXISTS (THIS WAS MISSING)
    return render_template(
        "coreresult.html",
        results=results
    )
 

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)