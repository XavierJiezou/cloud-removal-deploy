from flask import Flask, jsonify, request, render_template, redirect, url_for
import torchvision.transforms as transforms
transforms.Resize
import torch.nn.functional as F
from torchvision import models
import torch.nn as nn
from PIL import Image
import numpy as np
import torch
import io, re, os
from inference import cloud_remove


app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


# model_thin = Generator(0)
# model_thick = Generator(0)
# model_thin.load_state_dict(torch.load('model_thin.pth'))
# model_thick.load_state_dict(torch.load('model_thick.pth'))
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model_thin.to(device)
# model_thick.to(device)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    file.save('./static/img/upload/inp.png')
    cloud_cover = request.values.get( "cloud-cover")
    cloud_remove(cloud_cover, 'inp.png','out.png')
    return jsonify({'outdir': url_for('static', filename='img/result/out.png')})


@app.route('/result_thin')
def result_thin():
    return render_template('index_1.html')


@app.route('/result_thick')
def result_thick():
    return render_template('index_2.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='9000')
