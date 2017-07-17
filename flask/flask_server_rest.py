#!/usr/bin/env python3

# -IMPORTS- #

# flask
from flask import Flask  # flask micro framework
# redirect(url_for('function_name',[args]))
from flask import flash  # for flashing message
# app.secret_key = '<key>'
from flask import jsonify  # jsonofy things
from flask import redirect  # for easy redirection
from flask import render_template  # for rendering heml templates
# url_for('function_name',arg0, arg1...)
from flask import request  # for taking post form
from flask import url_for  # for generating elegant urls http://flask.pocoo.org/docs/0.12/blueprints/#building-urls

# template examples:    default dir = /templates/
"""
{% #logical code %}
{{ #printed code }}
    {% #endfor %}
    {% #endif %}
"""
# static files:     default dir = /static/
# JSON - JS object notation

from flask.flask_pg import get_posts, add_post

# sqlalchemy
from sqlalchemy import create_engine  # use at end of conf
from sqlalchemy.orm import sessionmaker
from sql.sql_alchemy_orm import Base, Restaurant, MenuItem  # basic Base class extended from delaritve_base()

# -INIT SQLALCHEMY- #
engine = create_engine('sqlite:///restaurantmenu.db')  # create sqlite db conf
Base.metadata.bind = engine  # bind engine to Base
DBSession = sessionmaker(bind=engine)  # create session binding engine
session = DBSession()  # create session handle

# -INIT FLASK- #
app = Flask(__name__)  # __name__ for application name assign when running, __main__ when running as main

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>DB Forum</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''
  <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
    """Main page of the forum."""
    posts = "".join(POST % (date, text) for text, date in get_posts())
    html = HTML_WRAP % posts
    return html


@app.route('/', methods=['POST'])
def post():
    """New post submission."""
    message = request.form['content']
    add_post(message)
    return redirect(url_for('main'))


# get restaurant by id
@app.route('/restaurant/<int:restaurant_id>/')  # default restaurant page
def restaurant_menu(restaurant_id):  # decorator function for above line @
    # get orms for restaurant and menu item
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html',  # templates/menu.html listing menu items of a restaurant
                           restaurant=restaurant,  # restaurant data
                           items=items)  # menu items data


@app.route('/restaurant/<int:restaurant_id>/menu/JSON')  # JSON menu for mobile
def restaurant_menu_json(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItem=[item.serialize for item in items])  # jsonify an orm looping through it


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')  # JSON menu for mobile
def restaurant_menu_item_json(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
    return jsonify(MenuItem=item.serialize)  # jsonify an orm looping through it


# post menu item by id
@app.route('/restaurant/<int:restaurant_id>/new', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':  # do post
        new_item = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)  # create new obj with form data
        session.add(new_item)
        session.commit()  # add and commit new item
        flash("new menu item %s created." % new_item.name)  # add flash message to message queue
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))  # redirect to listing after commit
    else:  # do get form
        return render_template('new_menu_item.html',
                               restaurant_id=restaurant_id,
                               restaurant=restaurant)  # for get form


# put menu item by id
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    # prepare orm
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    # do post
    if request.method == 'POST':
        if request.form['name']:  # existence check
            item.name = request.form['name']  # put
        session.add(item)  # add and commit
        session.commit()
        flash("menu item %s edited." % item.name)  # add flash message to message queue
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))  # redirect to listing
    # do get
    else:
        return render_template('edit_menu_item.html',
                               restaurant_id=restaurant_id,
                               restaurant=restaurant,
                               menu_id=menu_id,
                               item=item)


# delete menu item by id
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    # prepare orm
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    # do post
    if request.method == 'POST':
        session.delete(item)  # add and commit
        session.commit()
        flash("menu item %s deleted." % item.name)  # add flash message to message queue
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))  # redirect to listing
    # do get
    else:
        return render_template('delete_menu_item.html',
                               restaurant_id=restaurant_id,
                               restaurant=restaurant,
                               menu_id=menu_id,
                               item=item)


# -MAIN- #
if __name__ == '__main__':  # only do when running as main, not import
    app.secret_key = 'mykey'  # create session for user
    app.debug = True  # reload on file change
    # by default, only accessible from host
    app.run(host='0.0.0.0', port=5000)  # use 0.0.0.0 to listen to all public ip addresses
