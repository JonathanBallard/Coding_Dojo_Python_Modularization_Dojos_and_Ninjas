from flask import Flask, render_template, request, redirect, session, flash
from config import db, app
from models import Dojo, Ninja




#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database








# routes go here...

@app.route('/')
def index():

    list_of_ninjas = Ninja.query.all()
    list_of_dojos = Dojo.query.all()



    return render_template('index.html', ninjaList = list_of_ninjas, dojoList = list_of_dojos)


@app.route('/create_ninja', methods=['POST'])
def create_ninja():

    first_name = request.form['fname']
    last_name = request.form['lname']
    dojo = request.form['dojo']

    new_ninja = Ninja(first_name=first_name, last_name = last_name, dojo=dojo)
    db.session.add(new_ninja)
    db.session.commit()

    

    return redirect("/")


@app.route('/create_dojo', methods=['POST'])
def create_dojo():

    name = request.form['name']
    city = request.form['city']
    state = request.form['state']

    new_dojo = Dojo(name=name, city=city, state=state)
    db.session.add(new_dojo)
    db.session.commit()

    


    return redirect("/")








if __name__ == "__main__":
    app.run(debug=True)




















