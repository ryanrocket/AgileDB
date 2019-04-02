# AgileDB
### The most intuitive solution for simple yet powerful database management

## What makes AgileDB the right choice for your?
AgileDB was designed to be simple at the surface but powerful at its core. AgileDB is fast and efficient at compiling your database into a JSON file, allowing for complex data structures and reliable encoding. Anyone can run AgileDB, as its only dependency is Python 3.0 or higher. AgileDB also uses metadata in your databases to make it easy to link relational data between databases. 

## How do I install AgileDB and how do I get started?
To install AgileDB, simple move into a directory where you wish to store AgileDB's contents and clone the repo. To start AgileDB, simple run the command:<br>
```python3 cli.py```<br>
Once the CLI starts up you can run the following command to initialize the filesystem for database storage. This process is not done on installation so running this command on first start is paramount.<br>
```[ agile ] init```<br>
Once the `init` command has been run, the filesystem is good to go for database storage. From here, AgileDB is ready to run, its just that simple.

## How do I create a database and add some data?
Ok, lets start by creating our first database:<br>
```[ agile ] create tester```<br>
This will create a database called 'tester', which can be seen by running the command:<br>
```[ agile ] list```<br>
Once you create a database, or even log into AgileDB, you need to start by selecting the database you wish to modify.<br>
```[ agile ] use tester``` <br>
This command will let us modify the database 'tester'
