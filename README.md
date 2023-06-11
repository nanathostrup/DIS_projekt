# DIS_projekt

This is our DIS_Project :)
We wanted to make a overview of all candidates from the last folketingsvalg in Denmark in 2022.
Due to technical issues, we instead made an applicaton in the correct theme, where a person can see a few candidates, add/delete/update their own, or search the database for existing candidates. The application thus lives up to the requirements set fourth by the assignment. 


## How to run:

Before running the application, a user needs to do several things:

### clone the repository
$ git clone https://github.com/nanathostrup/DIS_projekt

$ cd DIS_projekt 

Make sure to have all required packages downloaded:
  
### download all required packages

$ pip install -r requirements.txt

### run the program as such:

1. Create a database in postgres. In "init_db.py" and "app.py", change "USERNAME" and "PASSWORD" so that it suits your database.

2. Run init_db.py.

$ python3 init_db.py

3. Use flask run to run the website. 

$ flask run


## How to navigate:
- Use the mouse
