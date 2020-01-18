import os
import sqlite3

import pytest

from pythontest.helpers import helpers


def test_compare_tables():
    helpers.print_pakkaran()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "testdb.db")
    sql = sqlite3.connect(db_path)
    cursor = sql.cursor()

    sqlquery1 = """CREATE TABLE IF NOT EXISTS ATable(
      id    INTEGER PRIMARY KEY,
      text  TEXT NOT NULL
    );
    """

    sqlquery2 = """CREATE TABLE IF NOT EXISTS BTable(
      id    INTEGER PRIMARY KEY,
      text  TEXT NOT NULL
    );
    """
    cursor.execute(sqlquery1)
    cursor.execute(sqlquery2)

    insertqueryAtable1="""INSERT INTO ATable (text) values ('Micro Service1');"""
    cursor.execute(insertqueryAtable1)
    insertqueryAtable2="""INSERT INTO ATable (text) values ('Micro Service2');"""
    cursor.execute(insertqueryAtable2)

    insertqueryBtable1="""INSERT INTO BTable (text) values ('Micro Service1');"""
    cursor.execute(insertqueryBtable1)

    insertqueryBtable2="""INSERT INTO BTable (text) values ('Micro Service2');"""
    cursor.execute(insertqueryBtable2)

    # Comment above and uncomment below to get data disparity
    # insertqueryBtable3 = """INSERT INTO BTable (text) values ('Micro Service3');"""
    # cursor.execute(insertqueryBtable3)



    cursor.execute("select * from ATable;")
    result1 = cursor.fetchall()
    cursor.execute("select * from BTable;")
    result2 = cursor.fetchall()

    # for row in rows:
    #     print(row)

    assert len(result1) == len(result2)
    for i in range(len(result1)):
        for j in range(len(result1[i])):
            assert result1[i][j] == result2[i][j]


    # for result in result1:
    #     for resultdata in result:
    #         print(resultdata)


if __name__ == '__main__':
    test_compare_tables()