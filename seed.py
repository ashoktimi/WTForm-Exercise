from app import db
from models import Pet

db.drop_all()
db.create_all()


p1 = Pet(name="Woofly", species="Dog", photo_url = "https://dogtime.com/assets/uploads/2011/03/puppy-development.jpg", age=2.5, available =False)
p2 = Pet(name="Milo", species="Cat", photo_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg", age=1.5, available =True)
p3 = Pet(name="Tia", species="Bird")


db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()