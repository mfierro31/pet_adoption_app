from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# Make pets

roger = Pet(name='Roger', species='Rabbit', photo_url='https://vignette.wikia.nocookie.net/disney/images/c/cf/Profile_-_Roger_Rabbit.png/revision/latest?cb=20190312161439', age=20, notes='Gets into a lot of trouble, but very loving.')
petey = Pet(name='Petey', species='Tiger', photo_url='https://petpress.net/wp-content/uploads/2020/01/tiger-names.jpg', notes="Only adopt if you know what you're doing.  Tigers are dangerous!")
larry = Pet(name='Larry', species='Lion', photo_url='https://ichef.bbci.co.uk/news/1024/cpsprodpb/E0F0/production/_112548575_gettyimages-492611032-1.jpg', age=15, notes="Only adopt if you know what you're doing.  Lions are dangerous!")
rocket = Pet(name='Rocket', species='Raccoon', photo_url='https://cdn.vox-cdn.com/thumbor/Kcurk6tQuIS-Ssrqfu-n1D2R3Ug=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/18796252/b660a31607.jpg', notes='Talks.  Sassy.')
duke = Pet(name='Duke', species='Dog', photo_url='https://live.staticflickr.com/301/19233205218_b6ce57632f_b.jpg', age=2, notes='Already taken.  Sorry!', available=False)
bitey = Pet(name='Mr. Bitey', species='Cat', photo_url='https://pbs.twimg.com/profile_images/1214332182141034502/tdRhBSW7_400x400.jpg', notes='Bites a lot.')
davy = Pet(name='Davy Jones', species='Octopus')

db.session.add_all([roger, petey, larry, rocket, duke, bitey, davy])
db.session.commit()