from django.db import models


class BikeRoute(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Review(models.Model):
    bikeroute = models.ForeignKey(BikeRoute, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    review_text = models.CharField(max_length=200)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text