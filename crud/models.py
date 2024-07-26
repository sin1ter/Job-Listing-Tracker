from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.

class Recruiter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recruiters_name = models.CharField(max_length=254)
    recruiters_email = models.EmailField()
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.recruiters_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Recruiter, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.recruiters_name)
        unique_slug = slug
        num = 1
        while Recruiter.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

class Job(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=254)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.CASCADE)
    requirements = models.TextField()
    job_position = models.CharField(max_length=254)
    job_link = models.URLField()
    apply_date = models.DateField()

    PENDING = 'Pending'
    REJECTED = 'Rejected'
    REPLIED = 'Replied'
    GHOSTED = 'Ghosted'
    ACCEPTED = 'Accepted'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (REPLIED, 'Replied'),
        (GHOSTED, 'Ghosted'),
        (ACCEPTED, 'Accepted'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.company_name 


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Job, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.company_name)
        unique_slug = slug
        num = 1
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug


class Skills(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skills = models.CharField(max_length=254)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.skills

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Skills, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.skills)
        unique_slug = slug
        num = 1
        while Skills.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug
    