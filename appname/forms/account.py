from appname.forms import BaseForm
from wtforms import BooleanField, validators, StringField, FieldList, FormField, DateField

class ChangeProfileForm(BaseForm):
    name = StringField("Name", validators=[validators.InputRequired()])
    bio = StringField("Bio", validators=[validators.InputRequired()])


class WorkExperienceForm(BaseForm):
    job_title = StringField("Job Title")
    company = StringField("Company")
    city = StringField("City")
    state = StringField("State")
    position = StringField("Position")
    start_date = DateField("Start Date")
    end_date = DateField("End Date")
    current_position = BooleanField("Current Position", default=False)
    description = StringField("Description")

class EducationForm(BaseForm):
    school_name = StringField("School Name")
    degree = StringField("Degree")
    city = StringField("City")
    state = StringField("State")
    start_date = DateField("Start Date")
    end_date = DateField("End Date")
    currently_enrolled = BooleanField("Currently Enrolled", default=False)
    description = StringField("Description")

class ChangeEmployeeProfileForm(ChangeProfileForm):
    bio = StringField("Bio", validators=[validators.InputRequired()])
