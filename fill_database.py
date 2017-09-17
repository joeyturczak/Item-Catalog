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
