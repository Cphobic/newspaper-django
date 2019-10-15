from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from accounts.models import CustomUser

from .models import Post


class HomeView(generic.ListView):
    template_name = 'paper/home.html'
    model = Post
    ordering = ['-pub_date']


class DetailPostView(generic.DetailView):
    template_name = 'paper/detail.html'
    model = Post


class CreatePostView(generic.CreateView):
    template_name = 'paper/create_post.html'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(generic.UpdateView):
    template_name = 'paper/update.html'
    model = Post
    fields = ['title', 'content']


class DeletePostView(generic.DeleteView):
    template_name = 'paper/delete_post.html'
    model = Post
    success_url = reverse_lazy('home')
