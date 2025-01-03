from django.db import models


class FAQ(models.Model):
    """
    Represents a Frequently Asked Question (FAQ) with its answer.
    """
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
