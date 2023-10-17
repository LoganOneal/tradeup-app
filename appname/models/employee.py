import logging

from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy_utils.types import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine

from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from appname.models import db, Model, ModelProxy, global_encryption_key_iv
from appname.models.workexperience import WorkExperience
from appname.models.education import Education
from appname.models.license import License
from appname.models.skill import Skill
from appname.models.link import Link
from appname.models.user import User


class Employee(Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="employee")

    work_experiences = db.relationship(
        "WorkExperience",
        backref="employee",
    )
    educations = db.relationship(
        "Education",
        backref="employee",
    )
    licenses = db.relationship(
        "License",
        backref="employee",
    )
    skills = db.relationship(
        "Skill",
        backref="employee",
    )
    links = db.relationship(
        "Link",
        backref="employee",
    )

    __mapper_args__ = {
        "polymorphic_identity": "employee",
    }
