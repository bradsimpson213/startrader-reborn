"""migration for species, shiptypes, users, starships and transactions

Revision ID: ee42b99a447f
Revises: 
Create Date: 2024-07-29 21:23:58.603252

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'ee42b99a447f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shiptypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=50), nullable=False),
    sa.Column('starship_class', sa.String(length=50), nullable=False),
    sa.Column('manufacturer', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('hyperdrive_rating', sa.Float(), nullable=False),
    sa.Column('mglt', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('passenger', sa.Integer(), nullable=False),
    sa.Column('cargo', sa.BigInteger(), nullable=False),
    sa.Column('consumables', sa.String(length=30), nullable=False),
    sa.Column('cost_credits', sa.BigInteger(), nullable=False),
    sa.Column('ship_image', sa.String(length=150), nullable=False),
    sa.Column('unique', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('species_type', sa.String(length=75), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.Column('species', sa.Integer(), nullable=False),
    sa.Column('bio', sa.Text, nullable=True),
    sa.Column('faction', sa.Boolean(), nullable=True),
    sa.Column('credits', sa.BigInteger(), nullable=False),
    sa.Column('user_image', sa.String(length=250), nullable=False),
    sa.Column('force_points', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['species'], ['species.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ship_type', sa.Integer(), nullable=False),
    sa.Column('custom_name', sa.String(length=75), nullable=True),
    sa.Column('sale_price', sa.BigInteger(), nullable=False),
    sa.Column('lightyears_traveled', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('for_sale', sa.Boolean(), nullable=True),
    sa.Column('seller_comment', sa.String(length=250), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.ForeignKeyConstraint(['ship_type'], ['shiptypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buyer', sa.Integer(), nullable=True),
    sa.Column('seller', sa.Integer(), nullable=True),
    sa.Column('starship', sa.Integer(), nullable=True),
    sa.Column('sale_price', sa.BigInteger(), nullable=False),
    sa.Column('sale_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['buyer'], ['users.id'], ),
    sa.ForeignKeyConstraint(['seller'], ['users.id'], ),
    sa.ForeignKeyConstraint(['starship'], ['starships.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    if environment == "production":
        op.execute(f"ALTER TABLE shiptypes SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE species SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE starships SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE transactions SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('starships')
    op.drop_table('users')
    op.drop_table('species')
    op.drop_table('shiptypes')
    # ### end Alembic commands ###
