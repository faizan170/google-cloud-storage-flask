from flask import Flask, request, jsonify
import json, os
from utils import process_tree
from storage import create_folder, delete_folder, upload_blob, list_blobs
app = Flask(__name__)

def jsonifyData(data):
    my_json = data.decode('utf8')
    data = json.loads(my_json)
    return data

def getPath(data):
    return os.path.join(data["userId"], data["courseId"], data["assignmentId"])


@app.route("/")
def main():
    return "Gcloud app is working"

@app.route("/create-folder", method=["POST"])
def createFolderRequest():
    data = jsonifyData(request.data)
    print(getPath(data))
    resp = create_folder(os.path.join(getPath, data["path"]))
    return jsonify({"type":"success"})

@app.route("/delete-folder", method=["POST"])
def deleteFolderRequest():
    data = jsonifyData(request.data)
    resp = delete_folder(os.path.join(getPath, data["path"]))
    return jsonify({"type":"success"})


@app.route("/upload-file", method=["POST"])
def uploadFileRequest():
    data = jsonifyData(request.data)
    with open("temp/" + data["path"], "w+") as file:
        file.write(data["code"])
    resp = upload_blob("temp/" + data["path"], os.path.join(getPath, data["path"]))
    os.remove("temp/" + data["path"])
    return jsonify({"type":"success"})

@app.route("/get-dirs-structured-data", method=["POST"])
def getDirsData():
    data = jsonifyData(request.data)
    mainPath = getPath(data)
    data = list_blobs(mainPath)
    finalData = process_tree(data, mainPath)
    return jsonify({"type":"success", "data" : finalData})

if __name__ == "__main__":
    app.run()
