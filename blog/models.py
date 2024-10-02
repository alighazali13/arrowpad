from django.db import models
from django.utils.translation import gettext as _
import uuid, os, jdatetime
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from arrowpad.models import categories

def blogPoster_path(instance, fileName):
    status = True
    while status:
        if ' ' in instance.title:
            folderName = instance.title.replace(' ','_')
        if '.' in instance.title:
            folderName = instance.title.replace('.','_')
        if '.' not in instance.title and ' ' not in instance.title:
            status = False
    fileName = 'bp_' + uuid.uuid4 + uuid.uuid4 + '.webp'

    return 'Images/Blogs/{0}/{1}'.format(folderName, fileName)

def blogSlides_path(instance, fileName):
    status = True
    while status:
        if ' ' in instance.blog.title:
            folderName = instance.title.replace(' ','_')
        if '.' in instance.blog.title:
            folderName = instance.title.replace('.','_')
        if '.' not in instance.blog.title and ' ' not in instance.blog.title:
            status = False
    fileName = 'bs_' + uuid.uuid4 + uuid.uuid4 + '.webp'

    return 'Images/Blogs/{0}/{1}'.format(folderName, fileName)

def blogVideo_path(instance, fileName):
    status = True
    while status:
        if ' ' in instance.blog.title:
            folderName = instance.title.replace(' ','_')
        if '.' in instance.blog.title:
            folderName = instance.title.replace('.','_')
        if '.' not in instance.blog.title and ' ' not in instance.blog.title:
            status = False
    fileName = 'bv_' + uuid.uuid4 + uuid.uuid4 + '.webp'

    return 'Videos/Blogs/{0}/{1}'.format(folderName, fileName)

class blog(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    title = models.CharField(max_length=255, unique=True)
    poster = models.ImageField(upload_to=blogPoster_path)
    author = models.CharField(max_length=255)
    categories = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='blog')
    brief = models.TextField()
    content = RichTextField()
    url = models.URLField(max_length=255, unique=True)
    publishedAt = jmodels.jDateField(default=jdatetime.date.today)
    updatedAt = jmodels.jDateField(default=jdatetime.date.today)
    hasVideo = models.BooleanField(default=False)
    hasSlider = models.BooleanField(default=False)
    isUpdated = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class blogMeta(models.Model):
    blog = models.OneToOneField(blog, on_delete=models.CASCADE, related_name='blogMeta')
    metaTitle = models.CharField(max_length=255)
    metaTags = models.CharField(max_length=255)
    metaDescription = models.TextField()
    metaKeywords = models.CharField(max_length=255)

class blogSlides(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogSlides')
    image = models.ImageField(upload_to=blogVideo_path)


class blogVideos(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogVideos')
    image = models.FileField(upload_to=blogVideo_path)

