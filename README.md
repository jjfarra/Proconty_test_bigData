# Proconty Test BigData
This project was a tentative solution for Proconty's Challenge, which has as the principal objective read a table from an origin database and transfer all the data to a new table on a different database. The data source for this project is Kaggle, which will load, store, and transfer to a new database.

## Resources
* Data: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download
* Origin DB: PostgreSQL
* New DB: MySQL

## How to run it
1. Go to [this website] (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download), download the file, and unzip it.
2. Clon this repo
3. Move the first step file to the repo's folder.
4. You need to get PostgreSQL and MySQL, if you haven't installed them, I recommend laragon, you can follow [this tutorial](https://www.kreaweb.be/laragon-add-postgresql/)
5. Create a database on PostgreSQL and MySQL as "creditcard_data"
6. Install the libraries with `pip install -r requirements.txt`
7. Run Load_oring.py, then transfer_data.py

## Workflow
* Load data from CSV file 'creditcard' as pandas' dataframe.
* Using SQLAlchemy we create a class that contains the table name 'creditcard' with its structure.
* Make an object for each row on the dataframe, and append it to a list.
* Save a batch of objects, in this case, 5000 per write in the table
* Then, we read that table on PostgreSQL as a list of tuples.
* Establish a new connection for MySQL and make an object for each tuple, and save it on the new table.
