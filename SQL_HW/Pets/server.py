from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'pet')

@app.route('/')
def index():
    query = "SELECT * FROM pet"                      
    friends = mysql.query_db(query)                        
    return render_template('index.html', all_pet=pet)

@app.route('/pet', methods=['POST'])
def create():
    query = "INSERT INTO pet (name, type, created_at, updated_at) VALUES (:name, :type, NOW(), NOW())"
    data = {
             'name': request.form['name'],
             'type':  request.form['type'],
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/pet/<pet_id>')
def show(pet_id):
    query = "SELECT * FROM pet WHERE id = :specific_id"
    data = {'specific_id': pet_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_pet=pet[0])

@app.route('/update_pet/<pet_id>', methods=['POST'])
def update(pet_id):
    query = "UPDATE pet SET name = :name, type = :type, WHERE id = :id"
    data = {
             'name': request.form['name'],
             'type':  request.form['type'],
             'id': pet_id
           }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)