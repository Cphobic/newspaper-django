from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser

from .models import Post
from .forms import PostCreateForm, PostUpdateForm


class HomeView(generic.ListView):
    template_name = 'paper/home.html'
    model = Post
    ordering = ['-pub_date']


class DetailPostView(generic.DetailView):
    template_name = 'paper/detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(self.request, 'paper/post_create.html', context)

    def post(self, *args, **kwargs):
        form = PostCreateForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            cover_photo = form.cleaned_data.get('cover_photo')

            new_post = Post.objects.create(
                title=title,
                author=self.request.user,
                content=content,
                cover_photo=cover_photo,
            )
            new_post.save()
            return redirect('home')
        context = {
            'form': form,
        }

        return render(self.request, 'paper/post_create.html', context)


class EditPostView(generic.UpdateView):
    template_name = 'paper/update.html'
    model = Post
    form_class = PostUpdateForm


class DeletePostView(generic.DeleteView):
    template_name = 'paper/delete_post.html'
    model = Post
    success_url = reverse_lazy('home')
