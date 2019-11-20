from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    post_content=models.TextField()
    post_date=models.DateTimeField(default=datetime.now)
    post_photo=models.ImageField(upload_to='photos/%/%m/%d/', blank=True)
    post_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.post_content

