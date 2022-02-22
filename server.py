from flask import Flask
from flask_restful import Resource
from flask_restful import Api

import numpy as np
import cv2


import werkzeug
from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument("file", type = werkzeug.datastructures.FileStorage, location = "files")


app = Flask(__name__)
api = Api(app)

import base64



class ImageServer(Resource):

    def _decode(self, image):
        image = np.fromstring(image, np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)

        return image


    def _encode(self, image):
        _, encoded_image = cv2.imencode(".jpg", image)
        image_data = base64.b64encode(encoded_image).decode("utf-8")

        return f"data:image/jpeg;base64,{image_data}"



    def post(self):
        data = parser.parse_args()
        image = data["file"].read()
        image = self._decode(image = image)
        image = self._encode(image = image)


        return {"image" : image}

api.add_resource(ImageServer, "/")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
