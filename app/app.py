# Import dependencies
from flask import Flask, request, redirect, render_template
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Set Connection to Mongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to index.html using data from Mongo 
@app.route("/")
def main():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    
if __name__ = "__main__":
    app.run()