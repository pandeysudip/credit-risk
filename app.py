from flask import Flask, render_template, redirect, jsonify, request
import utilis
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base
import os
# Create an instance of Flask
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# 'postgresql://localhost:5432/credit-risk-eval'


# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# getting the tables from database-1st approach
# test = db.Table('train', db.metadata, autoload=True, autoload_with=db.engine)
# train = db.Table('test', db.metadata, autoload=True, autoload_with=db.engine)
# test_dumy = db.Table('train_dumy', db.metadata,autoload = True, autoload_with = db.engine)
# train_dumy = db.Table('test_dumy', db.metadata,autoload=True, autoload_with=db.engine)
# query be like: db.session.query(train).all()


# getting the tables from database-2nd approach
# reflect an existing database into a new model
#Base = automap_base()
#Base.prepare(db.engine, reflect=True)

# Save references to each table
#train = Base.classes.train
#test = Base.classes.test
#train_dumy = Base.classes.train_dumy
#test_dumy = Base.classes.test_dumy


@ app.route('/')
def home():
    # Return the template
    return render_template('index.html')


@ app.route('/send', methods=["GET", "POST"])
def predic():

    if request.method == "POST":
        loan_amount = request.form.get('loan_amnt')
        interest_rate = request.form.get("int_rate")
        installement = request.form.get("installment")
        anual_income = request.form.get('anual_inc')
        # home_owenership = request.form.get("home_ownership")

        variables = [loan_amount, interest_rate,
                     installement,  anual_income]
        predict = utilis.preprocess(variables)
        predict, *_ = predict
        # Return the template

        return render_template("index.html", pred=variables, prediction=predict)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
