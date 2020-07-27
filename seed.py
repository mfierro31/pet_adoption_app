from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# Make pets

roger = Pet(name='Roger', species='Porcupine', photo_url='https://cincinnatizoo.org/system/assets/uploads/2019/08/47014743964_301007edc0_b-1024x683.jpg', age=20, notes='Gets into a lot of trouble, but very loving.')
petey = Pet(name='Petey', species='Porcupine', photo_url='https://www.zoomontana.org/images/img_7oG4iZhLWRyAxceYYZHoMe/north-american-porcupine.jpg?fit=outside&w=1600')
larry = Pet(name='Larry', species='Cat', photo_url='https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2018/08/kitten-440379.jpg?h=c8d00152&itok=1fdekAh2', age=1, notes="Gets scared easily.  Needs a patient owner.")
rocket = Pet(name='Rocket', species='Dog', photo_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*', notes='A very good boy.')
duke = Pet(name='Duke', species='Dog', photo_url='https://live.staticflickr.com/301/19233205218_b6ce57632f_b.jpg', age=2, notes='Already taken.  Sorry!', available=False)
bitey = Pet(name='Mr. Bitey', species='Cat', photo_url='https://pbs.twimg.com/profile_images/1214332182141034502/tdRhBSW7_400x400.jpg', notes='Bites a lot.')
davy = Pet(name='Davy', species='Dog')

db.session.add_all([roger, petey, larry, rocket, duke, bitey, davy])
db.session.commit()