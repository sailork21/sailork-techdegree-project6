from django.db import models

# Create your models here.
class Mineral(models.Model):
    name = models.CharField(max_length=500, blank=True)
    img_file = models.CharField(max_length=500, blank=True)
    img_caption = models.CharField(max_length=500, blank=True)
    category = models.CharField(max_length=500, blank=True)
    formula = models.CharField(max_length=500, blank=True)
    strunz = models.CharField(max_length=500, blank=True)
    color = models.CharField(max_length=500, blank=True)
    crystal_sys = models.CharField(max_length=500, blank=True)
    unit = models.CharField(max_length=500, blank=True)
    crystal_sym = models.CharField(max_length=500, blank=True)
    cleavage = models.CharField(max_length=500, blank=True)
    mohs = models.CharField(max_length=500, blank=True)
    luster = models.CharField(max_length=500, blank=True)
    streak = models.CharField(max_length=500, blank=True)
    diaphaneity = models.CharField(max_length=500, blank=True)
    optical = models.CharField(max_length=500, blank=True)
    refractive = models.CharField(max_length=500, blank=True)
    crystal_habit = models.CharField(max_length=500, blank=True)
    specific_gravity = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name
