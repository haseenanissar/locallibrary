from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_searchbook = Book.objects.filter(title__icontains="Harry").count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres' : num_genres,
        'num_searchbook' : num_searchbook,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorDetailView(generic.DetailView):
    model = Author