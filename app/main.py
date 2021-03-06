from flask import Flask
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
# cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/')
# @cross_origin
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
