from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, validators


class EndpointForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    secret = BooleanField('secret', default=False)


class GoogleSheetForm(FlaskForm):
    spreadsheet = SelectField('Spreadsheet', choices=[])
