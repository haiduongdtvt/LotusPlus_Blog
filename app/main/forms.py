from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from config import Config

class ReportForm(FlaskForm):
    title = StringField('Tiêu đề cho báo cáo', validators=[DataRequired()])
    job_content = TextAreaField('Nội dung công việc')
    describe = TextAreaField('Mô tả chi tiết công việc')
    result = TextAreaField('Kết quả công việc')
    file = FileField('Hình ảnh báo cáo', validators=[
        FileRequired(),
        FileAllowed((Config.ALLOWED_EXTENSIONS), 
                   'Chỉ các file hình ảnh nằm trong danh mục cho phép mới được gửi lên!')
    ])
    submit = SubmitField('Gửi lên !')