# --CONFIG--    import and initialization
import sys
from sqlalchemy import Column, ForeignKey, Integer, String  # helpers for sql builder mapper
from sqlalchemy.ext.declarative import declarative_base  # use in configuration and class
from sqlalchemy.orm import relationship  # foreign key relationships for mapper
from sqlalchemy import create_engine  # use at end of conf
Base = declarative_base()  # declarative base class


# --CLASSES--   extended from Base class for ORM features
# class/table restaurant
class Restaurant(Base):
    # set table name
    __tablename__ = 'restaurant'
    # --columns--
    # pk
    id = Column(
        Integer,
        primary_key=True
    )
    # restaurant name, varchar80, not null
    name = Column(
        String(80),
        nullable=False
    )

    @property
    def serialize(self):
        # returns json
        return {
            'id': self.id,
            'name': self.name
        }

# class/table menu item
class MenuItem(Base):
    # set table name
    __tablename__ = 'menu_item'
    # --columns--
    # pk
    id = Column(
        Integer,
        primary_key=True
    )
    # menu item name, varchar80, not null
    name = Column(
        String(80),
        nullable=False
    )
    # course, menu item type
    course = Column(
        String(250)
    )
    # description, menu item desc
    description = Column(
        String(250)
    )
    # item price
    price = Column(
        String(8)
    )
    # restaurant id, belongs to
    restaurant_id = Column(
        Integer,  # validator integer
        ForeignKey('restaurant.id')  # id column of restaurant table
    )
    # relationship
    restaurant = relationship(Restaurant)  # set relationship to Restaurant class

    @property
    def serialize(self):
        # returns json
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'course': self.course
        }


# --ENGINE--    insert at end of file
engine = create_engine('sqlite:///restaurantmenu.db')  # specify database engine
# Base.metadata.bind = engine  # bind database engine to Base's metadata
Base.metadata.create_all(engine)  # create classes as tables in database

# cmd session
# DBSession = sessionmaker(bind=engine)  # make a DB session with binding to the above db engine
# session = DBSession()  # init a session instance
# newEntry = ClassName(property="value",...)  # prepare an object
##!! restaurantRamenRyoma = Restaurant(name="Ramen Ryoma")
# session.add(newEntry)  # "insert" the object
##!! session.add(restaurantRamenRyoma)
##!! session.commit()  # execute the queries to db
# session.query(Restaurant).all()  # query all Restaurant, return <list>
# firstRestaurant = session.query(Restaurant).first()  # the first result querying all restaurant, return object
# firstRestaurant.name  # print property
# http://docs.sqlalchemy.org/en/rel_0_9/orm/query.html  #query docs
##!! veggie = session.query(MenuItem).filter_by(name = 'Veggie Burger')  # query with filter
# for v in veggie:
#     print v.id
#     print v.price
#     print v.restaurant.name  #  relationship.name
# urban = session.query(MenuItem).filter_by(id=8).one()  # get filtered query, only get one, not a list
##!! urban.price = '$2.99'  # update attribute
# session.add(urban)  # add updated object
# session.commit()  # commit after added updated object
# for loop all items, update each item, commit
##!! delete : query - session.delete(objectToBeDeleted) - commit
# query for deleted - return 'No row found'


