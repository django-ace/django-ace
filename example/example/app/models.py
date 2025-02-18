from django.db import models


class Snippet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text.splitlines()[0]

    class Meta:
        ordering = ("-created_at",)
