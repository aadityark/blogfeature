from django.conf import settings
from django.db import models
from blogauth.models  import UserProfileInfo
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    CATA_CHOICES = (
        ('ART','ART'),
        ('BEAUTY','BEAUTY'),
        ('BOOKS','BOOKS'),
        ('CULTURE','CULTURE'),
        ('FICTION','FICTION'),
        ('FILM','FILM'),
        ('FOOD','FOOD'),
        ('GAMING','GAMING'),
        ('HUMOUR','HUMOUR'),
        ('MEDIUM','MEDIUM')
    )
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    catagory = models.CharField(max_length=25,
                                      choices=CATA_CHOICES,
                                      default='MEDIUM')                                  
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blogcontent.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

  

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)    

    