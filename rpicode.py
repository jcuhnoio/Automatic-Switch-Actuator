from adafruit_motorkit import MotorKit
from RPi.GPIO as GPIO
import time
import pyrebase
from collections import OrderedDict

firebaseConfig = {
  apiKey: "AIzaSyCuzQ6QIjGh3D_jOvUxxjwj9GJjSVcyQlw",
  authDomain: "automatic-switch-actuator.firebaseapp.com",
  databaseURL: "https://automatic-switch-actuator-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "automatic-switch-actuator",
  storageBucket: "automatic-switch-actuator.appspot.com",
  messagingSenderId: "857715037947",
  appId: "1:857715037947:web:a06d53436a8272e82fc25e",
  measurementId: "G-J1LJB4TJE9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
on = GPIO.output(18, 1)
off = GPIO.output(17, 1)

while True:
    if state_ref.child("state").get().val() == OrderedDict([('state', "on")]):
        on
        time.sleep(1)
    if state_ref.child("state").get().val() == OrderedDict([('state', "off")]):
        off
        time.sleep(1)
    GPIO.output(18, 0)
    GPIO.output(17, 0)
    time.sleep(0.1)