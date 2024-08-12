from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import AddBookForm
from .models import Catalog, Post


class CreatePostView(PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = 'permis.add_post'
    fields = ('title', 'description')
    template_name = 'permis/post.html'


def home(request):
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
    books = Catalog.objects.all()
    add_book_form = AddBookForm()

    return render(request, 'permis/home.html', {
        "add_book_form": add_book_form,
        "books": books
    })
