from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
    )
from .models import Post
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'post/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'  # <app>/<model>_<viewtype>.html   
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'post/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-pub_date')

class PostDetailView(DeleteView):
    model = Post
    template_name = 'post/post_detail.html' 
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post/post_form.html' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post/post_form.html' 

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
    template_name = 'post/post_confirm_delete.html' 
    success_url = '/comu/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def newreply(request):
        if request.method == 'POST':
                comment = Comment()
                comment.comment_body = request.POST['comment_body']
                comment.blog = Post.objects.get(pk=request.POST['blog']) # id로 객체 가져오기        
                comment.comment_user = request.user
                comment.save()
                return redirect('/comu/post/'+ str(comment.blog.id))
        else :
                return redirect('home') # 홈으로


def border_search(request):
    br = Post.objects.all() # 모든 Border 테이블의 모든 object들을 br에 저장하라

    b = request.GET.get('b','') # GET request의 인자중에 b 값이 있으면 가져오고, 없으면 빈 문자열 넣기

    if b: # b에 값이 들어있으면 true
        br = br.filter(title__icontains=b) # 의 title이 contains br의 title에 포함되어 있으면 br에 저장

    return render(request, 'post/search.html', { 'border_search':br , 'b':b})
    # br에는 Border 테이블에 title 이름이 'Singapore'인 데이터들이 들어있고,
    # b에는 내가 처음에 입력했던 'Singapore'가 들어있다.