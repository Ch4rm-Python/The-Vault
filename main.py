from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def default():
  return render_template("default.html")

app.run(host='0.0.0.0', port=8080)