#PYTHON PASSWORD GENERATOR, UPDATER, AND WEBPAGE HOST
import qrcode
import random
import string
import os
from flask import Flask, render_template

SSID = 'BananaMan'
security = 'WPA'
password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range (12)])

# SSH Into router, and update password
# TODO

# Generate QR Code for wifi connection image

wifiString = f'WIFI:S:{SSID};T:{security};P:{password}'
wifiQR = qrcode(wifiString)
wifiQR.save('qrlogin.jpg')

# Display on flask webapp

app = flask(__name__)

app.route("/")
def showQR():
    filename = os.path.join(app.config['UPLOAD_FOLDER'], 'qrlogin.jpg')
    return render_template("page.html", user_image = filename)


