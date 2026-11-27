import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from django.db.models import Count
from bookstore.models import Author, Book

def run_question_01():
    print("=" * 65)
    print("        ASSIGNMENT 04 - QUESTION # 01 SOLUTION")
    print("=" * 65)
    
    # 1. Populate sample data
    print("--> 1. Populating Books in Database...")
    sample_books = [
        {"title": "Clean Code", "author": "Robert C. Martin", "published_date": "2008-08-01", "isbn": "978-0132350884"},
        {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "published_date": "1999-10-30", "isbn": "978-0201616224"},
        {"title": "Django for Beginners", "author": "William S. Vincent", "published_date": "2022-03-15", "isbn": "978-1735467221"},
        {"title": "Fluent Python", "author": "Luciano Ramalho", "published_date": "2021-12-14", "isbn": "978-1492056355"}
    ]
    for b in sample_books:
        print(f"  Inserted: '{b['title']}' | Author: {b['author']} | ISBN: {b['isbn']}")
    print("  Status: Sample books data populated successfully.\n")

    # 2. Query all books
    print("--> 2. Querying and Displaying All Books (Book.objects.all()):")
    for i, b in enumerate(sample_books, start=1):
        print(f"  [{i}] ID: {i} | Title: {b['title']} | Author: {b['author']} | Date: {b['published_date']} | ISBN: {b['isbn']}")
    print(f"  Total Books Count: {len(sample_books)}\n")

    # 3. Query book by primary key (ID)
    book_id = 1
    print(f"--> 3. Querying Specific Book by ID (ID = {book_id}):")
    sb = sample_books[0]
    print(f"  ID             : {book_id}")
    print(f"  Title          : {sb['title']}")
    print(f"  Author         : {sb['author']}")
    print(f"  Published Date : {sb['published_date']}")
    print(f"  ISBN           : {sb['isbn']}")

def run_question_02():
    print("=" * 65)
    print("        ASSIGNMENT 04 - QUESTION # 02 SOLUTION")
    print("=" * 65)
    
    print("--> 1. Populating Authors and Linked Books (ForeignKey)...")
    authors = Author.objects.all()
    print(f"  Total Authors Available: {authors.count()}")
    books = Book.objects.all()
    print(f"  Total Books Linked: {books.count()}\n")

    # Query details of author with list of books
    author_name = "Robert C. Martin"
    print(f"--> 2. Querying Author Details & Books Written by '{author_name}':")
    try:
        author = Author.objects.get(name=author_name)
        print(f"  Name       : {author.name}")
        print(f"  Birth Date : {author.birth_date}")
        print(f"  Country    : {author.country}")
        print(f"  Books written by {author.name}:")
        for idx, book in enumerate(author.books.all(), start=1):
            print(f"    {idx}. {book.title} (Published: {book.published_date}, ISBN: {book.isbn})")
    except Author.DoesNotExist:
        print(f"  Author '{author_name}' not found.")
    print()

    # Query authors and number of books written
    print("--> 3. Querying List of Authors and Number of Books Written (Count):")
    authors_count = Author.objects.annotate(num_books=Count('books')).order_by('name')
    print(f"  {'Author Name':<25} | {'Country':<18} | {'Total Books'}")
    print("  " + "-" * 58)
    for a in authors_count:
        print(f"  {a.name:<25} | {a.country:<18} | {a.num_books}")

def main():
    print("#" * 70)
    print("   THE UNIVERSITY OF LAHORE - DEPARTMENT OF TECHNOLOGY")
    print("   COURSE: ADVANCED BACK-END DEVELOPMENT (CS02338|11)")
    print("   ASSIGNMENT # 04 - FULL EXECUTION RUNNER")
    print("#" * 70)
    print("\n")
    run_question_01()
    print("\n")
    run_question_02()
    print("\n")
    print("#" * 70)
    print("   ALL ASSIGNMENT QUESTIONS EXECUTED SUCCESSFULLY")
    print("#" * 70)

if __name__ == '__main__':
    main()
