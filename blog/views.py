from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm
from django.core.paginator import Paginator

def blog_list(request):
    all_posts = BlogPost.objects.all().order_by('-date_published')
    paginator = Paginator(all_posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-date_published')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})

@user_passes_test(lambda u: u.is_staff)
def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_detail', post_id=post.id)
        else:
            messages.error(request, 'There was an error with your form. Please check the details.')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog_detail', post_id=post.id)
        else:
            messages.error(request, 'There was an error with your form. Please check the details.')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/add_blog.html', {'form': form, 'editing': True})