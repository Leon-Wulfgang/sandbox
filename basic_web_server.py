#   BaseHTTPserver  https://docs.python.org/2/library/basehttpserver.html

# basic python http server lib
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  # if py3 import http.server

# common gateway interface lib
import cgi

# sqlalchemy orm
from sqlalchemy import create_engine  # for db engine
from sqlalchemy.orm import sessionmaker  # for sql sessions
from sql_alchemy_orm import Base, Restaurant, MenuItem  # basic Base class extended from delaritve_base() and example classes

# DB conf
engine = create_engine('sqlite:///restaurantmenu.db')  # create sqlite db conf
Base.metadata.bind = engine  # bind engine to Base
DBSession = sessionmaker(bind=engine)  # create session binding engine
session = DBSession()  # create session handle


# HANDLER   what code to send
class webserverHandler(BaseHTTPRequestHandler):  # the handler extend from base http handler
    def do_GET(self):  # for GET requests
        try:
            # /delete
            if self.path.endswith("/delete"):
                restaurantId = self.path.split("/")[2]  # get id from url
                myRestaurantORM = session.query(Restaurant).filter_by(id=restaurantId).one()  # get first restaurant by id
                if myRestaurantORM != []: # found at least one entry
                    # standard 200 ok
                    self.send_response(200)  # handler send code 200
                    self.send_header('Content-type', 'text/html')  # handler send header
                    self.end_headers()  # handler send a blank line to end headers section

                    # confirmation page
                    output = "<html><body>"
                    output += "<h1>Delete this ? %s</h1>" % myRestaurantORM.name
                    output += "<form " \
                              "method='POST' " \
                              "enctype='multipart/form-data' " \
                              "action='/restaurant/%s/delete'>" % restaurantId
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)  # write output content string to handler's wfile for response
                    return  # exit with normal

            # /edit
            if self.path.endswith("/edit"):
                restaurantId = self.path.split("/")[2]  # get id from url
                myRestaurantORM = session.query(Restaurant).filter_by(id=restaurantId).one()  # get first restaurant by id
                # found
                if myRestaurantORM != []: # found at least one entry
                    # standard 200 ok
                    self.send_response(200)  # handler send code 200
                    self.send_header('Content-type', 'text/html')  # handler send header
                    self.end_headers()  # handler send a blank line to end headers section
                    # build form
                    output = "<html><body>"
                    output += "<h1>%s</h1>" % myRestaurantORM.name
                    output += "<form " \
                              "method='POST' " \
                              "enctype='multipart/form-data' " \
                              "action='/restaurant/%s/edit'>" % restaurantId
                    output += "<input type='text' name='newRestaurantName' placeholder='%s'>" % myRestaurantORM.name
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)  # write output content string to handler's wfile for response
                    return  # exit with normal

            # /restaurant/new
            if self.path.endswith("/restaurant/new"):
                # standard 200 ok
                self.send_response(200)  # handler send code 200
                self.send_header('Content-type', 'text/html')  # handler send header
                self.end_headers()  # handler send a blank line to end headers section

                # build form
                output = "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form " \
                          "method='POST' " \
                          "enctype='multipart/form-data' " \
                          "action='/restaurant/new' " \
                          ">" \
                          "<input type='text' name='newRestaurantName' placeholder='New Restaurant Name'>" \
                          "<input type='submit' value='Create'>"
                output += "</form>"
                output += "</body></html>"
                self.wfile.write(output)  # write output content string to handler's wfile for response
                return  # exit with normal

            # /restaurant
            if self.path.endswith("/restaurant"):
                # get all restaurant from db
                restaurants = session.query(Restaurant).all()

                # standard 200 ok
                self.send_response(200)  # handler send code 200
                self.send_header('Content-type', 'text/html')  # handler send header
                self.end_headers()  # handler send a blank line to end headers section

                # build restaurant list
                output = "<html><body>"
                # make new restaurant link
                output += "<a href='/restaurant/new'>" \
                          "Make a New Restaurant Here" \
                          "</a></br></br>"
                # restaurant list
                for restaurant in restaurants:
                    output += restaurant.name + "</br>"  # restaurant name
                    output += "<a href='/restaurant/%s/edit'>Edit</a></br>" % restaurant.id  # edit link
                    output += "<a href='/restaurant/%s/delete'>Delete</a></br></br>" % restaurant.id  # delete link
                output += "</body></html>"

                # write out
                self.wfile.write(output)  # write output content string to handler's wfile for response
                # print(output)  # debug in terminal
                return  # exit with normal

            # /hello
            if self.path.endswith("/hello"):  #match handler's url ending with /hello
                self.send_response(200)  # handler send code 200
                self.send_header('Content-type', 'text/html')  # handler send header
                self.end_headers()  # handler send a blank line to end headers section

                output = ""  # init output string to respond as content
                output += "<html><body>Hello!"  # populate html into content
                # form to post message
                output += "<form method='POST' " \
                          "enctype='multipart/form-data' " \
                          "action='/hello'>" \
                          "<h2>What would you like to say</h2>" \
                          "<input name='message' type = 'text'>" \
                          "<input type='submit' value='Submit'>" \
                          "</form>"
                output += "</body></html>"

                self.wfile.write(output)  # write output content string to handler's wfile for response
                print(output)  # debug in terminal
                return  # exit with normal

            # /hola
            if self.path.endswith("/hola"):  #match handler's url ending with /hello
                self.send_response(200)  # handler send code 200
                self.send_header('Content-type', 'text/html')  # handler send header
                self.end_headers()  # handler send a blank line to end headers section

                output = ""  # init output string to respond as content
                output += "<html><body>&#161Hola" \
                          "<a href = '/hello'>Back to Hello</a>" # populate html into content
                output += "</body></html>"

                self.wfile.write(output)  # write output content string to handler's wfile for response
                print(output)  # debug in terminal
                return  # exit with normal

        except IOError:  # IOError
            self.send_error(  # send error response
                404,  # with code 404
                "File Not Found %s" % self.path  # and message for 404, with handlers' url
            )

    # overwrites the default do_POST method of BaseHTTPRequestHandler
    def do_POST(self):
        try:
            # POST delete
            if self.path.endswith('/delete'):
                # get new restaurant name from post form data
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))  # get content type from header
                restaurantId = self.path.split("/")[2]  # get id from url
                myRestaurantORM = session.query(Restaurant).filter_by(id=restaurantId).one()  # get first restaurant by id
                if myRestaurantORM != []:
                    session.delete(myRestaurantORM)
                    session.commit()

                    #redirection after put
                    self.send_response(301)  # response with 301 for success POST
                    self.send_header('Content-type', 'text/html')  # handler send header
                    self.send_header('Location', '/restaurant')  # respond with redirection
                    self.end_headers()  # end headers section

            # POST /restaurant/<id>/edit
            if self.path.endswith('/edit'):
                # get new restaurant name from post form data
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))  # get content type from header
                if ctype == 'multipart/form-data':  # form data is for posted forms
                    fields = cgi.parse_multipart(self.rfile, pdict)  # parse form data from rfile as pdict indicates
                    newRestaurantName = fields.get('newRestaurantName')  # returns a list
                    restaurantId = self.path.split("/")[2]  # get id from url
                    myRestaurantORM = session.query(Restaurant).filter_by(id=restaurantId).one()  # get first restaurant by id

                    # found
                    if myRestaurantORM != []:
                        myRestaurantORM.name = newRestaurantName[0]
                        session.add(myRestaurantORM)
                        session.commit()

                        #redirection after put
                        self.send_response(301)  # response with 301 for success POST
                        self.send_header('Content-type', 'text/html')  # handler send header
                        self.send_header('Location', '/restaurant')  # respond with redirection
                        self.end_headers()  # end headers section


            # POST /restaurant/new
            if self.path.endswith('/restaurant/new'):
                # get new restaurant name from post form data
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))  # get content type from header
                if ctype == 'multipart/form-data':  # form data is for posted forms
                    fields = cgi.parse_multipart(self.rfile, pdict)  # parse form data from rfile as pdict indicates
                    newRestaurantName = fields.get('newRestaurantName')  # returns a list

                    #create new restaurant orm
                    newRestaurant = Restaurant(name=newRestaurantName[0])
                    session.add(newRestaurant)
                    session.commit()

                    #redirection after create
                    self.send_response(301)  # response with 301 for success POST
                    self.send_header('Content-type', 'text/html')  # handler send header
                    self.send_header('Location', '/restaurant')  # respond with redirection
                    self.end_headers()  # end headers section

            # other post
            else:
                self.send_response(301)  # response with 301 for success POST
                self.end_headers()  # end headers section

                # get message field from post form data
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))  # get content type from header
                if ctype == 'multipart/form-data':  # form data is for posted forms
                    fields = cgi.parse_multipart(self.rfile, pdict)  # parse form data from rfile as pdict indicates
                    messagecontent = fields.get('message')  # returns a list

                # construct response content
                output = ""
                output += "<html><body>"
                output += "<h2>Okay, how about this: </h2>"
                output += "<h1>%s</h1>" % messagecontent[0]  # element 0 of messagecontent list
                # form to post message
                output += "<form method='POST' " \
                          "enctype='multipart/form-data' " \
                          "action='/hello'>" \
                          "<h2>What would you like to say</h2>" \
                          "<input name='message' type = 'text'>" \
                          "<input type='submit' value='Submit'>" \
                          "</form>"
                output += "</body></html>"

                self.wfile.write(output)  # write output content string to handler's wfile for response
                print(output)  # debug in terminal

        except:
            pass


# MAIN  base server function setup, port
def main():  # entry point
    try:
        port = 8080  # define port to listen to
        server = HTTPServer(  # init instant of http server with
            ('', port),  # a tuple of address,port
            webserverHandler  # and a handler
        )
        print("Web server running on port %s" % port)  # msg server running success
        server.serve_forever()  # keep listening to port

    except KeyboardInterrupt:  # user ctrl+c to stop server
        print("^C entered, stopping web server...")
        server.socket.close()  # close server socket, shut down server

# enter main() when interpret
if __name__ == '__main__':
    main()
