from app.models import db, environment, SCHEMA, Species
from sqlalchemy.sql import text

# Adds a demo user, you can add other users here if you want
def seed_species():
    species_1 = Species(species_type='Human')
    species_2 = Species(species_type='Driod')
    species_3 = Species(species_type='Wookie')
    species_4 = Species(species_type='Rodian')
    species_5 = Species(species_type='Hutt')
    species_6 = Species(species_type="Yoda's Species")
    species_7 = Species(species_type='Trandoshan')
    species_8 = Species(species_type='Mon Calamari')
    species_9 = Species(species_type='Ewok')
    species_10 = Species(species_type='Sullustan')
    species_11 = Species(species_type='Neimodian')
    species_12 = Species(species_type='Gungan')
    species_13 = Species(species_type='Toydarian')
    species_14 = Species(species_type='Dug')
    species_15 = Species(species_type="Twi'lek")
    species_16 = Species(species_type='Aleena')
    species_17 = Species(species_type='Vulptereen')
    species_18 = Species(species_type='Xexto')
    species_19 = Species(species_type='Toong')
    species_20 = Species(species_type='Cerean')
    species_21 = Species(species_type='Nautolan')
    species_22 = Species(species_type='Zabrak')
    species_23 = Species(species_type='Tholothian')
    species_24 = Species(species_type='Iktotchi')
    species_25 = Species(species_type='Quermian')
    species_26 = Species(species_type='Kel Dor')
    species_27 = Species(species_type='Chagrian')
    species_28 = Species(species_type='Geonosian')
    species_29 = Species(species_type='Mirialan')
    species_30 = Species(species_type='Clawdite')
    species_31 = Species(species_type='Besalisk')
    species_32 = Species(species_type='Kaminoan')
    species_33 = Species(species_type='Skakoan')
    species_34 = Species(species_type='Muun')
    species_35 = Species(species_type='Togruta')
    species_36 = Species(species_type='Kaleesh')
    species_37 = Species(species_type="Pau'an")
    
    all_species = [species_1, species_2, species_3, species_4, species_5,
                    species_6, species_7, species_8, species_9, species_10,
                    species_11, species_12, species_13, species_14, species_15,
                    species_16, species_17, species_18, species_19, species_20,
                    species_21, species_22, species_23, species_24, species_25,  
                    species_26, species_27, species_28, species_29, species_30,
                    species_31, species_32, species_33, species_34, species_35,
                    species_36, species_37]
    _ = [db.session.add(specie) for specie in all_species]
    db.session.commit()
    


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_species():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.species RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM species"))
        
    db.session.commit()