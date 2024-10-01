from flask import Flask

app = Flask(__name__)

# @app.route("/optimization")
@app.route("/")
def optimization():
    return "<p>Hello world! We did some optimizations</p>"