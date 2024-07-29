"""users table

Revision ID: c1c663f2a230
Revises: 6cd71ed289b7
Create Date: 2020-07-06 16:57:12.125533

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'c1c663f2a230'
down_revision = '6cd71ed289b7'
branch_labels = None
depends_on = None


def upgrade():
     # ### commands auto generated by Alembic - please adjust! ###
     op.create_table('users',
     sa.Column('id', sa.Integer(), nullable=False),
     sa.Column('name', sa.String(length=50), nullable=False),
     sa.Column('email', sa.String(length=100), nullable=False),
     sa.Column('hashed_password', sa.String(length=100), nullable=False),
     sa.Column('species', sa.Integer(), nullable=False),
     sa.Column('bio', sa.String(length=1000), nullable=True),
     sa.Column('faction', sa.Boolean(), nullable=True),
     sa.Column('credits', sa.BigInteger(), nullable=False),
     sa.Column('user_image', sa.String(length=150), nullable=False),
     sa.Column('force_points', sa.Integer(), nullable=True),
     sa.ForeignKeyConstraint(['species'], ['species.id'], ),
     sa.PrimaryKeyConstraint('id'),
     sa.UniqueConstraint('email')
     )
    
     if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
     # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
