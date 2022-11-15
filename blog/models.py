from django.db import models
# next two lines are to import the current user model which is CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
