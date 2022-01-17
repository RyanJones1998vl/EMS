from flask import Flask
from flask import Flask, jsonify, request, Response,g
from . import create_app, db
from timeit import default_timer as timer
import datetime

from flask_cors import CORS
from datetime import datetime
import base64
import io
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from PIL import Image
import numpy as np

import cv2
app = create_app()
db.init_app(app)
CORS(app)
# g.rspt = "hello"
face_detector = cv2.cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
emotion_reg  = load_model('./Inception_Inceptionv2_Maxpool_optimizer_SGDN_batchsize_128-008-0.86.h5')


@app.route('/login', methods=['POST'])
def log_in():
 
    # #print(rs, flush=True)
    
    # imgdata = base64.b64decode(request.form.get("image")[23:])
    # image = Image.open(io.BytesIO(imgdata))
    # # image.show()
    # rs=ClassifyEmotion(np.asarray(image), int(request.form.get("width")), int(request.form.get("height")))
    # #print(rs[0]['emo_label'])
    rs = db.checkAccount(request.form.get("email"),request.form.get("password"))
    response=None
    #print(rs, flush=True)

    if rs:
        response = jsonify({"id":rs[0], "role":rs[1]})
    else:
        response = jsonify({"id":"", "role":""})
    response.headers.add("Access-Control-Allow-Origin", "*")
    #print(response, flush=True)
    
    return response

@app.route('/loadEmployees', methods=['GET'])
def loadEmployees():
 
    # #print(rs, flush=True)
    
    # imgdata = base64.b64decode(request.form.get("image")[23:])
    # image = Image.open(io.BytesIO(imgdata))
    # # image.show()
    # rs=ClassifyEmotion(np.asarray(image), int(request.form.get("width")), int(request.form.get("height")))
    # #print(rs[0]['emo_label'])
    rs = db.loadEmployee()
    # #print(rs)
    response=None

    if rs:
        response = jsonify({"employee":rs})
    else:
        response = jsonify({"employee":""})
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/getSalaries', methods=['GET'])
def getSalaries():
 
    # #print(rs, flush=True)
    
    # imgdata = base64.b64decode(request.form.get("image")[23:])
    # image = Image.open(io.BytesIO(imgdata))
    # # image.show()
    # rs=ClassifyEmotion(np.asarray(image), int(request.form.get("width")), int(request.form.get("height")))
    # #print(rs[0]['emo_label'])
    rs = db.loadSalary()
    # #print(rs)
    response=None

    if rs:
        response = jsonify({"salary":rs})
    else:
        response = jsonify({"salary":""})
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/getFormGivenId', methods=['POST'])
def getFormGivenId():
    print((request.form.get("id"),))
    # #print(rs, flush=True)
    
    # imgdata = base64.b64decode(request.form.get("image")[23:])
    # image = Image.open(io.BytesIO(imgdata))
    # # image.show()
    # rs=ClassifyEmotion(np.asarray(image), int(request.form.get("width")), int(request.form.get("height")))
    # #print(rs[0]['emo_label'])
    rs = db.loadSalary()
    # #print(rs)
    response = jsonify({"data":db.getLeave((request.form.get("id"),))})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # #print(db.getEmployIds())
    print(db.getLeave((request.form.get("id"))))
    return response
#
@app.route('/createEmployee', methods=['POST'])
def createEmployee():
    db.create_employee((request.form.get("id"),
                        request.form.get("gmail"),
                        request.form.get("password"),
                        request.form.get("role"),
                        request.form.get("gender"),
                        request.form.get("name"),
                        request.form.get("id_card"),
                        request.form.get("address_1"),
                        request.form.get("address_2"),
                        request.form.get("dob"),
                        request.form.get("contact"),
                        request.form.get("doj")))
    # #print(rs)
    response=None

    response = jsonify({"result":True})

    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
