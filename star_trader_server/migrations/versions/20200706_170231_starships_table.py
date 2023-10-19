"""starships table

Revision ID: db3f0ede48f5
Revises: c1c663f2a230
Create Date: 2020-07-06 17:02:31.381012

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = 'db3f0ede48f5'
down_revision = 'c1c663f2a230'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    starships_table = op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ship_type', sa.Integer(), nullable=False),
    sa.Column('custom_name', sa.String(length=75), nullable=True),
    sa.Column('sale_price', sa.BigInteger(), nullable=False),
    sa.Column('lightyears_traveled', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('for_sale', sa.Boolean(), nullable=True),
    sa.Column('seller_comment', sa.String(250), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.ForeignKeyConstraint(['ship_type'], ['shiptypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(starships_table,
        [
        {'ship_type': 10, 'custom_name': None, 'sale_price': 1000000, 'lightyears_traveled': 24999, 'owner': 14, 'for_sale': True, 'seller_comment': "The ship that made the Kessel Run in 12 parsecs!", 'post_date': datetime.datetime.now() },
        {'ship_type': 9, 'custom_name': None, 'sale_price': 1000000000000, 'lightyears_traveled': 5, 'owner': 12, 'for_sale': True, 'seller_comment': "Low Mileage!  Slightly used, great for destroying planets and rebel bases.  WARNING Keep Skywalkers away from exhaust ports!", 'post_date': datetime.datetime.now()},
        {'ship_type': 48, 'custom_name': "Obe-Wan's Jedi Starfighter", 'sale_price': 220000, 'lightyears_traveled': 57899, 'owner': 10, 'for_sale': True, 'seller_comment': "Ship priced to move ASAP! Need credits fast to head to Alderaan with Luke!  Spent many years burried in the sands of Tatooine, sand everywhere...", 'post_date': datetime.datetime.now()},
        {'ship_type': 14, 'custom_name': None, 'sale_price': 119999, 'lightyears_traveled': 67899 , 'owner': 4, 'for_sale': True, 'seller_comment': "The Emperor is buying me a new TIE Fighter, need to sell this one.  Serious inquiries only. No rebel scum please",'post_date': datetime.datetime.now()},
        {'ship_type': 27, 'custom_name': "Home 1", 'sale_price': 100000000, 'lightyears_traveled': 124995, 'owner': 27, 'for_sale': True, 'seller_comment': "It's a trap!  No price should be this low for a ship this great!",'post_date': datetime.datetime.now()},
        {'ship_type': 21, 'custom_name': "Boba Fett's Ship", 'sale_price': 249999, 'lightyears_traveled': 24587, 'owner': 22, 'for_sale': True, 'seller_comment': "Great ship for hunting down Jedis or smugglers named Solo",'post_date': datetime.datetime.now()},
        {'ship_type': 12, 'custom_name': "Lauretta", 'sale_price': 105000, 'lightyears_traveled': 350950, 'owner': 18, 'for_sale': True, 'seller_comment': 'Used X-wing fighter for sale, needs new hyperdrive, cockpit smells like Wookie...','post_date': datetime.datetime.now()},
        {'ship_type': 3, 'custom_name': "Star Destroyer #127", 'sale_price': 12000000, 'lightyears_traveled': 157000, 'owner': 21, 'for_sale': True, 'seller_comment': 'I have so many Star Destroyers, this one no longer pleases me.','post_date': datetime.datetime.now()},
        {'ship_type': 22, 'custom_name': "Imperial Shuttle #291", 'sale_price': 143000, 'lightyears_traveled': 251000, 'owner': 14, 'for_sale': True, 'seller_comment': 'Won this from a Corellian Trader in a game of sabacc...  Its no Millenium Falcon so its up for sale!','post_date': datetime.datetime.now()},
        {'ship_type': 15, 'custom_name':"Vader's Capital Ship" , 'sale_price': 750000000, 'lightyears_traveled': 150000, 'owner': 4, 'for_sale': True, 'seller_comment': 'But it while you can, it may crash into the second Death Star one day and explode, who knows?', 'post_date': datetime.datetime.now()},
        {'ship_type': 47, 'custom_name': "Rebel Freighter", 'sale_price': 620000, 'lightyears_traveled': 430000, 'owner': 25, 'for_sale': True, 'seller_comment': 'This ship is no "Falcon" but I lost that ship in a card game to Han Solo... It will make the Kessel Run in 34 parsecs!', 'post_date': datetime.datetime.now()},
        {'ship_type': 33, 'custom_name': "Imperial Cargo Ship" , 'sale_price': 165000, 'lightyears_traveled': 148005, 'owner': 24, 'for_sale': True, 'seller_comment': 'Great cargo ship, smells like Bantha...', 'post_date': datetime.datetime.now()},
        {'ship_type': 41, 'custom_name': "Imperial transport ship", 'sale_price': 3120000, 'lightyears_traveled': 224725, 'owner': 17, 'for_sale': True, 'seller_comment': 'Need to sell, this ship has too much leg room for me...', 'post_date': datetime.datetime.now()},
        {'ship_type': 2, 'custom_name': "Tantive IV" , 'sale_price': 1734000, 'lightyears_traveled': 425000, 'owner': 5, 'for_sale': True, 'seller_comment': "It's been in my family for years, I don't know if I can part with it, for under 1,700,000 credits...", 'post_date': datetime.datetime.now()},
        {'ship_type': 23, 'custom_name': "Nebulon Escort Frigate", 'sale_price': 3999000, 'lightyears_traveled': 625000, 'owner': 31, 'for_sale': True, 'seller_comment': "Don't tell the Rebellion I have one of these ships for sale!", 'post_date': datetime.datetime.now()},
        {'ship_type': 30, 'custom_name': "UT-60D U-wing", 'sale_price': 120000, 'lightyears_traveled': 215999, 'owner': 9, 'for_sale': True, 'seller_comment': "I don't think Cassain is coming back for his ship... Make me an offer!", 'post_date': datetime.datetime.now()},
        {'ship_type': 5, 'custom_name': "Imperial Landing Craft", 'sale_price': 100000, 'lightyears_traveled': 255999, 'owner': 30, 'for_sale': True , 'seller_comment': 'They just left this behind after blowing up the death star, anyone want it?', 'post_date': datetime.datetime.now()},
        {'ship_type': 40, 'custom_name': "Naboo Transport W-2", 'sale_price': 370000, 'lightyears_traveled': 182575, 'owner': 33, 'for_sale': True, 'seller_comment': 'Ahhh NUBIAN!  I give you great price!', 'post_date': datetime.datetime.now()},
        {'ship_type': 19, 'custom_name': "ARC Hornet", 'sale_price': 145000, 'lightyears_traveled': 190500, 'owner': 29, 'for_sale': True, 'seller_comment': 'Floats like a butterfly, stings like a HORNET!', 'post_date': datetime.datetime.now()},
        {'ship_type': 28, 'custom_name': "A-wing Model 2", 'sale_price': 50000, 'lightyears_traveled': 65000, 'owner': 28, 'for_sale': True, 'seller_comment': "Great opportunity for an Imperial to own some Rebel Tech! (It's really made out of cardboard.)", 'post_date': datetime.datetime.now()}
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starships')
    # ### end Alembic commands ###
