import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from bookstore.models import Author, Book

# Sample Authors
authors_data = [
    {
        "name": "Robert C. Martin",
        "birth_date": "1952-12-05",
        "country": "United States"
    },
    {
        "name": "William S. Vincent",
        "birth_date": "1980-06-20",
        "country": "United States"
    },
    {
        "name": "Luciano Ramalho",
        "birth_date": "1965-04-10",
        "country": "Brazil"
    },
    {
        "name": "J.K. Rowling",
        "birth_date": "1965-07-31",
        "country": "United Kingdom"
    }
]

created_authors = {}
for data in authors_data:
    author, created = Author.objects.get_or_create(
        name=data["name"],
        defaults=data
    )
    created_authors[author.name] = author
    if created:
        print(f"Added author: {author.name}")

# Sample Books linked to Authors
books_data = [
    {
        "title": "Clean Code",
        "author": created_authors["Robert C. Martin"],
        "published_date": "2008-08-01",
        "isbn": "978-0132350884"
    },
    {
        "title": "The Clean Coder",
        "author": created_authors["Robert C. Martin"],
        "published_date": "2011-05-13",
        "isbn": "978-0137081073"
    },
    {
        "title": "Clean Architecture",
        "author": created_authors["Robert C. Martin"],
        "published_date": "2017-09-10",
        "isbn": "978-0134494166"
    },
    {
        "title": "Django for Beginners",
        "author": created_authors["William S. Vincent"],
        "published_date": "2022-03-15",
        "isbn": "978-1735467221"
    },
    {
        "title": "Django for APIs",
        "author": created_authors["William S. Vincent"],
        "published_date": "2022-06-01",
        "isbn": "978-1735467238"
    },
    {
        "title": "Fluent Python",
        "author": created_authors["Luciano Ramalho"],
        "published_date": "2021-12-14",
        "isbn": "978-1492056355"
    }
]

for b_data in books_data:
    book, created = Book.objects.get_or_create(
        isbn=b_data["isbn"],
        defaults=b_data
    )
    if created:
        print(f"Added book: '{book.title}' by {book.author.name}")

print("\nDatabase populated with authors and books successfully!")
