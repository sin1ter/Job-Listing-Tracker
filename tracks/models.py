from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUserModel
# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=200)
    startdate = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Track, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Track.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug
    
class Resources(models.Model):
    title = models.ForeignKey("Track", related_name='resources', on_delete=models.CASCADE)
    resources = models.URLField()
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return f"Resources for {self.title.title}"
        
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Resources, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Resources.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

class Bookmark(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.track:
            return f"{self.user.username} bookmarked {self.track.title}"
        else:
            return f"{self.user.username} bookmark"