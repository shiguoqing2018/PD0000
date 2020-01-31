#-*- encoding=UTF-8 -*-
from flask import Flask,render_template

app = Flask(__name__)
@app.route('/profile/<int:uid>')
def profile(uid):
    return render_template('profile.html',uid=uid)
@app.route('/')
def index():
    return 'hello shiguoqing'

if __name__=="__main__":
    app.run(debug=True)
