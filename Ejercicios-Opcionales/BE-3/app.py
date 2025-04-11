from flask import Flask,request,jsonify
import sqlite3
import json

app = Flask(__name__)


DATABASE ="products.db"


def init_db():
    with sqlite3.connect(DATABASE) as conn:
          conn.execute(
                """
                CREATE TABLE IF NOT EXISTS products_table(
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
                )
                """
          )
init_db()


@app.route("/api/products", methods=["GET"])
def get_product_list():
        with sqlite3.connect(DATABASE) as conn:
          cursor = conn.execute("SELECT * FROM products_table")
          productos =[
               {"id": row[0], "nombre": row[1] , "precio": row[2]}
               for row in cursor.fetchall()
               ]
        return jsonify(productos)


@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json()

    with sqlite3.connect(DATABASE) as conn:
          cursor = conn.execute(
                "INSERT INTO products_table(nombre,precio) VALUES (?,?)",
                (data["nombre"],data["precio"])
          )
          conn.commit()

    return jsonify({"id":cursor.lastrowid}),201

@app.route("/api/products/<int:id>", methods =["PUT"])
def update_product(id):
    data= request.json
    with sqlite3.connect(DATABASE) as conn:
          conn.execute(
                "UPDATE products_table SET nombre=?, precio=? WHERE id=?",
                (data["nombre"], data["precio"], id)
          )
          conn.commit()

    return jsonify({"message":"Product Updated"}),201


@app.route("/api/products/<int:id>", methods =["DELETE"])
def remove_product(id):
    with sqlite3.connect(DATABASE) as conn:
          conn.execute(
                (f"DELETE FROM products_table WHERE id={id}")
                
          )
          conn.commit()

    return jsonify({"message":"Product Removed"}),201


if __name__ == "__main__":
        app.run(debug=True)