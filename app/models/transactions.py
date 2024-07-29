from .db import db, environment, SCHEMA, add_prefix_for_prod
# from ..models.starships import Starship
# from ..models.users import User


class Transaction(db.Model):
    __tablename__ = "transactions"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    seller = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    starship = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("starships.id")))
    sale_price = db.Column(db.BigInteger, nullable=False)
    sale_date = db.Column(db.DateTime, nullable=False)

    ship = db.relationship("Starship", back_populates="transaction")


    def to_dict(self):
        return {"id": self.id, "buyer": self.buyer, "seller": self.seller, "starship": self.starship,
                "sale_price": self.sale_price, "sale_date": self.sale_date}
