# -*- coding: latin-1 -*-

from flask import render_template, redirect, url_for
from Qudurat import app, db
from Qudurat.forms import PasswordForm, StudentDataForm
from Qudurat.models import Password, StudenData
import random, string, os, sys

reload(sys)
sys.setdefaultencoding('utf-8')




@app.route("/")
def home():
    

    return render_template("index.html")



@app.route("/enterpassword", methods=["GET", "POST"])
def password_entry():
    form = PasswordForm()

    if form.validate_on_submit():
        password = form.password.data
        if Password.query.filter_by(password=password).first():
            dynamic_string = "".join(random.choice(string.lowercase) for i in range(6))
            password = Password(password=dynamic_string)
            db.session.add(password)
            db.session.commit()
            random_string = Password.query.filter_by(password=dynamic_string)
            return redirect(url_for("data_entry", string=dynamic_string))
        else:
           return redirect(url_for("home"))

    return render_template("enterpassword.html", form=form)


@app.route("/dataentry<string>", methods=["GET", "POST"])
def data_entry(string):
    password = Password.query.filter_by(password=string).first()
    if not password:
        return redirect(url_for("password_entry"))

    db.session.delete(password)
    db.session.commit()
    

    form = StudentDataForm()

    if form.validate_on_submit():
        name = form.name.data
        academic_number = form.academic_number.data
        ID_number = form.ID_number.data
        number_of_try = form.number_of_try.data
        math_degree = form.math_degree.data
        language_degree = form.language_degree.data
        degrees_sum = form.degrees_sum.data
        
        student_data = StudenData(name=name, academic_number=academic_number, ID_number=ID_number, number_of_try=number_of_try, math_degree=math_degree, language_degree=language_degree, degrees_sum=degrees_sum)
        
        db.session.add(student_data)
        db.session.commit()

        return redirect(url_for("home"))


    return render_template("enterdata.html", form=form)



@app.route("/showdata")
def show_data():
    pass
