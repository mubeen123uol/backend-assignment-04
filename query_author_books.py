import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from bookstore.models import Author

# Query details of a specific author
author_name = "Robert C. Martin"

try:
    author = Author.objects.get(name=author_name)
    print("=" * 60)
    print("                     AUTHOR DETAILS")
    print("=" * 60)
    print(f"Name         : {author.name}")
    print(f"Birth Date   : {author.birth_date}")
    print(f"Country      : {author.country}")
    print("-" * 60)
    print(f"Books Written by {author.name}:")
    
    books = author.books.all()
    if books.exists():
        for idx, book in enumerate(books, start=1):
            print(f"  {idx}. {book.title} (Published: {book.published_date}, ISBN: {book.isbn})")
    else:
        print("  No books recorded for this author.")
    print("=" * 60)

except Author.DoesNotExist:
    print(f"Error: Author '{author_name}' not found.")
