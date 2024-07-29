from ..models import db, environment, SCHEMA
# from ..models.users import User


class Species(db.Model):
    __tablename__ = "species"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    species_type = db.Column(db.String(75), nullable=False)

    user_info = db.relationship("User", back_populates="species_info")

    def to_dict(self):
        return {"id": self.id, "species_type": self.species_type}
