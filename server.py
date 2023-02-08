from flask import Flask
from data import me

import json

app = Flask(__name__)  #create new instance; similar to new Task in JS


@app.get("/")
def home():
    return "Hello World!"

@app.get("/about")
def about():
    return "Hethe Allemand"

@app.get("/contact/me")
def contact_me():
    return "hethe.allemand@icloud.com"



####################################################
######################## API -> JSON ###############
####################################################

@app.get("/api/developer")
def developer():
    return json.dumps(me) #parse me into a json string

@app.get("/api/developer/address")
def developer_address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'


app.run(debug=True)
