from flask import Flask

app = Flask(__name__)

@app.route("/bienvenida" , methods=["GET"])
def welcome():
    return {"¡Bienvenidos a nuestra API!"}



@app.errorhandler(404)
def resource_not_found(e):
      return{"error":"Recurso no encontrado"},404

if __name__ == "__main__":
        app.run(debug=True)