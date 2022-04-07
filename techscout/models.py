from django.db import models

class SearchTerm(models.Model):
    datetime_created = models.DateTimeField()
    text = models.CharField(max_length=100)

class SearchLocation(models.Model):
    datetime_created = models.DateTimeField()
    text = models.CharField(max_length=100)

class SearchResult(models.Model):
    search_term = models.ForeignKey(SearchTerm, on_delete=models.CASCADE)
    search_location = models.ForeignKey(SearchLocation, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    job_count = models.IntegerField()
    job_meta = models.JSONField()
