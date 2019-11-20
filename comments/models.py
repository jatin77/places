from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    on_post = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
    comment_date = models.DateTimeField(default=datetime.now)
    comment_content=models.TextField()
    comment_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment_content