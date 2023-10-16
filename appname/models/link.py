from appname.models import db, Model

class Link(Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    title = db.Column(db.String())
    url = db.Column(db.String())
    description = db.Column(db.String())
