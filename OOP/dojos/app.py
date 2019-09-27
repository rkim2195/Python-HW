from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate=Migrate(app, db)

class Dojo(db.Model):
    __tablename__ = "dojos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(145))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    
    
class User(db.Model):	
    __tablename__ = "users"	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojos_id = db.Column(db.Integer, db.ForeignKey("dojos.id"))
    dojo = db.relationship("Dojo", foreign_keys=[dojos_id], backref="ninjas", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    

    def full_name(self):
        return self.first_name + ' ' + self.last_name

@app.route("/")
def main():
    dojo_list = Dojo.query.all()
    return render_template("main.html", dojos = dojo_list)

@app.route("/ninja", methods=['POST'])
def add_ninja():
    new_ninja = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        dojos_id=request.form['dojo']
    )
    db.session.add(new_ninja)
    db.session.commit()
    return redirect("/")

@app.route("/dojo", methods=['POST'])
def add_dojo():
    input_name=request.form['name']
    input_city=request.form['city']
    input_state=request.form['state']
    new_dojo=Dojo(name=input_name, city=input_city, state=input_state)
    db.session.add(new_dojo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)