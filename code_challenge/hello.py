import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
     result = 'Please input a dividend and divisor.'
     return render_template('start.html', result = result)
    if request.method == 'POST':
     result1 = float((request.form['dividend']))
     result2 = float((request.form['divisor']))
     result = result1/result2
     return render_template('start.html', result = result)



app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
