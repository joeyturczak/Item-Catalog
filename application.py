from flask import Flask, url_for, render_template, redirect, request
app = Flask(__name__)

from sqlalchemy import create_engine, asc, desc, and_
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
    list_title = "Latest Items"
    return render_template('catalog.html', categories=categories, items=items, list_title=list_title)

@app.route('/catalog/<string:category_name>')
def showCategory(category_name):
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(CatalogItem).filter_by(category_name=category_name).order_by(asc(CatalogItem.name))
    list_title = "%s Items" % category_name
    return render_template('catalog.html', categories=categories, items=items, list_title=list_title)

@app.route('/catalog/<string:category_name>/<string:item_name>')
def showItem(category_name, item_name):
    item = session.query(CatalogItem).filter(and_(CatalogItem.name==item_name, CatalogItem.category_name==category_name)).one()
    return render_template('item.html', item=item)

@app.route('/catalog/new', methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        newItem = CatalogItem(name=request.form['name'], description=request.form['description'], category_name=request.form['category'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        categories = session.query(Category).order_by(asc(Category.name))
        return render_template('new_item.html', categories=categories)

@app.route('/catalog/<string:category_name>/<string:item_name>/edit', methods=['GET', 'POST'])
def editItem(category_name, item_name):
    itemToEdit = session.query(CatalogItem).filter(and_(CatalogItem.name==item_name, CatalogItem.category_name==category_name)).one()
    if request.method == 'POST':
        if request.form['name']:
            itemToEdit.name = request.form['name']
            itemToEdit.description = request.form['description']
            itemToEdit.category_name = request.form['category']
            session.add(itemToEdit)
            session.commit()
            return redirect(url_for('showCategory', category_name=category_name))
    else:
        categories = session.query(Category).order_by(asc(Category.name))
        return render_template('edit_item.html', item=itemToEdit, categories=categories)

@app.route('/catalog/<string:item_name>/edit', methods=['GET', 'POST'])
def deleteItem():
    return "Delete Item"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