#
@app.route('/updateEmployee', methods=['POST'])
def updateEmployee():
    #print(request.form)
    db.updateEmployee((
                        request.form.get("gmail"),
                        request.form.get("password"),
                        request.form.get("role"),
                        request.form.get("gender"),
                        request.form.get("name"),
                        request.form.get("id_card"),
                        request.form.get("address_1"),
                        request.form.get("address_2"),
                        request.form.get("dob"),
                        request.form.get("contact"),
                        request.form.get("doj"),
                        request.form.get("id")))
    # #print(rs)
    response=None

    response = jsonify({"result":True})

    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/updateSalary', methods=['POST'])
def updateSalary():
    #print(request.form)
    print(request.form.get("salary"))
    db.updateSalary((  request.form.get("e_id"),
                        request.form.get("salary"),
                        request.form.get("bank"),
                        request.form.get("account"),
                        request.form.get("holder"),
                        request.form.get("tax"),
                        request.form.get("id"),))
    # #print(rs)
    response=None

    response = jsonify({"result":True})

    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/updateLeaveForm', methods=['POST'])
def updateLeaveForm():
    #print(request.form)
    db.updateLeaveForm((  request.form.get("e_id"),
                        request.form.get("type"),
                        request.form.get("start"),
                        request.form.get("to"),
                        request.form.get("reason"),
                        request.form.get("status"),
                        request.form.get("id"),))
    # #print(rs)
    response=None

    response = jsonify({"result":True})

    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/createSalary', methods=['POST'])
def createSalary():
    #print(request.form)
    db.createSalary((  request.form.get("e_id"),
                        request.form.get("salary"),
                        request.form.get("bank"),
                        request.form.get("account"),
                        request.form.get("holder"),
                        request.form.get("tax")))
    # #print(rs)
    response=None

    response = jsonify({"result":True})

    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/createLeaveForm', methods=['POST'])
def createLeaveForm():
    #print(request.form)
    db.createLeaveForm((  request.form.get("e_id"),
                        request.form.get("type"),
                        datetime.now().strftime('%m/%d/%Y'),
                        request.form.get("to"),
                        request.form.get("reason"),
                        request.form.get("status")))
    # #print(rs)
    response=None

    response = jsonify({"result":True})

    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/deleteEmployee', methods=['POST'])
def deleteEmployee():
    db.deleteEmployee((request.form.get("id"),))
    # #print(rs)

    response = jsonify({"rows":db.loadEmployee()})
    #print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/deleteSalary', methods=['POST'])
def deleteSalary():
    db.deleteSalary((request.form.get("id"),))
    # #print(rs)

    response = jsonify({"rows":db.loadSalary()})
    #print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
@app.route('/deleteLeaveForm', methods=['POST'])
def deleteLeaveForm():
    db.deleteLeaveForm((request.form.get("id"),))
    # #print(rs)

    response = jsonify({"rows":db.loadSalary()})
    #print(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
        
