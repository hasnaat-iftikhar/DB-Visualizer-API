from . import db
from enum import Enum

# UserType Enum for User model
class UserTypeEnum(Enum):
    STUDENT = 'student'
    PROFESSIONAL = 'professional'

# Role Enum for User model
class RoleEnum(Enum):
    DEVELOPER = 'developer'
    DATABASE_DESIGNER = 'database_designer'

# User model: Represents a user who can create projects
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False, index=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password = db.Column(db.String(150), nullable=False)
    profile_picture = db.Column(db.String(150), nullable=True)
    user_type = db.Column(db.Enum(UserTypeEnum), nullable=False)
    role = db.Column(db.Enum(RoleEnum), nullable=False)
    company_name = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Define the relationship
    projects = db.relationship('Project', backref='creator', lazy=True, cascade="all, delete-orphan")

# Project model: Represents a project created by a user
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationship with Table: A project can have many tables
    tables = db.relationship('Table', backref='project', lazy=True, cascade="all, delete-orphan")

# Table model: Represents a table in a project
class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationship with Field: A table can have many fields
    fields = db.relationship('Field', backref='table', lazy=True, cascade="all, delete-orphan")

# Field model: Represents a field in a table
class Field(db.Model):
    __tablename__ = 'fields'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
