#!/usr/bin/env python
import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.metrics import AUC
import numpy as np
from tensorflow.keras.utils import to_categorical
import pickle




app = Flask(__name__)

# Load your trained model
 
verbose_name = {
0: "Normal",
1: "Doubtful",
2: "Mild",
3: "Moderate",
4: "Severe" 




}

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'knee.h5')

# Load the model if it exists
model = None
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    print(f"Warning: Model file not found at {MODEL_PATH}. Please ensure knee.h5 is available.")

def predict_label(img_path):
	if model is None:
		return "Model not loaded"
	test_image = image.load_img(img_path, target_size=(224,224))
	test_image = image.img_to_array(test_image)/255.0
	test_image = test_image.reshape(1, 224,224,3)

	predict_x=model.predict(test_image) 
	classes_x=np.argmax(predict_x,axis=1)
	
	return verbose_name [classes_x[0]] 
 

# Load your trained model
 


@app.route("/")
@app.route("/first")
def first():
	return render_template('first.html')
    
@app.route("/login")
def login():
	return render_template('login.html')    
@app.route("/chart")
def chart():
	return render_template('chart.html')

@app.route("/performance")
def performance():
	return render_template('performance.html')


@app.route("/index", methods=['GET', 'POST'])
def index():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/tests/" + img.filename	
		img.save(img_path)
		#plt.imshow(img)
		predict_result = predict_label(img_path)


		 

	
	return render_template("result.html", prediction = predict_result, img_path = img_path)



 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)

