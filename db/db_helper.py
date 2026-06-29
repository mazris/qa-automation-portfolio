import pymysql

class DBHelper:

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root1234",
            database="pos_test_db",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def get_customer_by_id(self, customer_id):
        self.cursor.execute(
            "SELECT * FROM customers WHERE id = %s",
            (customer_id,)
        )

        return self.cursor.fetchone()

    def get_customer_by_email(self,email):
        self.cursor.execute("SELECT * FROM customers WHERE email = %s",
                            (email,))
        return self.cursor.fetchone()

    def update_loyalty_points(self,customer_id,points):
        self.cursor.execute("UPDATE customers SET loyalty_points = %s WHERE id = %s",
                            (points,customer_id))
        self.connection.commit()

    def reset_loyalty_points(self,customer_id):
        self.cursor.execute("UPDATE customers SET loyalty_points = 500 WHERE id = %s",
                            (customer_id,))
        self.connection.commit()

    def get_product_by_barcode(self, barcode):
        self.cursor.execute(
            "SELECT * FROM products WHERE barcode = %s",
            (barcode,)
        )
        return self.cursor.fetchone()

    def update_product_stock(self, barcode, quantity):
        self.cursor.execute(
            "UPDATE products SET quantity = %s, in_stock = %s WHERE barcode = %s",
            (quantity, quantity > 0, barcode)
        )
        self.connection.commit()

    def reset_product_stock(self, barcode, quantity=50):
        self.update_product_stock(barcode, quantity)

 # ── Promo code methods ────────────────────────────

    def get_promo_code(self, code):
        self.cursor.execute(
            "SELECT * FROM promo_codes WHERE code = %s",
            (code,)
        )
        return self.cursor.fetchone()

    def deactivate_promo_code(self, code):
        self.cursor.execute(
            "UPDATE promo_codes SET is_active = FALSE WHERE code = %s",
            (code,)
        )
        self.connection.commit()

    def activate_promo_code(self, code):
        self.cursor.execute(
            "UPDATE promo_codes SET is_active = TRUE WHERE code = %s",
            (code,)
        )
        self.connection.commit()

    def insert_promo_code(self, code, discount, expiry_date):
        self.cursor.execute(
            "INSERT INTO promo_codes (code, discount_percent, is_active, expiry_date) VALUES (%s, %s, TRUE, %s)",
            (code, discount, expiry_date)
        )
        self.connection.commit()

    def delete_promo_code(self, code):
        self.cursor.execute(
            "DELETE FROM promo_codes WHERE code = %s",
            (code,)
        )
        self.connection.commit()

        # ── Transaction methods ───────────────────────────

    def get_transaction_by_id(self, transaction_id):
        self.cursor.execute(
            "SELECT * FROM transactions WHERE id = %s",
            (transaction_id,)
        )
        return self.cursor.fetchone()

    def insert_transaction(self, customer_id, total, discount, promo_code):
        self.cursor.execute(
            "INSERT INTO transactions (customer_id, total, discount_applied, promo_code) VALUES (%s, %s, %s, %s)",
            (customer_id, total, discount, promo_code)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def delete_transaction(self, transaction_id):
        self.cursor.execute(
            "DELETE FROM transactions WHERE id = %s",
            (transaction_id,)
        )
        self.connection.commit()

        # ── Cleanup ───────────────────────────────────────

        def reset_all_test_data(self):
            self.reset_loyalty_points(1)
            self.reset_product_stock("00123")
            self.activate_promo_code("SAVE5")
            self.cursor.execute("DELETE FROM transactions")
            self.connection.commit()

