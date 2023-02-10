from flask import Flask, abort
from data import me, mock_catalog

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

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)

@app.get("/api/catalog/count")
def count_products():
    count = len(mock_catalog)
    return json.dumps(count)


@app.get("/api/category/<tart>")
def prods_by_category(tart):
    results = []
    for prod in mock_catalog:
        if prod["category"] == tart:
            results.append(prod)

    return json.dumps(results)


@app.get("/api/product/<id>")
def prod_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    # not found
    return abort(404, "Invalid ID")


@app.get("/api/product/search/<text>")
def search_product(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)
    
    return json.dumps(results)


@app.get("api/categories")
def get_categories():
    results = []
    for prod in mock_catalog:
        cat = prod["category"]



app.run(debug=True)
