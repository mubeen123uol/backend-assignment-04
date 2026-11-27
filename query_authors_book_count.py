import os
import django
from django.db.models import Count

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore_project.settings')
django.setup()

from bookstore.models import Author

# Query all authors and count the number of books written by each
authors = Author.objects.annotate(total_books=Count('books')).order_by('name')

print("=" * 65)
print("          AUTHORS AND NUMBER OF BOOKS WRITTEN")
print("=" * 65)
print(f"{'Author Name':<25} | {'Country':<18} | {'Total Books'}")
print("-" * 65)

for author in authors:
    print(f"{author.name:<25} | {author.country:<18} | {author.total_books}")

print("=" * 65)
