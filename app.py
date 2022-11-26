from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 6,
        "category": "European Country Name",
        "word": "France"
    },
    {
        "inputs": 6,
        "category": "South American Country Name",
        "word": "Brazil"
    },
    {
        "inputs": 5,
        "category": "Asian Country Name",
        "word": "Japan"
    }    
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(templates)
    })

if __name__ == '__main__':
  app.run()