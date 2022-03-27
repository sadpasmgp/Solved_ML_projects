# Important imports
from app import app
from flask import request, render_template, url_for
from keras import models
import numpy as np
from PIL import Image
import string
import random
import os

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Loading model
model = models.load_model('app/static/model/intel_image.h5')

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():

	# Execute if request is get
	if request.method == "GET":
		full_filename =  'images/white_bg.jpg'
		return render_template("index.html", full_filename = full_filename)

	# Execute if reuqest is post
	if request.method == "POST":

		# Generating unique image name
		letters = string.ascii_lowercase
		name = ''.join(random.choice(letters) for i in range(10)) + '.png'
		full_filename =  'uploads/' + name

		# Reading, resizing, saving and preprocessing image for predicition 
		image_upload = request.files['image_upload']
		imagename = image_upload.filename
		image = Image.open(image_upload)
		image = image.resize((150,150))
		image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))
		image_arr = np.array(image.convert('RGB'))
		image_arr.shape = (1,150,150,3)

		# Predicting output
		result = model.predict(image_arr)
		ind = np.argmax(result)
		classes = ['buildings','forest','glacier','mountain','sea','street']

		# Returning template, filename, extracted text
		return render_template('index.html', full_filename = full_filename, pred = classes[ind])

# Main function
if __name__ == '__main__':
    app.run(debug=True)
