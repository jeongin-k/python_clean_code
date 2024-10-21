import unittest
from peewee import *
# pip install peewee

database = SqliteDatabase(':memory:')
#database = SqliteDatabase('book.db')

class BaseModel(Model):
    class Meta:
        database = database

class Book(BaseModel):
    id = IntegerField(unique=True)
    title = TextField()

class BookTestCase(unittest.TestCase):

    def setUp(self):
        database.connect()
        database.create_tables([Book]) 
        try:
            with database.atomic():
                user = Book.create(id=1, title='Python CookBook')
                user = Book.create(id=2, title='Python Tips and Tricks')
        except ItegrityError:
              print('database integrity error: primary key dup')

    def tearDown(self):
        database.drop_tables([Book])
        database.close()


    def test_get_all_success(self):
        query = Book.select()
        result = [book.id for book in query]
        cnt = len(result)
        self.assertEqual(2, cnt)
        pass
            

    def test_persist_success(self):
        user = Book.create(id=3, title='JavaScript Deinitive Guide')
        query = Book.select()
        result = [book.id for book in query]
        cnt = len(result)
        self.assertEqual(3, cnt)
        pass


    def test_delete_success(self):
        query = Book.get(Book.id == 1)
        query.delete_instance()
        query = Book.select()
        result = [book.id for book in query]
        cnt = len(result)
        self.assertEqual(1, cnt)
        pass


if __name__ == '__main__':
    unittest.main()
