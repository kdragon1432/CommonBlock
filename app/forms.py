from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, InputRequired, NumberRange

class SearchForm(FlaskForm):
    min_rent = IntegerField('Minimum Rent', validators=[DataRequired()])
    max_rent = IntegerField('Maximum Rent', validators=[DataRequired()])
    num_bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    lat = HiddenField(validators=[DataRequired()])
    lng = HiddenField(validators=[DataRequired()])
    submit = SubmitField('Search')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class EditAccount(FlaskForm):
    first_name = StringField('First Name', validators=[Length(max=20)])
    last_name = StringField('Last Name',validators=[Length(max=20)])
    age = IntegerField("Age",validators=[InputRequired()])
    submit = SubmitField('Edit Account')

class ReviewForm(FlaskForm):
    review_type = SelectField('Review Type', choices=[('user', 'User'), ('apartment', 'Apartment')], validators=[InputRequired()])
    name_or_address = TextAreaField('Name or Address', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[InputRequired(), NumberRange(min=1, max=5)])
    comment = TextAreaField('Comment')