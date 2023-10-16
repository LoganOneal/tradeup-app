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

class Employee(User):
    id = db.Column(db.Integer(), primary_key=True)
    work_experiences = db.relationship('WorkExperience', backref='employee', lazy=True)
    e