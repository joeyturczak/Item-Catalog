from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, CatalogItem

# Connect to database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Show main catalog page
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('catalog.html', categories=categories)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
