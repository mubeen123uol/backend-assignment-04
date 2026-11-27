import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from bookstore.models import Book

# Query all books from the database
books = Book.objects.all()

print("=" * 60)
print("                  LIST OF ALL BOOKS")
print("=" * 60)

for book in books:
    print(f"ID             : {book.id}")
    print(f"Title          : {book.title}")
    print(f"Author         : {book.author}")
    print(f"Published Date : {book.published_date}")
    print(f"ISBN           : {book.isbn}")
    print("-" * 60)

print(f"Total Books: {books.count()}")
