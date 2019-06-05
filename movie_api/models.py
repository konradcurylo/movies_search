from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150, unique=True)
    year = models.CharField(max_length=100)
    rated = models.CharField(max_length=100, blank=True)
    released = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=150)
    writer = models.CharField(max_length=1000)
    actors = models.CharField(max_length=1000)
    plot = models.CharField(max_length=1000,blank=True)
    language = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    awards = models.CharField(max_length=100, blank=True)
    poster = models.CharField(max_length=1000, blank=True)
    metascore = models.CharField(max_length=100, blank=True)
    imdbRating = models.CharField(max_length=100, blank=True)
    imdbVotes = models.CharField(max_length=100, blank=True)
    imdbID = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    dvd = models.CharField(max_length=100, blank=True)
    boxOffice = models.CharField(max_length=100, blank=True)
    production = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.title} (id: {self.id})"

class Rating(models.Model):
    source = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="Ratings")

    def __str__(self):
        return f"Rating from {self.source} to {self.movie.title})"


class Comment(models.Model):
    comment_content = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="Comments")
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Anonymous")

    def __str__(self):
        return f" Comment for {self.movie} (id: {self.movie.id}): {self.comment_content}"
