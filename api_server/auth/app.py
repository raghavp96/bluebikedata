from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/<role>')
def authenticate(role=""):
    credentials = build_credentials(role)

    return jsonify(credentials)

def build_credentials(role):
    creds = {}
    tmp = {}
    with open('role-common.json', 'r') as f:
        creds = json.load(f)
    
    if role == "data-creator":
        with open('role-data-creator.json', 'r') as f:
            tmp = json.load(f)
    else:
        with open('role-default.json', 'r') as f:
            tmp = json.load(f)
    
    creds["user"] = tmp["user"]
    creds["password"] = tmp["password"]
    return creds
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)