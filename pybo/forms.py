# ---------------------------------------- [edit] ---------------------------------------- #
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired



class QuestionForm(FlaskForm):
    # ---------------------------------------- [edit] ---------------------------------------- #
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
    # ---------------------------------------------------------------------------------------- #

# ---------------------------------------- [edit] ---------------------------------------- #
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
# ---------------------------------------------------------------------------------------- #