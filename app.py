# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data"
mongo = PyMongo(app)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_data = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", mars_data=mars_data)

# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    mars_data = scraper.scrape_mars_data()

    # Insert mars data into database
    mongo.db.collection.insert_one(mars_data)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
