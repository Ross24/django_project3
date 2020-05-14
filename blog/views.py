from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment


from .forms import CommentForm
 

from django.urls import reverse

from django_comments.views.moderation import perform_delete

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
      user=get_object_or_404(User,username=self.kwargs.get('username'))
      return Post.objects.filter(author=user).order_by('-date_posted')



def post_detail(request, pk_slug):
    template_name = 'post_detail.html'

    

    if pk_slug.isdigit():
      post = Post.objects.filter(id=pk_slug).first()
    else:
      post = Post.objects.filter(url=pk_slug).first()

    comments = Comment.objects.filter(post=post.id ,active=True)
    #post = Post.objects.get(pk=pk)
    new_comment = None
    # Comment posted
    #comment_form = CommentForm(data=request.POST)

    #if comment_form.is_valid() and request.method == "POST":
    if request.method == 'POST':
      
     

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
          # Post instance which will be assigned to post attribute in Comment model

          #post_instance = get_object_or_404(Post, id=post.id)

          new_comment = comment_form.save(commit=False)
          new_comment.post = get_object_or_404(Post, id=post.id)
          
          new_comment.name = request.user.username
          new_comment.nameid = request.user
          new_comment.save()
          comment_form=CommentForm()




           
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])
        #return redirect('post-detail', 18)

    def form_valid(self, form):
        form.instance.author = self.request.user
        # will save the form and redirect to the success_url
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

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])
        #return redirect('post-detail', 18)




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html')

def delete_own_comment(request, pk):

  #template_name = 'post_detail.html'

  comment = get_object_or_404(Comment, id=pk)
  
  #comments = Comment.objects.filter(post=post.id ,active=True)
  #comment_form=CommentForm()
  #post = Post.objects.filter(id=8).first()
  comment.delete()

  #return reverse('post-detail', comment.post.id)


  #return redirect('post-detail', id=comment.post.id)

  #return reverse('post-detail', kwargs={'pk_slug':comment.post.id})


  return redirect('post-detail', comment.post.id)

  #return render(request, 'blog/home.html')

  
  #return HttpResponseRedirect(reverse('post_detail', kwargs={'pk_slug':comment.post}))


  #return redirect('post_detail', pk=comment.post.id)










  #return render(request, template_name, {'comment_form': comment_form})

#'comments': comments,













  #return HttpResponseRedirect(reverse('post_detail', kwargs={'pk_slug':comment.post.id}))

  #return reverse('post-detail', kwargs={'pk_slug': comment.post.id})



  #return redirect('post_detail', pk=comment.post.id)




  