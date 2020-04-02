# app.py
 Handles the user requests from the browser and renders the html temmplates, interprets the urls and feed the data requested by the user to the database utilities module

# database.py
Initializes the database, contains the SQL statements that create the tables and the relations between the tables

# DBUtil.py
Initializes the database, contains 2 functions
#
## def get_sub_catalogs(name):
Returns the subcatalogs from the database that are contained within a catalog name that's ordered by the user. 
-
Using code trial and error instead of a complex SQL Satatment 
## def get_services(name):
Returns the services from the database that are contained within a subcatalog name that's ordered by the user.
Used a complex SQL join statement.
# 
# Templates
Contains the html files that are renderred by Flask framework to put dynamic data in
# static 
Contains all the static files that aren't changed by the server in anyway to any user