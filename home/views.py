from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,CreateView,DetailView,FormView,TemplateView
from django.views.generic.edit import DeleteView,UpdateView
from .models import Post,Comment
from .forms import PostForm,CommentForm,EditCommentForm
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages

class HomeView(View):
    #model = Post
    template_name='home.html'

    paginate_by = 1

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts,self.paginate_by)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'post_list':page_obj
        }

        return render(request,self.template_name,context)

class CommentGet(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("detail", kwargs={'pk': post.pk})


class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostNewView(CreateView):
    model = Post
    template_name = 'newpost.html'
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'updatepost.html'
    fields = ['title','excerpt','body','photo']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

def edit_comment(request, pk):
    comments = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comments)
        if form.is_valid():
            form.save()
            messages.success(request,'Your comment updated successfully','success')
            return redirect('home')
    else:
        form = EditCommentForm(instance=comments)

    context = {

        'form': form,
        'comments': comments,

    }
    return render(request, 'edit_comment.html', context)


def delete_comment(request, pk):
    comments = get_object_or_404(Comment, pk=pk)
    comments.delete()
    messages.success(request,'Your comment deleted successfully','success')
    return redirect('home')

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'

class CategoryView(View):
    def get(self,request,category):
        posts=Post.objects.filter(category=category)
        context={
            'category':category,
            'posts':posts,
        }
        return render(request,'category.html',context)