from django.urls import path

from . import views

urlpatterns = [
	path('', views.BookIndexView.as_view(), name='index'),
	path('<int:pk>', views.BookDetailView.as_view(), name='book.show'),
	path('<int:id>/review', views.review, name='book.review')
]