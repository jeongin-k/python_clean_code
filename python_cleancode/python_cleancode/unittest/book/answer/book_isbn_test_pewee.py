import unittest
from peewee import *
# pip install peewee
from isbn_validator import ISBNValidator

database = SqliteDatabase(':memory:')
#database = SqliteDatabase('book.db')

class BaseModel(Model):
    class Meta:
        database = database

class Book(BaseModel):
    id = IntegerField(unique=True)
    title = TextField()
    isbn = TextField()

class BookTestCase(unittest.TestCase):

    def setUp(self):
        database.connect()
        database.create_tables([Book]) 
        try:
            with database.atomic():
                user = Book.create(id=1, title='Clean Code', isbn='978-8-966-26095-9')
                user = Book.create(id=2, title='Beyond the Basic Stuff with Python', isbn='1-189-90945-6')
                user = Book.create(id=3, title='No such a book', isbn='0-189-90945-6')
        except ItegrityError:
              print('database integrity error: primary key dup')

    def tearDown(self):
        database.drop_tables([Book])
        database.close()


    def test_get_all_success(self):
        query = Book.select()
        result = [book.id for book in query]
        cnt = len(result)
        self.assertEqual(3, cnt)
        pass
            

    def test_persist_success(self):
        user = Book.create(id=4, title='JavaScript Deinitive Guide', isbn='978-8-966-26120-8')
        query = Book.select()
        result = [book.id for book in query]
        cnt = len(result)
        self.assertEqual(4, cnt)
        pass


    def test_delete_success(self):
        query = Book.get(Book.id == 1)
        query.delete_instance()
        query = Book.select()
        result = [book.id for book in query]
        cnt = len(result)
        self.assertEqual(2, cnt)
        pass

    def test_isbn_success(self):
        query = Book.select(Book.id, Book.isbn)
        for book in query:
            if book.id == 1:
                self.assertTrue(ISBNValidator(book.isbn).is_valid())
            elif book.id == 2:
                self.assertTrue(ISBNValidator(book.isbn).is_valid())
            elif book.id == 3:
                self.assertFalse(ISBNValidator(book.isbn).is_valid())
            elif book.id == 4:
                self.assertTrue(ISBNValidator(book.isbn).is_valid())


if __name__ == '__main__':
    unittest.main()
