import os
from flask import Flask, request, redirect, jsonify, url_for, make_response
from werkzeug.utils import secure_filename

import trip_data

api_svc_url = os.getenv("API_SVC_URL", "http://localhost:8001/")

dir_path = os.path.dirname(os.path.realpath(__file__))
upload_folder = '/uploads'
allowed_extensions = set(['csv'])
renamed_csv_file = "data.csv"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = dir_path + '/' + upload_folder if dir_path != "/" else upload_folder

def allowed_file(filename):
    if "." in filename:
        file_ext = filename.split(".")[-1]
        if file_ext in allowed_extensions:
            return True
    return False

@app.route('/upload', methods=['POST'])
def upload_file():
    result = {}

    if 'file' not in request.files:
        result["status"] = "No file attribute in POST request!"
    else:
        file = request.files['file']
        if file.filename == '':
            result["status"] = "No selected file"
        
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result["status"] = "File Uploaded"
            result["response"] = convertCSVToJSONandDoSomeStuffHere(filename, api_svc_url)

    return jsonify(result)

def convertCSVToJSONandDoSomeStuffHere(filename, api_url):
    return trip_data.default_convert_csv_to_json(app.config['UPLOAD_FOLDER'] + '/' + filename, api_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)