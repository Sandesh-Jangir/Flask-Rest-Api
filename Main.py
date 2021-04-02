from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def Py_Api():
    Data = {
        "Author":"Sandesh",
        "Editor":"Visual Studio Code",
        "Email":"noreply@example.com"
    }
    Api = jsonify(Data)
    return Api

if __name__ == "__main__":
    app.run(debug=True, port=80)