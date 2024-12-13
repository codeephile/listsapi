from django.db import models

class Movielist(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    video = models.FileField(upload_to='shop/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Songlist(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    video = models.FileField(upload_to='shop/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Booklist(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    image = models.ImageField(upload_to='shop/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

