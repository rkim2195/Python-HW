from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruit_count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    fruits = {
    'sb': request.form['strawberry'],
    'rb': request.form['raspberrt'],
    'ap': request.form['apple'],
    'fn': request.form['first_name'],
    'ln': request.form['last_name'],
    'sid': request.form['student_name']
    'fc': fruit_count
    'order_date': datetime.today().strftime('%B %d' + ' at ' + ' %I:%M:%S %p')
    }
    return render_template("checkout.html", deli_fruits=fruits)

@app.route('/fruits')         
def fruits():

    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    