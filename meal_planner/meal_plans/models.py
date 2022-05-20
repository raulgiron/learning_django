from django.db import models

# Create your models here.

class Day(models.Model):
    """A day of the week for the planed meals."""
    text = models.CharField(max_length=9)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Meal(models.Model):
    """A meal the user is planing about."""
    topic = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"