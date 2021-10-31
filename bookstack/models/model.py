from mongoengine import StringField, Document, connect, IntField

connect('bookstack')


class Users(Document):
    """
    This collection stores user information.
    """
    username = StringField(max_length=20, required=True)
    password = StringField(max_length=20, required=True)


class Books(Document):
    """
    This collection stores books added by users.
    """
    book_title = StringField(max_length=50, required=True)
    book_author = StringField(max_length=50, required=True)
    isbn = IntField(max_length=20, required=True)
    is_read = StringField(max_length=3, required=True)
    added_by = StringField(max_length=20, required=True)


class Reviews(Document):
    """
    This collection stores book reviews.
    """
    book_review = StringField(max_length=100, required=True)
    book_title = StringField(max_length=50, required=True)
    book_author = StringField(max_length=50, required=True)
    added_by = StringField(max_length=20, required=True)


class Challenges(Document):
    """
    This collection stores challenges.
    """
    challenge_name = StringField(max_length=50, required=True)
    is_completed = StringField(max_length=3, required=True)
    added_by = StringField(max_length=20, required=True)
