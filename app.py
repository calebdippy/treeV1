from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/generate-trees', methods=['POST'])
def generate_trees():
    data = request.json
    image_data = data['image']
    
    # Decode the image
    image_data = image_data.split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Placeholder: Process the image and generate trees
    result_image = image  # This should be the processed image with trees

    # Encode the result image to base64
    _, buffer = cv2.imencode('.png', result_image)
    result_image_base64 = base64.b64encode(buffer).decode('utf-8')

    return jsonify({ 'result': 'data:image/png;base64,' + result_image_base64 })

if __name__ == '__main__':
    app.run(debug=True)