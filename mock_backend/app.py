from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Sonia123",
        database="pos_test_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# ── Get customer ──────────────────────────────

@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    conn.close()

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer), 200

# ── Apply promo code ──────────────────────────

@app.route("/apply-promo", methods=["POST"])
def apply_promo():
    data = request.get_json()
    code = data.get("promo_code")
    cart_total = data.get("cart_total")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promo_codes WHERE code = %s", (code,))
    promo = cursor.fetchone()

    if promo is None:
        cursor.close()
        conn.close()
        return jsonify({"error": "Promo code not found"}), 404

    if not promo["is_active"]:
        cursor.close()
        conn.close()
        return jsonify({"error": "Promo code is not active"}), 400

    discount = cart_total * (promo["discount_percent"] / 100)
    final_total = cart_total - discount

    cursor.close()
    conn.close()

    return jsonify({
        "promo_code": code,
        "discount_percent": promo["discount_percent"],
        "discount_amount": round(discount, 2),
        "final_total": round(final_total, 2)
    }), 200

# ── Update loyalty points ─────────────────────

@app.route("/customers/<int:customer_id>/loyalty-points", methods=["PUT"])
def update_loyalty_points(customer_id):
    data = request.get_json()
    new_points = data.get("points")
    print(f"DEBUG: received points = {new_points}, type = {type(new_points)}")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE customers SET loyalty_points = %s WHERE id = %s",
        (new_points, customer_id)
    )
    conn.commit()
    print(f"DEBUG: rows affected = {cursor.rowcount}")

    cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
    updated_customer = cursor.fetchone()
    print(f"DEBUG: after update, customer = {updated_customer}")

    cursor.close()
    conn.close()

    return jsonify(updated_customer), 200


if __name__ == "__main__":
    app.run(debug=True, port=5050)


