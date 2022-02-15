from flask import Flask, request, make_response, jsonify
import json
from back.mbi import mbi
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type' 
generatorMBI = mbi()

@app.route("/")
@cross_origin()
def serve():
    print('serve')
    return "hello"

#Verify an MBI Passed in
@app.route("/verify", methods=['POST'])
@cross_origin()
def verifyMBI():
    if 'mbi' in request.json:
        return make_response(jsonify(generatorMBI.verify(request.json['mbi'])),200)
    else:
        return make_response(jsonify({"error":"error"}),500)
    
#Generate an MBI ID
@app.route("/generate", methods=['GET'])
@cross_origin()
def generateMBI():
    return make_response(jsonify(generatorMBI.generate()),200)