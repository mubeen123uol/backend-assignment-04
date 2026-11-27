import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from bookstore.models import Book

# Query a specific book by its primary key (ID)
book_id = 1

try:
    book = Book.objects.get(pk=book_id)
    print("=" * 50)
    print(f"       DETAILS OF BOOK (ID: {book_id})")
    print("=" * 50)
    print(f"ID             : {book.id}")
    print(f"Title          : {book.title}")
    print(f"Author         : {book.author}")
    print(f"Published Date : {book.published_date}")
    print(f"ISBN           : {book.isbn}")
    print("=" * 50)
except Book.DoesNotExist:
    print(f"Error: Book with ID {book_id} does not exist in the database.")
