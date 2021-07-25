from django.shortcuts import redirect, render
from books.models import Book, Review
from django.views import generic


class BookIndexView(generic.ListView):
	def get_queryset(self):
		return Book.objects.all()

# def index(request):
# 	dbData = Book.objects.all()
# 	context = {'books': dbData}
# 	return render(request, 'books/index.html', context)

class BookDetailView(generic.DetailView):
	model = Book

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reviews'] = context['book'].review_set.order_by('-created_at')
		context['authors'] = context['book'].authors.all()
		return context


# def show(request, id):
# 	singleBook = get_object_or_404(Book, pk=id)
# 	reviews = Review.objects.filter(book_id=id).order_by('-created_at')
# 	context = {'book': singleBook, 'reviews': reviews}
# 	return render(request, 'books/show.html', context)

def review(request, id):
	body = request.POST['review']
	newReview = Review(body=body, book_id=id, user=request.user)
	newReview.save()
	return redirect('/books')

def author(request, author):
	books = Book.objects.filter(authors__name=author)
	context = {'book_list': books}
	return render(request, 'books/book_list.html', context)
