from django.db import models

class artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class movie(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(artist,related_name='artistmovie')

    def __str__(self):            
        return "%s (%s)" % (self.title, " & ".join(artist.name for artist in self.artists.all()))
    

class role(models.Model):
    role_name = models.CharField(max_length=100)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE,related_name='role_artist')
    movie = models.ForeignKey(movie, on_delete=models.CASCADE,related_name='role_movie')

    def __str__(self):
        return self.role_name
    