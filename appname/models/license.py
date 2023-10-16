from appname.models import db, Model

class License(Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    name = db.Column(db.String())
    issuer = db.Column(db.String())
    issuer_date = created = db.Column(db.DateTime(timezone=True))
    expires = db.Column(db.Boolean(), default=False)
    description = db.Column(db.String())
