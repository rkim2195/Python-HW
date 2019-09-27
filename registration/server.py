from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'abcd1234password'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    passFlag = True
    if len(request.form['first_name']) < 1:
        flash('Error! Invalid first name!', 'wrong')
        passFlag = False
    elif not request.form['first_name'].isalpha():
        flash('First name has non-alpha character!', 'wrong')
        passFlag = False
    if len(request.form['last_name']) < 1:
        flash('Error! Invalid last name!', 'wrong')
        passFlag = False
    elif not request.form['last_name'].isalpha():
        flash('Last name has a non-alpha character!', 'wrong')
        passFlag = False
    if len(request.form['email']) < 1:
        flash('Error! Invalid email', 'wrong')
        passFlag = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email format!', 'wrong')
        passFlag = False
    if len(request.form['password']) < 6:
        flash('Password must contain at least 6 characters!', 'wrong')
        passFlag = False
    if request.form['password'] != request.form['confirm_password']:
        flash('Password does not match!', 'wrong')
        passFlag = False

    if passFlag == True:
        flash('Success!', 'success')
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)