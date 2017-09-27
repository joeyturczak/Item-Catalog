# Item Catalog

This is a web application that provides a list of items which allows
authenticated users to add new items, as well as edit and delete items the
user has created.

# Usage

Instructions for setting up the VM environment to run this program can be found
[here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).

Clone this repository inside the vagrant folder.

Once you have vagrant up and running, `cd /vagrant` to change directories to
your vagrant folder. Cd into the repository directory and run the following
commands to set up the database fill it with some dummy data:

```
python models.py
python fill_database.py
```

Now start up the application!

```
python application.py
```

Navigate to localhost:8000 in your browser to use the app.