@app.route('/getEmployeeIds', methods=['GET'])
def getEmployeeIds():
    
    # #print(rs)
    response = jsonify({"ids":db.getEmployIds()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # #print(db.getEmployIds())
    return response

@app.route('/getEmployee', methods=['POST'])
def getEmployee():
    print(request.form.get("id"))
    #print(request.form)
    #print(request.data)
    # #print(rs)
    response = jsonify({"data":db.getEmployee((request.form.get("id"),))})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # #print(db.getEmployIds())
    return response

@app.route('/getSalary', methods=['POST'])
def getSalary():
    #print(request.form.get("id"))
    #print(request.form)
    #print(request.data)
    # #print(rs)
    response = jsonify({"data":db.getSalary((request.form.get("id"),))})
    # print("getsalary")
    # print(id)
    # print(db.getSalary((request.form.get("id"))))
    response.headers.add("Access-Control-Allow-Origin", "*")
    # #print(db.getEmployIds())
    return response
@app.route('/loadLeaveFormsGivenId', methods=['POST'])
def loadLeaveFormsGivenId():
    #print(request.form.get("id"))
    # #print(rs)
    response = jsonify({"data":db.loadLeaveFormsGivenId((request.form.get("id"),))})
    print(request.form.get("id"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    # #print(db.getEmployIds())
    return response

@app.route('/loadLeaveForms', methods=['GET'])
def loadLeaveForms():
    # #print(request.form.get("id"))
    # #print(request.form)
    # #print(request.data)
    # #print(rs)
    response = jsonify({"data":db.loadLeaveForms()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # #print(db.getEmployIds())
    return response
# getPrediction
#  loadCEmotions
@app.route('/send_image', methods=['POST'])
def send_image():
    print(request.form.get("id"))
    start = timer()
# ...
    imgdata = base64.b64decode(request.form.get("image")[23:])
    
    image = Image.open(io.BytesIO(imgdata))
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    rects = face_detector.detectMultiScale(gray, scaleFactor=1.05,
	    minNeighbors=5, minSize=(30, 30),
	    flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects)!=0:
        id = -1
        mx = 47
        for i in range(len(rects)):
            if mx < rects[i][2]:
                id = i
                mx = rects[i][2]
        if mx >= 48:
            face = gray[rects[id][1]:rects[id][1] + rects[id][3], rects[id][0]:rects[id][0] + rects[id][2]]
            face = cv2.resize(face, (48,48))
            # print(np.reshape(face, (48,48,1)).shape)
            face = np.reshape(face, (48,48,1))
            # print(face/255)
            emotions = emotion_reg.predict(np.array([face/255]))[0]
            # print(emotions)
            # print(np.argmax(emotions, axis = 0))
            if np.argmax(emotions, axis = 0) != -1:
                print(["HELLO"].extend(list(emotions)))
                db.createExpression((str(request.form.get("id")), datetime.now().strftime('%m/%d/%Y'))+ tuple([str(round(float(e),2)) for e in emotions]))
            response = jsonify({"emotion":str(np.argmax(emotions, axis = 0)), "confidence":str(emotions[np.argmax(emotions, axis = 0)])})
    else:
        # db.createExpression(("htc1997", datetime.now().strftime('%m/%d/%Y'))+ tuple([1.0,1.0,1.0,1.00,1.0,1.0]))

        response = jsonify({"emotion":"-1"})
    # response = jsonify({"emotion":"angry", "confidence":0.9})
    # Enable Access-Control-Allow-Origin
    print("Hello")
    response.headers.add("Access-Control-Allow-Origin", "*")
    end = timer()

    print(end - start)
    return response
@app.route('/loadCEmotions', methods=['GET'])
def loadCEmotions():
    # #print(request.form.get("id"))
    # #print(request.form)
    # #print(request.data)
    # #print(rs)
    response = jsonify({"data":db.loadCEmotions(), "rstp":"0"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    print(response)
    # #print(db.getEmployIds())
    return response

@app.route('/stream')
def streamed_response():
    def generate():
        print("HEllo")
        yield 'Hello '
        yield '!'
    return app.response_class(stream_with_context(generate()))

@app.route('/changeRSTP', methods=['POST'])
def changeRSTP():
    # #print(request.form.get("id"))
    # #print(request.form)
    # #print(request.data)
    # #print(rs)
    # print(rspt)
    db.addRspt((request.form.get("rstp"),))
    # rspt = request.form.get("rstp")
    response = jsonify({"data":True})
    response.headers.add("Access-Control-Allow-Origin", "*")
    # print(rspt)
    # #print(db.getEmployIds())
    return response
def gen_frames():  
    while True:
        print("hello" + datetime.now().strftime("%H:%M:%S"))
        yield "hello" + datetime.now().strftime("%H:%M:%S")
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=="__main__":
    # app = create_app()

    app.run(debug=True, host='192.168.108.50')
    
