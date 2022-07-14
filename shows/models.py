from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postdata):
        errors={}
        if len(postdata['title']) <2:
            errors['title'] = "Title should be longer than 2 characters"
        if len(postdata['network']) <3:
            errors['network'] = "Network should be longer than 3 characters"
        if len(postdata['description']) <10:
            errors['description'] = "Description must be longer than 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()