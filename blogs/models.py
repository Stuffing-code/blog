from django.db import models

# Create your models here.
# class TitlePost(models.Model):
#     title = models.CharField(max_length=100)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
