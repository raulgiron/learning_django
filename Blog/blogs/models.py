from django.db import models


# Create your models here.
class BlogPost(models.Model):
    """A topic the user is blogging about."""
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.title}"