# AgileDB
#### The most intuitive solution for simple yet powerful database management<br><br>

## What makes AgileDB the right choice for your?
AgileDB was designed to be simple at the surface but powerful at its core. AgileDB is fast and efficient at compiling your database into a JSON file, allowing for complex data structures and reliable encoding. Anyone can run AgileDB, as its only dependency is Python 3.0 or higher. AgileDB also uses metadata in your databases to make it easy to link relational data between databases. 

## How do I install AgileDB and how do I get started?
NOTE: Once you install AgileDB, you cant change the directory of its files w/o damaging it, so pick wisely before installation!<br><br>

To install AgileDB, simple move into a directory where you wish to store AgileDB's contents and clone the repo. To start AgileDB, simple run the command:<br><br>
```agile```<br><br>
Once the CLI starts up you can run the following command to initialize the filesystem for database storage. This process is not done on installation so running this command on first start is paramount.<br><br>
```[ agile ] init```<br><br>
Once the `init` command has been run, the filesystem is good to go for database storage. From here, AgileDB is ready to run, its just that simple.

## How do I create a database and add some data?
Ok, lets start by creating our first database:<br><br>
```[ agile ] create tester```<br><br>
This will create a database called 'tester', which can be seen by running the command:<br><br>
```[ agile ] list```<br><br>
Once you create a database, or even log into AgileDB, you need to start by selecting the database you wish to modify.<br><br>
```[ agile ] use tester``` <br><br>
This command will let us modify the database 'tester'. We can use the `display` command to expose the database file.<br><br>
```[ agile ] display``` <br><br>
Nice and easy, right? Lets start adding data, specifically Relational data. Any type of key to value data in AgileDB is refered to as relational or rel data.<br><br>
```[ agile ] add <type> <key> <value>```<br><br>
```[ agile ] add rel name ryan```<br><br>
Run the display command so you can see how this works. You can also add datatypes of lists (`list`) and dictionaries (`dict`).<br><br>
```[ agile ] add dict <name>```<br><br>
```[ agile ] add list <name>```<br><br>
You can update, or add values to these structures using the `update` command.<br><br>
```[ agile ] update <type> <name> <params>```<br><br>
```[ agile ] update dict <name> <key> <val>```<br><br>
```[ agile ] update list <name> <val>```<br><br>
Pretty easy. So, now lets select some of the data from our database.<br><br>
```[ agile ] select <type> <name>```<br><br>
Its just that simple! Slap in your structure type and the name and it will present your data. So, now lets back out and delete this database.<br><br>
```[ agile ] back```<br><br>
```[ agile ] purge tester```<br><br>
And thats it (for now)! These commands will give you a solid foundation for structuring your database, so go give it a try!
