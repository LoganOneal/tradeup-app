import logging

from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy_utils.types import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine

from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from appname.models import db, Model, ModelProxy, global_encryption_key_iv
from appname.models.user import User
from appname.models.workexperience import WorkExperience
from appname.models.education import Education
from appname.models.license import License
from appname.models.skill import Skill
from appname.models.link import Link


class Employee(User):
    __tablename__ = "employees"
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    employee_id = db.Column(db.String)
    work_experiences = db.relationship(
        "WorkExperience",
        backref="employee",
        lazy=True,
        primaryjoin="Employee.id == WorkExperience.employee_id",
    )
    educations = db.relationship(
        "Education",
        backref="employee",
        lazy=True,
        primaryjoin="Employee.id == Education.employee_id",
    )
    licenses = db.relationship(
        "License",
        backref="employee",
        lazy=True,
        primaryjoin="Employee.id == License.employee_id",
    )
    skills = db.relationship(
        "Skill",
        backref="employee",
        lazy=True,
        primaryjoin="Employee.id == Skill.employee_id",
    )
    links = db.relationship(
        "Link",
        backref="employee",
        lazy=True,
        primaryjoin="Employee.id == Link.employee_id",
    )

    __mapper_args__ = {
        "polymorphic_identity": "employee",
    }
