from appname.models import db, Model

class Education(Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    school_name = db.Column(db.String())
    degree = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    start_date = created = db.Column(db.DateTime(timezone=True))
    end_date = created = db.Column(db.DateTime(timezone=True))
    currently_enrolled = db.Column(db.Boolean(), default=False)
    description = db.Column(db.String())
