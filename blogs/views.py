from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

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

@login_required
def new_post(request):
    """Define new post"""
    if request.method != 'POST':
        # Data don't set
        form = BlogForm()
    else:
        # Date set POST
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:blog')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, text_id):
    text = BlogPost.objects.get(id=text_id)
    title = text.title
    check_post_owner(request, text.owner)
    if request.method != 'POST':
        form = BlogForm(instance=text)
    else:
        form = BlogForm(instance=text, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog')

    context = {'form': form, 'text': text, 'title': title}
    return render(request, 'blogs/edit_post.html', context)


def check_post_owner(request, owner):
    """Checking users owner or not"""
    if owner != request.user:
        raise Http404
