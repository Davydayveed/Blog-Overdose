from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import  render
from .models import Post, Comment
from .forms import CommentForm
from newsletter.models import Signup





# Create your views here.

def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

 
def blog(request):
     post = Post.published.all()
     paginator = Paginator (post, 6)
     page = request.GET.get('page')
     try:
         post = paginator.page(page)
     except PageNotAnInteger:
         post = paginator.page(1)
     except EmptyPage:
         post = paginator.page(paginator.num_pages)


     if request.method == "POST":
            email = request.POST["email"]
            new_signup = Signup()
            new_signup.email = email
            new_signup.save()

     context = {
        'page' : page,
        'post' : post
     }

     return render(request, "blog.html", context )


def blog_details(request, id):
    post = Post.objects.all()


    # List of active comments for this post
    comments = post.comments.filter(active=True)


    new_comment = None

    
    if request.method == 'POST':
            # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()


    context = {
        'post' : post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
     }

    return render(request, "blog-details.html", context)

