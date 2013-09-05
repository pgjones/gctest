from django.db import models
from django.core.validators import RegexValidator

alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z]*$', "Alpha numeric only")

class App(models.Model):
    name = models.CharField(max_length=25, validators=[alphanumericValidator])
    current_build = models.ForeignKey("Build", related_name='current_build', null=True, blank=True)
    released = models.BooleanField()
    def __unicode__(self):
        return self.name

class Build(models.Model):
    version = models.DecimalField(max_digits=5, decimal_places=2)
    app = models.ForeignKey(App)
    current = models.BooleanField()
    def __unicode__(self):
        return self.version

class Developer(models.Model):
    name = models.CharField(max_length=25, validators=[alphanumericValidator])
    email = models.EmailField()
    apps = models.ManyToManyField(App)
    def __unicode__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    updated = models.DateTimeField()
    class Meta:
        verbose_name_plural = "news"
