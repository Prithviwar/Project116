# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Prithvi" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Vinoo"
    age = "48"
# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Dhanya"
    age = "42"
# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "Pannag"
    age = "16"

# add other routes, if you want
@app.route("/sister")
def sister():
    name = "Dyuthi"
    age = "10"



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
