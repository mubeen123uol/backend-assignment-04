import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from bookstore.models import Book

# Sample data for books
sample_books = [
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "published_date": "2008-08-01",
        "isbn": "978-0132350884"
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "published_date": "1999-10-30",
        "isbn": "978-0201616224"
    },
    {
        "title": "Django for Beginners",
        "author": "William S. Vincent",
        "published_date": "2022-03-15",
        "isbn": "978-1735467221"
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "published_date": "2021-12-14",
        "isbn": "978-1492056355"
    }
]

# Populate database
for book_data in sample_books:
    book, created = Book.objects.get_or_create(
        isbn=book_data["isbn"],
        defaults=book_data
    )
    if created:
        print(f"Added book: '{book.title}' by {book.author}")
    else:
        print(f"Book already exists: '{book.title}'")

print("\nDatabase populated successfully!")
