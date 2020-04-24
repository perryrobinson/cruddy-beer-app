==============
cruddy-beer-app
==============

Sample CRUD applcation using Python, Flask, SQLAlchemy, and SQLite for maintaining a collection of your favorite beer.


Requirements
============
Create a virtual environment if you don't want to bloat your installed packages.

Please execute the following commands:

    $ git clone https://github.com/perryrobinson/cruddy-beer-app.git
    
    $ pip install -r requirements.txt


Running
=======
If you would like to start fresh with a new database, you can delete the "beer.db" file and just run "python db_creator.py" to make a new empty database that is setup with the right tables and PK/FK relationships.

To run the web app, execute the following command:

    $ python run.py

Open at your Web browser the following link http://127.0.0.1:5000
