from django.shortcuts import render, redirect

from .forms import BlogForm
from .models import BlogPost

def index(request):
    """Home page application Blogs"""
    return render(request, 'blogs/index.html')

def blog(request):
    """Page with list blog"""
    texts = BlogPost.objects.order_by('-date_added')
    context = {'texts': texts}
    return render(request, 'blogs/blog.html', context)

def new_post(request):
    """Define new post"""
    if request.method != 'POST':
        # Data don't set
        form = BlogForm()
    else:
        # Date set POST
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, text_id):
    text = BlogPost.objects.get(id=text_id)
    title = text.title
    if request.method != 'POST':
        form = BlogForm(instance=text)
    else:
        form = BlogForm(instance=text, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog')

    context = {'form': form, 'text': text, 'title': title}
    return render(request, 'blogs/edit_post.html', context)
