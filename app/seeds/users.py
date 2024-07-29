from app.models import db, User, environment, SCHEMA
from werkzeug.security import generate_password_hash

# Adds a demo user, you can add other users here if you want
def seed_users():
    user_1 = User(
                name='Luke Skywalker', 
                email='lukeskywalker@aol.com', 
                hashed_password=generate_password_hash('force1'), 
                species=1, 
                bio='Luke Skywalker was a Tatooine farm boy who rose from humble beginnings to become one of the greatest Jedi the galaxy has ever known.',
                faction=True, 
                credits= 1000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/01.jpg', 
                force_points=0, 
    )
    
    user_2 = User(
                name='C-3PO', 
                email='goldguy@gmail.com', 
                hashed_password=generate_password_hash('masterluke'), 
                species=2, 
                bio='C-3PO longs for more peaceful times, but his continued service to the Resistance — and his knowledge of more than seven million forms of communication — keeps the worry-prone droid in the frontlines of galactic conflict.',
                faction=True, 
                credits=1000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/02.jpg', 
                force_points=0,
    )
    
    user_3 = User(
                name='R2-D2', 
                email='droid1@R2D2.net', 
                hashed_password=generate_password_hash('xwingsrule4'), 
                species=2, 
                bio='A reliable and versatile astromech droid, R2-D2 has served Padmé Amidala, Anakin Skywalker, and Luke Skywalker in turn, showing great bravery in rescuing his masters and their friends from many perils',
                faction=True, 
                credits=1000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/03.jpg', 
                force_points=0,
    )
          
    user_4 = User (
                name='Darth Vader', 
                email='darkside4life@hotmail.com', 
                hashed_password=generate_password_hash('iamyourfather'), 
                species=1, 
                bio='Once a heroic Jedi Knight, Darth Vader was seduced by the dark side of the Force, became a Sith Lord, and led the Empire’s eradication of the Jedi Order. But there was still good in him…',
                faction=False, 
                credits=1500000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/04.jpg', 
                force_points=0,
    )
          
    user_5 = User(
                name='Leia Organa', 
                email='goldenbikini@mac.com', 
                hashed_password=generate_password_hash('ewoksarecute'), 
                species=1, 
                bio='Princess Leia Organa was one of the greatest leaders of the Rebel Alliance, fearless on the battlefield and dedicated to ending the Empire’s tyranny. Daughter of Padmé Amidala and Anakin Skywalker, sister of Luke Skywalker, and with a soft spot for scoundrels, Leia ranked among the galaxy’s great heroes.',
                faction=False, 
                credits=3000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/05.jpg', 
                force_points=0,
    )
          
    user_6 = User(      
                name='Owen Lars', 
                email='larsevaporators@tatooine.org', 
                hashed_password=generate_password_hash('evaporators'), 
                species=1, 
                bio="Owen Lars continued his father Cliegg’s efforts to build his homestead into a productive farm, working alongside his wife, Beru. Helping with the dreary chores required to keep the farm profitable, Owen relied on his nephew Luke Skywalker. He could not rein in Luke's drive for adventure, though.",
                faction=True, 
                credits=50000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/06.jpg', 
                force_points=0,
    )
          
    user_7 = User(      
                name='Beru Whitesun Lars', 
                email='auntberu@optimium.net', 
                hashed_password=generate_password_hash('larssmells'), 
                species=1, 
                bio="As a young, shy girl, Beru Whitesun's aspirations did not reach beyond Tatooine. She was content to marry Owen Lars and lead the tough life of a moisture farmer.",
                faction=True, 
                credits=25000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/07.jpg', 
                force_points=0,
    )
          
    user_8 = User(
                name='R5-D4', 
                email='wishiwasr2d2@R2D2.net', 
                hashed_password=generate_password_hash('notr2d2'), 
                species=2, 
                bio="A red astromech droid, R5-D4 thought he'd found a home when the Jawas sold him to Owen Lars, along with the protocol droid C-3PO. But R5's motivator blew as he rolled away from the sandcrawler, forcing the Jawas to take him back in exchange for R2-D2.",
                faction=True, 
                credits=15000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/08.jpg', 
                force_points=0,
    )
          
    user_9 = User(
                name='Biggs Darklighter', 
                email='biggs@rebels.com', 
                hashed_password=generate_password_hash('imbiggs'), 
                species=1, 
                bio="Biggs Darklighter grew up on Tatooine with Luke Skywalker, and shared his friend's dreams of escaping the dull desert world. After graduating from the Imperial Academy, he defected from the Empire's service to join the Rebellion.",
                faction=True, 
                credits=34560, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/09.jpg', 
                force_points=0,
    )
         
    user_10 = User(
                name='Obi-Wan Kenobi', 
                email='force2@force.net', 
                hashed_password=generate_password_hash('usetheforceluke'), 
                species=1, 
                bio="A legendary Jedi Master, Obi-Wan Kenobi was a noble man and gifted in the ways of the Force. He trained Anakin Skywalker, served as a general in the Republic Army during the Clone Wars, and guided Luke Skywalker as a mentor.",
                faction=True, 
                credits=1000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/10.jpg', 
                force_points=0,
    )
          
    user_11 = User(      
                name='Anakin Skywalker', 
                email='anny1@jediturnedsith.org', 
                hashed_password=generate_password_hash('imreallyvader'), 
                species=1, 
                bio="Discovered as a slave on Tatooine by Qui-Gon Jinn and Obi-Wan Kenobi, Anakin Skywalker had the potential to become one of the most powerful Jedi ever, and was believed by some to be the prophesied Chosen One who would bring balance to the Force.",
                faction=True, 
                credits=65000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/11.jpg', 
                force_points=0,
    )
          
    user_12 = User(      
                name='Wilhuff Tarkin', 
                email='moftarkin@empirerulez.com', 
                hashed_password=generate_password_hash('deathstar1'), 
                species=1, 
                bio="An ambitious, ruthless proponent of military power, Wilhuff Tarkin became a favorite of Supreme Chancellor Palpatine and rose rapidly through the Imperial ranks. Shortly after the Empire's creation, he was put in charge of the construction of the Death Star.",
                faction=False, 
                credits=2000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/12.jpg', 
                force_points=0,
    )
          
    user_13 = User(      
                name='Chewbacca', 
                email='chewie@falcon.com', 
                hashed_password=generate_password_hash('wookie1'), 
                species=3, 
                bio="A legendary Wookiee warrior and Han Solo’s longtime co-pilot, Chewbacca continues to serve as faithful first mate to carry out daring missions against the First Order behind the controls of the Millennium Falcon. Known as Chewie to his closest friends, he was part of a core group of rebels who restored freedom to the galaxy during the reign of the Galactic Empire. ",
                faction=True, 
                credits=500000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/13.jpg', 
                force_points=0,
    )

    user_14 = User(
                name='Han Solo', 
                email='solo1@falcon.com', 
                hashed_password=generate_password_hash('12parsecs'), 
                species=1, 
                bio="Han Solo rose from an impoverished childhood on the mean streets of Corellia to become one of the heroes of the Rebel Alliance. As captain of the Millennium Falcon, Han and his co-pilot Chewbacca came to believe in the cause of galactic freedom, joining Luke Skywalker and Princess Leia Organa in the fight against the Empire.",
                faction=True, 
                credits=25000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/14.jpg', 
                force_points=0,
    )
         
    user_15 = User(
                name='Greedo', 
                email='greedo@bountyhunters.org', 
                hashed_password=generate_password_hash('hanshotme'), 
                species=4, 
                bio="Greedo was a Rodian bounty hunter with a tapir-like snout, bulbous eyes, pea-green skin, and a crest of spines atop his skull. He was overzealous and a bit slow on the take, not to mention a pretty poor shot with a blaster. ",
                faction=False, 
                credits=125000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/15.jpg', 
                force_points= 0,
    )
         
    user_16 = User(
                name='Jabba Desilijic Tiure', 
                email='jabba@hutt.net', 
                hashed_password=generate_password_hash('iwillgetyousolo'),
                species=5, 
                bio="Jabba the Hutt was one of the galaxy’s most powerful gangsters, with far-reaching influence in both politics and the criminal underworld.",
                faction=False, 
                credits=7500000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/16.jpg', 
                force_points=0,
    )
          
    user_17 = User(      
                name='Darth Maul', 
                email='darthmaul@jediturnedsith.org', 
                hashed_password=generate_password_hash('jediscum'), 
                species=23, 
                bio="A deadly, agile Sith Lord trained by the evil Darth Sidious, Darth Maul was a formidable warrior and scheming mastermind. He wielded an intimidating double-bladed lightsaber and fought with a menacing ferocity. ",
                faction=False, 
                credits=143000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/17.jpg', 
                force_points=0,
    )
          
    user_18 = User(      
                name='Wedge Antilles', 
                email='wedge2@rebels.com', 
                hashed_password=generate_password_hash('wedgethis'), 
                species=1, 
                bio="A talented young rebel pilot from Corellia, Wedge Antilles survived the attack on the first Death Star to become a respected veteran of Rogue Squadron.",
                faction=True, 
                credits=132500, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/18.jpg', 
                force_points=0,
    )
          
    user_19 = User(      
                name='Jek Tono Porkins', 
                email='jek@rebels.com', 
                hashed_password=generate_password_hash('vaderkilledme'), 
                species=1, 
                bio="Jek Tono Porkins, nicknamed 'Piggy', was a male human trader and pilot from Bestine IV. He decided to abandon his homeworld after the Galactic Empire moved in and built a new military base there, and he ended up joining the Alliance to Restore the Republic.",
                faction=True, 
                credits=5000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/19.jpg', 
                force_points=0,
    )
          
    user_20 = User(      
                nam='Yoda', 
                email='yoda@force.net', 
                hashed_password=generate_password_hash('thereisnotry'), 
                species=6, 
                bio="Yoda was a legendary Jedi Master and stronger than most in his connection with the Force. Small in size but wise and powerful, he trained Jedi for over 800 years, playing integral roles in the Clone Wars, the instruction of Luke Skywalker, and unlocking the path to immortality.",
                faction=True, 
                credits=10000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/20.jpg', 
                force_points=0,
    )
          
    user_21 = User(      
                name='Palpatine', 
                email='emperor@jediturnedsith.org', 
                hashed_password=generate_password_hash('darkside'), 
                species=1, 
                bio="The dark side of the Force is a pathway to many abilities some consider to be unnatural, and Sheev Palpatine is the most infamous follower of its doctrines. Scheming, powerful, and evil to the core, Darth Sidious restored the Sith and destroyed the Jedi Order. Living a double life, he was also Palpatine, a Naboo Senator and phantom menace",
                faction=False, 
                credits=1000000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/21.jpg', 
                force_points=0,
    )
          
    user_22 = User(      
                name='Boba Fett', 
                email='bfett@bountyhunters.org', 
                hashed_password=generate_password_hash('password'), 
                species=1, 
                bio="With his customized Mandalorian armor, deadly weaponry, and silent demeanor, Boba Fett was one of the most feared bounty hunters in the galaxy. A genetic clone of his “father,” bounty hunter Jango Fett, Boba learned combat and martial skills from a young age.",
                faction=False, 
                credits=750000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/22.jpg', 
                force_points=0,
    )
          
    user_23 = User(      
                name='IG-88', 
                email='IG@R2D2.net', 
                hashed_password=generate_password_hash('imdroid'), 
                species=2, 
                bio="IG-88 is a battered chrome war droid who has become a bounty hunter, and answered Darth Vader's call to capture the Millennium Falcon during the events surrounding the Battle of Hoth.",
                faction=False, 
                credits=50000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/23.jpg', 
                force_points=0,
    )
          
    user_24 = User(      
                name='Bossk', 
                email='bossk@bountyhunters.org', 
                hashed_password=generate_password_hash('bossk1'), 
                species=7, 
                bio="One of the most feared bounty hunters of the galaxy, Bossk used his natural Trandoshan hunting instincts to capture his prey. During the Clone Wars, the red-eyed reptilian partnered with Aurra Sing, Castas and young Boba Fett. Bossk didn't care much for vendettas or politics. He was in it to get paid. After a brief stint in a Republic prison, Bossk continued his partnership with Fett, becoming a bodyguard to the teen bounty hunter.",
                faction=False, 
                credits=500000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/24.jpg', 
                force_points=0,
    )
          
    user_25 = User(
                name='Lando Calrissian', 
                email='lando@falcon.com', 
                hashed_password=generate_password_hash('cloudcity'), 
                species=1, 
                bio="Lando Calrissian may have come late to the fight against the Empire, but his role in destroying the second Death Star cemented his reputation as a hero. After he lost his beloved ship to Han Solo, Lando spent years living the high life and pursuing get-rich-quick schemes, with uneven results. He went semi-respectable as the baron administrator of Cloud City, only to be drawn into the fight against the Empire. ",
                faction=True, 
                credits=3000000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/25.jpg', 
                force_points=0,
    )

    user_26 = User(
                name='Lobot',
                email='lobot@cloudcity.com', 
                hashed_password=generate_password_hash('lobot'), 
                species=2, 
                bio="Never far from Baron Administrator Lando Calrissian's side was Lobot, Calrissian's aide and Cloud City's computer liaison officer. Lobot is a human male with a shiny, brain-enhancing device wrapped around the back of his skull that allowed him to contact directly with the city's central computer.",
                faction=True, 
                credits=25000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/26.jpg', 
                force_points=0,
    )
          
    user_27 = User(      
                name='Admiral Ackbar', 
                email='ackie@rebels.com', 
                hashed_password=generate_password_hash('itsatrap'), 
                species=8, 
                bio="A veteran commander, Ackbar led the defense of his homeworld, Mon Cala, during the Clone Wars and then masterminded the rebel attack on the second Death Star at the Battle of Endor. Ackbar realized the rebels had been drawn into a trap at Endor, but adjusted, with his fleet buying valuable time for the attack to succeed. ",
                faction=True, 
                credits=500000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/27.jpg', 
                force_points=0,
    )
          
    user_28 = User(
                name='Mon Mothma', 
                email='mon@rebels.com', 
                hashed_password=generate_password_hash('mothma'), 
                species=1, 
                bio="A leader of the Galactic Senate's Loyalist faction, Mon Mothma opposed Supreme Chancellor Palpatine's policies during the final days of the Republic. Working in secret, she helped found the Rebel Alliance, and served as its civilian leader during the long struggle against the Empire.",
                faction=True, 
                credits=250000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/28.jpg', 
                force_points=0,
    )

    user_29= User(     
                name='Arvel Crynyd', 
                email='crynyd@rebels.com', 
                hashed_password=generate_password_hash('nooneknowsme'), 
                species=1, 
                bio="Arvel Crynyd was a male human pilot who served in the Alliance to Restore the Republic during the Galactic Civil War. In the war's fourth year, Commander Crynyd participated in the Rebellion's attack on the Galactic Empire's second Death Star in the Battle of Endor, flying an RZ-1 A-wing interceptor in Green Squadron as leader of the squadron",
                faction=True, 
                credits=120000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/29.jpg', 
                force_points=0,
    )

    user_30 = User(
                name='Wicket Systri Warrick', 
                email='wicket@emok.org', 
                hashed_password=generate_password_hash('lublub'), 
                species=9, 
                bio="Wicket W. Warrick was the brave young Ewok who willingly joined the Rebellion and aided in the battle against the Empire on the forest moon of Endor. Even before he encountered the Rebels, Wicket had devised methods for defeating the Imperial machines, plans which were implemented after the Ewok befriended Princess Leia and recruited his tribe to the Alliance's cause.",
                faction=True, 
                credits=50000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/30.jpg', 
                force_points=0,
    )
         
    user_31 = User(
                name='Nien Nunb', 
                email='nunb@rebels.com', 
                hashed_password=generate_password_hash('nubnub'), 
                species=10, 
                bio="A native of Sullust, Nien Nunb was a smuggler who fought for both the Rebel Alliance and the Resistance during his long career. An expert pilot, he served as Lando Calrissian’s co-pilot aboard the Millennium Falcon during the Battle of Endor, flew an X-wing in the raid on Starkiller Base and survived the First Order’s assault on Crait.",
                faction=True, 
                credits=152000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/31.jpg', 
                force_points=0,
    )
    
    user_31 = User(
                name='Qui-Gon Jinn', 
                email='quigon@force.net', 
                hashed_password=generate_password_hash('jedi4life'), 
                species=1, 
                bio="A venerable if maverick Jedi Master, Qui-Gon Jinn was a student of the living Force. Qui-Gon lived for the moment, espousing a philosophy of 'feel, don't think -- use your instincts.' On Tatooine, Qui-Gon discovered a young slave boy named Anakin Skywalker who was strong in the Force. Sensing the boy's potential, Qui-Gon liberated Anakin from slavery.",
                faction=True, 
                credits=555000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/32.jpg', 
                force_points=0,
    )
    
    user_32 = User(
                name='Watto', 
                email='watto@ibuyjunk.org', 
                hashed_password=generate_password_hash('nubian'), 
                species=13, 
                bio="Watto was a Toydarian junk dealer in Mos Espa who bought Shmi Skywalker and her son Anakin from Gardulla the Hutt. An inveterate gambler, he sponsored Anakin in several Podraces, but often bet against his own slave, who was talented but inexperienced.",
                faction=True, 
                credits=237000, 
                user_image='https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/40.jpg', 
                force_points=0,
    )
          
    all_users = [user_1, user_2, user_, user_4, user_5, user_6, user_7, user_8, user_9, user_10,
                 user_11, user_12, user_13, user_14, user_15, user_16, user_17,user_18, user_19.
                 user_20, user_21, user_22, user_23, user_24,user_25, user_26, user_27, user_28,
                 user_29, user_30, user_31, user_32 ]

    _ = [db.session.add(user) for user in all_users]
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()