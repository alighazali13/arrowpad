from django.db import models
from django.utils.translation import gettext as _
import uuid, os, jdatetime, re
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from arrowpad.models import categories

def blogPoster_path(instance, fileName):
    
    ext = os.path.splitext(fileName)[1].lower()
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'{folderName}_{uuid.uuid4().hex}{ext}'
        
    return f'images/blogs/{folderName}/{unique_name}'

def blogPosterWebp_path(instance, fileName):
    
    ext = '.webp'
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'{folderName}_{uuid.uuid4().hex}{ext}'
        
    return f'images/blogs/{folderName}/{unique_name}'

def blogPosterJpeg_path(instance, fileName):
    
    ext = '.jpeg'
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'{folderName}_{uuid.uuid4().hex}{ext}'
        
    return f'images/blogs/{folderName}/{unique_name}'

class blog(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    title = models.CharField(max_length=255, unique=True)
    poster = models.ImageField(upload_to=blogPoster_path)
    posterWebp = models.ImageField(upload_to=blogPosterWebp_path)
    posterJpeg = models.ImageField(upload_to=blogPosterJpeg_path)
    author = models.CharField(max_length=255)
    categories = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='blog')
    brief = models.TextField()
    content = RichTextField()
    url = models.CharField(max_length=255, unique=True)
    publishedAt = jmodels.jDateField(default=jdatetime.date.today)
    updatedAt = jmodels.jDateField(default=jdatetime.date.today)
    totalView = models.IntegerField(default=0)
    hasVideo = models.BooleanField(default=False)
    hasSlider = models.BooleanField(default=False)
    isUpdated = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    

class blogTags(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)
    view = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def getPopularTags(cls, limit=10):
        """
        Return the top 'limit' most viewed blog tags.
        """
        return cls.objects.order_by('-view')[:limit]

class blogMeta(models.Model):
    blog = models.OneToOneField(blog, on_delete=models.CASCADE, related_name='blogMeta')
    metaTitle = models.CharField(max_length=255)
    metaTags = models.CharField(max_length=255)
    metaDescription = models.TextField()
    metaKeywords = models.CharField(max_length=255)


def blogSlides_path(instance, fileName, extension):
    
    ext = os.path.splitext(fileName)[1].lower()
    folderName = re.sub(r'[^\w]', '_', instance.blog.title)
    unique_name = f'{folderName}_{uuid.uuid4().hex}{ext}'

    return f'images/blogs/{folderName}/slides/{unique_name}'

def blogSlidesWebp_path(instance, fileName, extension):
    
    ext = '.webp'
    folderName = re.sub(r'[^\w]', '_', instance.blog.title)
    unique_name = f'{folderName}_{uuid.uuid4().hex}{ext}'

    return f'images/blogs/{folderName}/slides/{unique_name}'

class blogSlides(models.Model):
    blog = models.ForeignKey(blog, on_delete = models.CASCADE, related_name = 'blogSlides')
    image = models.ImageField(upload_to = blogSlides_path)
    imageWebp = models.ImageField(upload_to = blogSlidesWebp_path)

class blogVideos(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogVideos')
    url = models.URLField(max_length=255)

class blogViewTypesChoices(models.IntegerChoices):
    null = 0,
    total = 1,
    today = 2

class blogView(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogView')
    # types = models.IntegerField(default = blogViewTypesChoices.null, choices=blogViewTypesChoices.choices)
    date = jmodels.jDateField(default=jdatetime.date.today)
    view = models.IntegerField()

class blogComment(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogComment')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    jdate = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=False)

class blogReplies(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blogReplies')
    comment = models.ForeignKey(blogComment, on_delete=models.CASCADE, related_name='commentReplies')
    admin = models.CharField(max_length=50)
    reply = models.TextField()
    jdate = jmodels.jDateField(default=jdatetime.date.today)
    active = models.BooleanField(default=False)