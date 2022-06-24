from flask import Flask,jsonify
import json
import requests

app = Flask(__name__)

    
@app.route("/api")
def api_route():
    data = {
        "Author":"Sandesh",
        "Editor":"Visual Studio Code",
        "Email":"noreply@example.com"
    }
    # Jsonifying Dict Type "data" to JSON format
    jsonified_data = jsonify(data)
    return jsonified_data

@app.route("/")
def home_route():
    # Fetching Api
    api_url = requests.get("http://localhost:80/api").text
    # Converting API Data to Python Dict Type
    dict_api = json.loads(api_url)

    # Creating a custom message to show using API Data
    str_to_display = f'Author is {dict_api["Author"]} and He uses {dict_api["Editor"]} to write his code and his e-mail is {dict_api["Email"]}'

    return str_to_display

if __name__ == "__main__":
    app.run(debug=True, port=80)