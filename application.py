from flask import Flask, url_for, render_template, redirect
app = Flask(__name__)

from sqlalchemy import create_engine, asc, desc
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
    items = session.query(CatalogItem).order_by(desc(CatalogItem.created_date)).limit(10)
    return render_template('catalog.html', categories=categories, items=items)

@app.route('/catalog/<string:category_name>')
def showCategory(category_name):
    return "Category page"

@app.route('/catalog/<string:category_name>/<int:catalog_item_id>')
def showItem(category_name, catalog_item_id):
    return "Item page"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
