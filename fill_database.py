from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, CatalogItem

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy data
category = Category(name = "Living Room")
session.add(category)
session.commit()

item1 = CatalogItem(name="Sofa", description="A piece of furniture for seating"
                    "three or more people in the form of a bench", category=category)
session.add(item1)
session.commit()

item2 = CatalogItem(name="Coffee Table", description="A style of long, low table which is designed to be placed in front of a sofa",
                    category=category)
session.add(item2)
session.commit()

category = Category(name = "Dining Room")
session.add(category)
session.commit()

category = Category(name = "Kitchen")
session.add(category)
session.commit()

category = Category(name = "Bedroom")
session.add(category)
session.commit()

category = Category(name = "Bathroom")
session.add(category)
session.commit()

print "Added catalog items!"
