from wtforms import Form, TextAreaField, validators, PasswordField


class LoginForm(Form):
    email = TextAreaField('email', [validators.Length(min=6, max=100)])
    password = PasswordField('password', [validators.Length(min=4, max=100)])


