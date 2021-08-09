import camelot
import os
from flask import Flask,jsonify,request
from flask import send_file
main=Flask(__name__)

@main.route("/generatePDFToCSV",methods=["POST"])
def generateCSVFile():
    json_data = request.get_json()
    filename1 = json_data["fileName"]
    tables = camelot.read_pdf(filename1, flavor='stream')
    print(tables.n)
    print(tables[0].df)
    tables.export('data.csv', f='csv', compress=True)
    return jsonify(os.path.abspath("data.zip"))


@main.route("/hi",methods=["GET"])
def hi():
    return "hi"

@main.route("/delete",methods=["DELETE"])
def deleteFile():
    json_data=request.get_json()
    filename1=json_data["fileName"]

    print(filename1)
    os.remove(filename1)
    print("File Removed!")
    return jsonify("File Removed")

if(__name__=="__main__"):
    main.run(host='0.0.0.0',debug=True)

