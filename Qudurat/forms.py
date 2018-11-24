# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, ValidationError
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

selectTable = (("1", "1"), ("2", "2"), ("3", "3"), ("4","4"), ("5", "5"))


class StudentDataForm(FlaskForm):

    name = wtforms.StringField("الإسم الرباعي", validators=[DataRequired()])
    academic_number = wtforms.StringField("الرقم الأكاديمي", validators=[DataRequired()])

    ID_number = wtforms.StringField("رقم الهوية", validators=[DataRequired()])
    number_of_try = wtforms.SelectField("المحاولة رقم", choices=selectTable)
    math_degree = wtforms.StringField("درجة الكمي", validators=[DataRequired()])
    language_degree = wtforms.StringField("درجة اللفضي", validators=[DataRequired()])
    degrees_sum = wtforms.StringField("المجموع الكلي", validators=[DataRequired()])
    check_field = wtforms.BooleanField("أشهد أن معلوماتي صحيحة")
    submit = wtforms.SubmitField("إرسال")






class PasswordForm(FlaskForm):

    password = wtforms.StringField("أدخل الرقم السري", validators=[DataRequired()])
    submit = wtforms.SubmitField("تحقق")





















