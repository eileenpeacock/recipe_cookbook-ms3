#import modules
import os
from flask import Flask
from flask import render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# # set app environment variables

app.config["MONGO_DBNAME"] = 'recipeDB'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)

# #Set homepage
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template("index.html")

#Get Recipes
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

#Add Recipes
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")

#Submit Recipe
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

#Global settings
# if __name__ == '__main__':      
#     app.run(host=os.environ.get('IP'),              
#     port=int(os.environ.get('PORT')),              
#     debug=True)

# # local settings
if __name__=='__main__':
    app.run(host = '0.0.0.0',
    port = int('8080'),
    debug=True) 