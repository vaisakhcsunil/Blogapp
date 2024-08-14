from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts_page = paginator.get_page(page_number)
    return render(request, 'blog.html', {'posts': posts_page})
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})


def contact(request):
    return render(request,"contact.html")