from .db import db, environment, SCHEMA, add_prefix_for_prod
# from ..models.transactions import Transaction
# from ..models.starships import Starship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    hashed_password = db.Column(db.String(250), nullable=False)
    species = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("species.id")), nullable=False)
    bio = db.Column(db.Text)
    faction = db.Column(db.Boolean, default=False)
    credits = db.Column(db.BigInteger, nullable=False)
    user_image = db.Column(db.String(250), nullable=False)
    force_points = db.Column(db.Integer, default=0)

    starships = db.relationship("Starship", back_populates="user", cascade="all, delete-orphan")
    species_info = db.relationship("Species", back_populates="user_info")
   


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "species": self.species, "bio": self.bio,
                "faction": self.faction, "credit": self.credits, "user_image": self.user_image, "force_points": self.force_points, "starships": {}}
