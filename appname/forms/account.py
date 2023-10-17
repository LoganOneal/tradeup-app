from appname.forms import BaseForm
from wtforms import BooleanField, validators, StringField, FieldList, FormField, DateField

class ChangeProfileForm(BaseForm):
    name = StringField("Name", validators=[validators.InputRequired()])
    bio = StringField("Bio", validators=[validators.InputRequired()])


class WorkExperienceForm(BaseForm):
    job_title = StringField("Job Title")
    company = StringField("Company")
    position = StringField("Position")
    start_date = DateField("Start Date")
    end_date = DateField("End Date")
    current_position = BooleanField("Current Position", default=False)
    description = StringField("Description")


class ChangeEmployeeProfileForm(ChangeProfileForm):
    bio = StringField("Bio", validators=[validators.InputRequired()])
