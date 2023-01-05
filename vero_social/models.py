from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post_vero(models.Model):

    title= models.CharField(max_length=150, default='')
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked_vero')
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, related_name='author_vero', on_delete=models.CASCADE)
    image = models.FileField()
    tag = models.CharField(max_length=50)
    slug_title = models.SlugField()
    bool_stampato = models.BooleanField(default=False) # questo campo lo uso per vedere se il post è stato già stampato
    #dal raccomandation system

    def __str__(self):
        return str(self.tag)

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like_vero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post_vero, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.value)

class tag_piaciuti(models.Model):
    username = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    

    def __str__(self):
        return self.tag


