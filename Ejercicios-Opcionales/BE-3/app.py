from flask import Flask,request,jsonify
import json

app = Flask(__name__)


products = []


@app.route("/api/products", methods=["GET"])
def get_product_list():
        with open("products.json" , "r") as file:
              data = json.load(file)
        return jsonify({"products":data})


@app.route("/api/products", methods=["POST"])
def create_product_list():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
         return jsonify({"error":"Faltan Campos"})
 
    with open("products.json" , "r") as file:
        existing_products = json.load(file)

    new_product = {
        "id": len(existing_products)+1,
        "name": data["name"],
        "price": data["price"]   
    }

    existing_products.append(new_product)

    with open("products.json" , "w") as file:
          json.dump(existing_products, file, indent= 4)

    return jsonify({"message":"Producto creado con Éxito","product":new_product})




if __name__ == "__main__":
        app.run(debug=True)