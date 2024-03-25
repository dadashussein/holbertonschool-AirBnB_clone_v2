#!/usr/bin/python3
"""Test console test module"""
import MySQLdb
import unittest
import os
from unittest import skip


class TestConsole(unittest.TestCase):
    """Test console class"""
    def setUp(self):
        self.db = MySQLdb.connect(
            host=os.environ.get('HBNB_MYSQL_HOST'),
            user=os.environ.get('HBNB_MYSQL_USER'),
            passwd=os.environ.get('HBNB_MYSQL_PWD'),
            db=os.environ.get('HBNB_MYSQL_DB')
        )
        create_table = """CREATE TABLE IF NOT EXISTS states (
        id INT
        AUTO_INCREMENT
        PRIMARY KEY,
        name VARCHAR(128) NOT NULL)"""
        self.cursor = self.db.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS states")
        self.cursor.execute(create_table)

    def tearDown(self):
        self.db.close()

    def test_create_state(self):
        if not hasattr(self, 'consul'):
            self.skipTest("consul attribute not defined")
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]
        self.consul.onecmd("create State name='California'")
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]
        self.assertEqual(final_count, initial_count + 1)


if __name__ == "__main__":
    unittest.main()
