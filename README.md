# pakkaranspython

pakkara these are the steps

First you need to install python 3.5> versions

then you would need to create a virtual environment like this 
```python3 -m venv ~/.venvs/<nameofyourchoice>```

then you would need to acitvate it like this

```source ~/.venvs/<name>/bin/activate```

once you are in the virtual environment, navigate to the folder in the checked out repo where you have requirements.txt

then you should do

```python setup.py develop```
```pip install -r requirements.txt```
```pip install .```

post that once you are inside the test folder in the checked out code, you can run test like this

``` pytest --html=report.html test.py``` this would create html report


- basically am using something called sqlite3 flat file DB for doing tests. This is a file based db - residing inside test.db file in
the checked out code. When you are running the test, what it does is, it creates two tables, inserts similiar data on both
the tables and since tables are like 2 d arrays does the comparison
- to get failed sitution, you can uncomment the commented out lines and the tests will fail
- If the table to be compared is really huge, then i would recommend creating a hash code for each row, indexing the table
and comparing those indexes in the other table. - provided you have access to copy table, manipulate etc
