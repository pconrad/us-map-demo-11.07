import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

if __name__=="__main__":
    port_number = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port_number)
