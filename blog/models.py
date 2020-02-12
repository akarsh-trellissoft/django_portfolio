from django.db import models

class Author(models.Model):
    title = models.CharField(max_length=64)
    pub_date = models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='image/')
    def __str__(self):
        return self.title
