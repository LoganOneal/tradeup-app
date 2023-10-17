from appname.models import db, Model

class WorkExperience(Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    job_title = db.Column(db.String())
    company = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    start_date = created = db.Column(db.DateTime(timezone=True))
    end_date = created = db.Column(db.DateTime(timezone=True))
    current_job = db.Column(db.Boolean(), default=False)
    description = db.Column(db.String())

    def __str__(self):
        return f"{self.job_title} at {self.company}"
