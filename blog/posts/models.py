from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User






class Category(models.Model):
    title = models.CharField(max_length=20)

   
    def __str__(self):
        return self.title

class Banner(models.Model):
    thumbnail = models.ImageField()



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    thumbnail = models.ImageField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('post-detail', kwargs={
             'id': self.id
         })
 

class Comment(models.Model):
    posts = models.ForeignKey(Post,
                on_delete=models.CASCADE,
                related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return f'Comment by {self.name} on {self.posts}'