from flask_wtf import Flask_Form
import wtforms
from wtforms.validators import DataRequired, ValidationError


selectTable = (("1", "1"), ("2", "2"), ("3", "3"), ("4","4"), ("5", "5"))


class StudentDataForm(Flask_Form):

    name = wtforms.StringField("الإسم الرباعي", validators=[DataRequired()])
    academic_number = wrforms.StringField("الرقم الأكاديمي", validators=[DataRequired()])

    ID_number = wtforms.StringField("رقم الهوية", validators=[DataRequired])
    number_of_try = SelectField("المحاولة رقم", chices=selectTable, validators=[DataRequired()])
    math_degree = StringField("درجة الكمي", validators=[DataRequired()])
    language_degree = StringField("درجة اللفضي", validators=[DataRequired()])
    degrees_sum = StringField("المجموع الكلي", validators=[DataRequired])
    check_field = BooleanField("أشهد أن معلوماتي صحيحة")
    submit = SubmitField("إرسال")

    def validate_check_field(self, check_field):

        if not check_field:
            raise ValidationError("يجب عليك التحقق من هذا الحقل")





class PasswordForm(FlaskForm):

    password = StringField("أدخل الرقم السري", validators=[DataRequired()])






















