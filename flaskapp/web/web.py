# from http://flask.pocoo.org/ tutorial
from flask import Flask
import es_example
app = Flask(__name__)

@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    return "Welcome to this website"

@app.route("/example/<int:index>") # take note of this decorator syntax, it's a common pattern
def example(index):
    es_example.load_es_starwars_names()
    return str(es_example.get_starwars_name(index))

if __name__ == "__main__":
    app.run(debug=True)
    reload=True
