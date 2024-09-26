from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils import timezone


CATEGORY_CHOICES = [
    ('sport','Sport'),
    ('news','News'),
    ('general','General'),
    ('art','Art'),
    ('lifestyle','LifeStyle'),
    ('health','Health'),
    ('fun','Fun'),
]

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CostomUser',on_delete=models.CASCADE)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    date  = models.DateTimeField(default=datetime.now)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
    
class Comment(models.Model):
    author = models.ForeignKey('accounts.CostomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField(null=False,blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
