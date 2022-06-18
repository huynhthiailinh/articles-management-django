from django.shortcuts import render
from matplotlib.pyplot import cla
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'article/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'article/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# def mine(request):
#     return render(request, 'article/mine.html', {'title':'My Articles'})

@login_required
def mine(request):
    context = {
        'posts': Post.objects.all()
        # 'u_posts': Post.objects.filter(author=request.user).all(),
        # 'p_posts': Post.objects.filter(author=request.user.profile).all()
    }
    return render(request, 'article/mine.html', {'title':'My Articles'})