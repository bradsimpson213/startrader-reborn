from app.models import db, environment, SCHEMA, Shiptype
from sqlalchemy.sql import text


def seed_shiptypes():
    shiptype_1 = Shiptype(
                    type_name='CR90 Corvette', 
                    starship_class='Star Cruiser', 
                    manufacturer='Corellian Engineering Company', 
                    model='CR90 Corvette', 
                    hyperdrive_rating= 2.0, 
                    mglt=60, 
                    length=150,
                    crew=30, 
                    passenger=600, 
                    cargo=3000000, 
                    consumables='1 year', 
                    cost_credits= 3500000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/02.jpg', 
                    unique=False,
    )
    
    shiptype_2 = Shiptype(
                    type_name='Star Destroyer', 
                    starship_class='Star Dreadnought', 
                    manufacturer='Kuat Drive Yard', 
                    model='Imperial I-class Star Destroyer', 
                    hyperdrive_rating= 2.0, 
                    mglt=60, 
                    length=1600,
                    crew=47060, 
                    passenger=0, 
                    cargo=36000000, 
                    consumables='2 years', 
                    cost_credits=150000000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/03.jpg', 
                    unique=False,
    )
    
    shiptype_3 = Shiptype(
                    type_name='Sentinel-class Landing Craft', 
                    starship_class='Transport',
                    manufacturer='Sienar Fleet Systems', 
                    model='Sentinel-class Landing Craft', 
                    hyperdrive_rating=1.0, 
                    mglt=70, 
                    length=38,
                    crew=5, 
                    passenger=75, 
                    cargo=180000, 
                    consumables='1 month', 
                    cost_credits=240000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/05.jpg', 
                    unique=False,
    )
    
    shiptype_4 = Shiptype(
                    type_name='Death Star', 
                    starship_class='Star Dreadnought', 
                    manufacturer='Sienar Fleet System', 
                    model='D5-1 Orbital Battle Station', 
                    hyperdrive_rating=4.0, 
                    mglt=10, 
                    length=120000,
                    crew=342953, 
                    passenger=843342, 
                    cargo=1000000000000, 
                    consumables='3 years', 
                    cost_credits=1000000000000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/09.jpg', 
                    unique=True,
    )
    
    shiptype_5 = Shiptype(
                    type_name='Millennium Falcon', 
                    starship_class='Freighter', 
                    manufacturer='Corellian Engineering Corporation', 
                    model='YT-1300 Light Freighter', 
                    hyperdrive_rating=0.5, 
                    mglt=75, 
                    length=35,
                    crew=4, 
                    passenger=6, 
                    cargo=100000, 
                    consumables='2 months', 
                    cost_credits=100000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/10.jpg', 
                    unique=True,
    )
    shiptype_6 = Shiptype(  
                    type_name='Y-wing', 
                    starship_class='Starfighter', 
                    manufacturer='Koensayr Manufacturing', 
                    model='BTL Y-wing', 
                    hyperdrive_rating=1.0, 
                    mglt=80, 
                    length=14,
                    crew=2, 
                    passenger=0, 
                    cargo=110, 
                    consumables='1 week', 
                    cost_credits=134999, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/11.jpg', 
                    unique=False,
    )

    shiptype_7 = Shiptype(
                    type_name='X-wing', 
                    starship_class='Starfighter', 
                    manufacturer='Incom Corporation', 
                    model='T-65 X-wing', 
                    hyperdrive_rating=1.0, 
                    mglt=100, 
                    length=13,
                    crew=1, 
                    passenger=0, 
                    cargo=110, 
                    consumables='1 week', 
                    cost_credits=149999, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/12.jpg', 
                    unique=False,
    )
        
    shiptype_8 = Shiptype(
                    type_name='TIE Advanced x1', 
                    starship_class='Starfighter', 
                    manufacturer='Sienar Fleet System', 
                    model='Twin Ion Engine Advanced x1', 
                    hyperdrive_rating=1.0, 
                    mglt=105, 
                    length=9,
                    crew=1, 
                    passenger=0, 
                    cargo=150, 
                    consumables='5 days', 
                    cost_credits=79999, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/13.jpg', 
                    unique=False,
    )

    shiptype_9 = Shiptype(
                    type_name="Darth Vader's TIE Fighter", 
                    starship_class='Starfighter', 
                    manufacturer='Sienar Fleet System', 
                    model='Experimental Twin Engine Advnced x2', 
                    hyperdrive_rating=1.0, 
                    mglt=105, 
                    length=10,
                    crew=1, 
                    passenger=0, 
                    cargo=150, 
                    consumables='5 days', 
                    cost_credits=135999, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/14.jpg', 
                    unique=True,
    )
        
    shiptype_10 = Shiptype(    
                    type_name='Executor', 
                    starship_class='Star Dreadnought', 
                    manufacturer='Kuat Drive Yard', 
                    model='Executor-class Star Dreadnought', 
                    hyperdrive_rating=2.0, 
                    mglt=40, 
                    length=19000,
                    crew=279144, 
                    passenger=38000, 
                    cargo=250000000, 
                    consumables='6 years', 
                    cost_credits=1143350000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/15.jpg', 
                    unique=True,
    )

    shiptype_11 = Shiptype(
                    type_name='Rebel Transport', 
                    starship_class='Transport', 
                    manufacturer='Gallofree Yards, Inc.', 
                    model='GR-75 Medium Transport', 
                    hyperdrive_rating=4.0, 
                    mglt=20, 
                    length=90,
                    crew=6, 
                    passenger=90, 
                    cargo=19000000, 
                    consumables='6 months', 
                    cost_credits=180000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/17.jpg', 
                    unique=False,
    )
        
    shiptype_12 = Shiptype(        
                    type_name='ARC-170 Starfighter', 
                    starship_class='Starfighter', 
                    manufacturer='Incom Corporation', 
                    model='ARC-170 Aggressive Reconnaissance Starfighter', 
                    hyperdrive_rating=1.5, 
                    mglt=70, 
                    length=13,
                    crew=3, 
                    passenger=0, 
                    cargo=250, 
                    consumables='1 month', 
                    cost_credits=180000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/19.jpg', 
                    unique=False,
    )
        
    shiptype_13 = Shiptype(
                    type_name='Slave 1', 
                    starship_class='Transport', 
                    manufacturer='Kuat Systems Engineering', 
                    model='Firespray-31-class Patroll and Attack', 
                    hyperdrive_rating=3.0, 
                    mglt=70, 
                    length=22,
                    crew=1, 
                    passenger=6, 
                    cargo=70000, 
                    consumables='1 month', 
                    cost_credits=343000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/21.jpg', 
                    unique=True,
    )
        
    shiptype_14 = Shiptype(    
                    type_name='Imperial Shuttle', 
                    starship_class='Transport', 
                    manufacturer='Sienar Fleet Systems', 
                    model='Lambda-Class T-4a Shuttle', 
                    hyperdrive_rating=1.0, 
                    mglt=50, 
                    length=20,
                    crew=6, 
                    passenger=20, 
                    cargo=80000, 
                    consumables='2 months', 
                    cost_credits=240000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/22.jpg', 
                    unique=False,
    )
        
    shiptype_15 = Shiptype(    
                    type_name='EF76 Nebulon-9 Escort Frigate', 
                    starship_class='Star Cruiser', 
                    manufacturer='Kuat Drive Yards',
                    model='EF76 Nebulon-9 Escort Frigate', 
                    hyperdrive_rating=2.0, 
                    mglt=40, 
                    length=300,
                    crew=854, 
                    passenger=75, 
                    cargo=6000000, 
                    consumables='2 years', 
                    cost_credits=8500000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/23.jpg', 
                    unique=False,
    )
        
    shiptype_16 = Shiptype(    
                    type_name='Calamari Cruiser', 
                    starship_class='Star Cruiser', 
                    manufacturer='Mon Calamari Shipyards', 
                    model='MC80 Liberty Type Star Cruiser', 
                    hyperdrive_rating=1.0, 
                    mglt=60, 
                    length=1200,
                    crew=5400, 
                    passenger=1200, 
                    cargo=3000000, 
                    consumables='2 years', 
                    cost_credits=104000000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/27.jpg', 
                    unique=False,
    )
        
    shiptype_17= Shiptype(   
                    type_name='A-wing', 
                    starship_class='Starfighter', 
                    manufacturer='Alliance Underground Engineering', 
                    model='RZ-I A-wing Interceptor', 
                    hyperdrive_rating=1.0, 
                    mglt=120, 
                    length=10,
                    crew=1, 
                    passenger=0, 
                    cargo=40, 
                    consumables='1 week', 
                    cost_credits=175000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/28.jpg', 
                    unique=False,
    )
       
    shiptype_18 = Shiptype(   
                    type_name='B-wing', 
                    starship_class='Starfighter', 
                    manufacturer='Slayn & Korpil', 
                    model='A/SF-01 B-wing Starfighter', 
                    hyperdrive_rating=2.0, 
                    mglt=91, 
                    length=17,
                    crew=1, 
                    passenger=0, 
                    cargo=45, 
                    consumables='1 week', 
                    cost_credits=220000, 
                    ship_image='https: // starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/29.jpg', 
                    unique=False,
    )
        
    shiptype_19 = Shiptype(
                    type_name='U-wing', 
                    starship_class='Starfighter', 
                    manufacturer='Incom Corporation', 
                    model='UT-60D U-wing Starfighter', 
                    hyperdrive_rating=1.0, 
                    mglt=95, 
                    length=24,
                    crew=2, 
                    passenger=8, 
                    cargo=25000, 
                    consumables='2 weeks', 
                    cost_credits=130000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/30.jpg', 
                    unique=False,
    )
       
    shiptype_20 = Shiptype(   
                    type_name='Republic Frigate', 
                    starship_class='Star Cruiser', 
                    manufacturer='Corellian Engineering Corporation', 
                    model='Consular-Class Cruiser', 
                    hyperdrive_rating=2.0, 
                    mglt=60, 
                    length=115,
                    crew=9, 
                    passenger=16, 
                    cargo=120000, 
                    consumables='3 months', 
                    cost_credits=850000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/31.jpg', 
                    unique=False,
    )
        
    shiptype_21 = Shiptype(
                    type_name='Imperial Zeta-Class Cargo Shuttle', 
                    starship_class='Freighter', 
                    manufacturer='Sienar Fleet Systems', 
                    model='Zeta-Class Cargo Shuttle', 
                    hyperdrive_rating=2.0, 
                    mglt=60, 
                    length=35,
                    crew=2, 
                    passenger=20, 
                    cargo=450000, 
                    consumables='2 weeks', 
                    cost_credits=195000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/33.jpg', 
                    unique=False,
    )
        
    shiptype_22 = Shiptype(    
                    type_name='Naboo Fighter', 
                    starship_class='Starfighter', 
                    manufacturer='Theed Palace Space Vessel Engineering Corps.', 
                    model='N-1 Starfighter', 
                    hyperdrive_rating=1.0, 
                    mglt=90, 
                    length=11,
                    crew=1, 
                    passenger=0, 
                    cargo=65, 
                    consumables='1 week', 
                    cost_credits=200000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/39.jpg', 
                    unique=False,
    )
        
    shiptype_23 = Shiptype(    
                    type_name='Naboo Royal Starship', 
                    starship_class='Transport', 
                    manufacturer='Theed palace Space Vessel Engineering Corps.', 
                    model='J-type 327 Nubian Royal Starship', 
                    hyperdrive_rating=1.8, 
                    mglt=95, 
                    length=76,
                    crew=8, 
                    passenger=20, 
                    cargo=30000, 
                    consumables='1 month', 
                    cost_credits=535000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/40.jpg', 
                    unique=False,
    )
        
    shiptype_24 = Shiptype(    
                    type_name='Scimitar', 
                    starship_class='Transport', 
                    manufacturer='Sienar Fleet Systems', 
                    model='Star Courier', 
                    hyperdrive_rating=1.5, 
                    mglt=75, 
                    length=27,
                    crew=1, 
                    passenger=6, 
                    cargo=250000, 
                    consumables='1 month', 
                    cost_credits=5500000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/41.jpg', 
                    unique=False,
    )
        
    shiptype_25 = Shiptype(    
                    type_name='J-Type Diplomatic Shuttle', 
                    starship_class='Transport', 
                    manufacturer='Theed palace Space Vessel Engineering Corps.', 
                    model='J-Type Diplomatic Shuttle', 
                    hyperdrive_rating=0.7, 
                    mglt=50, 
                    length=39,
                    crew=5, 
                    passenger=10, 
                    cargo=175000, 
                    consumables='1 year', 
                    cost_credits=2000000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/43.jpg', 
                    unique=False,
    )
        
    shiptype_26 = Shiptype(    
                    type_name='AA-9 Coruscant Freighter', 
                    starship_class='Freighter', 
                    manufacturer='Botajef Shipyards', 
                    model='Botajef AA-9 Freighter-Liner', 
                    hyperdrive_rating=0.5, 
                    mglt=50, 
                    length=390,
                    crew=15, 
                    passenger=30000, 
                    cargo=750000, 
                    consumables='3 months',
                    cost_credits=825700, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/47.jpg', 
                    unique=False,
    )
       
    shiptype_27 = Shiptype(   
                    type_name='Jedi Starfighter', 
                    starship_class='Starfighter', 
                    manufacturer='Kuat Systems Engineering', 
                    model='Delta-7 Aethersprite-class Interceptor', 
                    hyperdrive_rating=1.0, 
                    mglt=95, 
                    length=8,
                    crew=1, 
                    passenger=0, 
                    cargo=60, 
                    consumables='1 week', 
                    cost_credits=180000, 
                    ship_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/48.jpg', 
                    unique=False
    )

    all_shiptypes = [ shiptype_1, shiptype_2, shiptype_3, shiptype_4, shiptype_5, shiptype_6,
                    shiptype_7, shiptype_8, shiptype_9, shiptype_10, shiptype_11, shiptype_12,
                    shiptype_13, shiptype_14, shiptype_15, shiptype_16, shiptype_17, shiptype_18,
                    shiptype_19, shiptype_20, shiptype_21, shiptype_22, shiptype_23, shiptype_24,
                    shiptype_25, shiptype_26, shiptype_27 ]
    
    _ = [db.session.add(shiptype) for shiptype in all_shiptypes]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_shiptypes():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.shiptypes RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM shiptypes"))
        
    db.session.commit()