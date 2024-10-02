from django.shortcuts import render, get_object_or_404 
from .models import Post , Comment
from django.http import Http404 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , EmptyPage
from .forms import CommentForm
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from .forms import SearchForm 
from django.contrib.postgres.search import SearchVector
from .forms import CreatePostForm

# Create your views here.
@login_required
def post_list(request, tag_slug=None):
    
    list_post = Post.published.all()
    
    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        list_post = list_post.filter(tags__in=[tag])
    
    # pagination with 5 post per page
    paginator = Paginator(list_post,3)
    page_number= request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # If page_number is out of range get last page of results 
        posts = paginator.page(paginator.num_pages)
    return render(
        request, 
        'blog/post/list.html',
        {
            'posts': posts,
            'tag': tag
            
        }
    )

@login_required
def post_detail(request,  year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    post = get_object_or_404(
        Post,
        # id=id,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    
    # lists of active comments for this post 
    comments  = post.comments.filter(active=True)
    
    # Form for users to comment 
    form = CommentForm()
    
    # list of similar posts 
    
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in = post_tags_ids,
        
    ).exclude(id=post.id)
    similar_posts = similar_posts.annotate(
        same_tags = Count('tags')
    ).order_by('-same_tags', '-publish')[:4]
    
    
    return render(
        request, 
        'blog/post/detail.html',
        {
            'post':post,
            'comments': comments,
            'form': form,
            'similar_posts': similar_posts
        }
    )


@login_required
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id, 
        status=Post.Status.PUBLISHED,
    )
    comment = None 
    # A comment was posted 
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment Object without saving it to the database 
        comment = form.save(commit=False)
        # Assign the post to the comment 
        comment.post = post 
        # Save the comment to the database 
        comment.save()
        
    return render(
        request, 
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment,
        }
    )
    
@login_required
def post_search(request):
    form = SearchForm()
    query = None 
    results = [] 
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = (
                Post.published.annotate(
                    search = SearchVector('title','body'),
                )
                .filter(search=query)
            )
    return render(
        request,
        'blog/post/search.html',
        {
            'form': form,
            'query': query,
            'results': results,
        }
    )
            
            
@login_required
def create_post(request):
    # form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = form.save(commit=False)
            post.author = request.user
            # post.tags.add(cd['tags'])
            post.save()
            for i in cd['tags']:
                post.tags.add(i)
            post.save()
        
    else:
        form = CreatePostForm()
    
    return render(
        request, 
        'blog/post/create_post.html',
        {
            'form': form,
        }
    )