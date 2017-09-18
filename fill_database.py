from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, CatalogItem, User

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy User
user = User(name="Some Guy", email="someguy@someguy.com")
session.add(user)
session.commit()

# Create dummy data
# All descriptions are from https://en.wikipedia.org
category = Category(name = "Living Room")
session.add(category)
session.commit()

item1 = CatalogItem(user_id=1, name="Sofa", description="A piece of furniture for seating"
                    "three or more people in the form of a bench.", category=category)
session.add(item1)
session.commit()

item2 = CatalogItem(user_id=1, name="Coffee Table", description="A style of long, low table which is designed to be placed in front of a sofa.",
                    category=category)
session.add(item2)
session.commit()

category = Category(name = "Dining Room")
session.add(category)
session.commit()

item1 = CatalogItem(user_id=1, name="Dining Table", description="A table designed to be used for formal dining.", category=category)
session.add(item1)
session.commit()

category = Category(name = "Kitchen")
session.add(category)
session.commit()

item1 = CatalogItem(user_id=1, name="Trash Compactor", description="A machine often used to reduce the amount of trash in a home.", category=category)
session.add(item1)
session.commit()

item2 = CatalogItem(user_id=1, name="Dishwasher", description="A mechanical device for cleaning dishware and cutlery.",
                    category=category)
session.add(item2)
session.commit()

category = Category(name = "Bedroom")
session.add(category)
session.commit()

item1 = CatalogItem(user_id=1, name="Bed", description="A piece of furniture that is used as a place to sleep or relax.", category=category)
session.add(item1)
session.commit()

category = Category(name = "Bathroom")
session.add(category)
session.commit()

item1 = CatalogItem(user_id=1, name="Sink", description="A bowl-shaped fixture used for washing hands, dishwashing, and other purposes.",
                    category=category)
session.add(item1)
session.commit()

category = Category(name = "Office")
session.add(category)
session.commit()

item1 = CatalogItem(user_id=1, name="Desk", description="A piece of furniture with a flat table-style work surface.",
                    category=category)
session.add(item1)
session.commit()

print "Added catalog items!"
