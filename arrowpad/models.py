from django.db import models
import uuid, os, re

def categoryVector_path(instance, fileName):
    ext = os.path.splitext(fileName)[1].lower()
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'cv_{folderName}_{uuid.uuid4().hex}{ext}'
    return f'images/categories/{folderName}/{unique_name}'

def categoryVectorWebp_path(instance, fileName):
    ext = '.webp'
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'cv_{folderName}_{uuid.uuid4().hex}{ext}'
    return f'images/categories/{folderName}/{unique_name}'


class categories(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    vector = models.ImageField(upload_to=categoryVector_path)
    vectorWebp = models.ImageField(upload_to=categoryVectorWebp_path)
    brief = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=255)
    postCount = models.IntegerField(default=0)
    youtubePlaylist = models.URLField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

class categoryMeta(models.Model):
    category = models.OneToOneField(categories, on_delete=models.CASCADE, related_name='categoryMeta')
    metaTitle = models.CharField(max_length=255)
    metaTags = models.CharField(max_length=255)
    metaDescription = models.TextField()
    metaKeywords = models.CharField(max_length=255)

def bannerBackgroundImage_path(instance, fileName):
    ext = '.webp'
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'bbg_{folderName}_{uuid.uuid4().hex}{ext}'
    return f'images/banner/{folderName}/{unique_name}'

def bannerRightImage_path(instance, fileName):
    ext = '.png'
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'br_{folderName}_{uuid.uuid4().hex}{ext}'
    return f'images/banner/{folderName}/{unique_name}'

def bannerLeftImage_path(instance, fileName):
    ext = '.png'
    folderName = re.sub(r'[^\w]', '_', instance.title)
    unique_name = f'br_{folderName}_{uuid.uuid4().hex}{ext}'
    return f'images/banner/{folderName}/{unique_name}'

class banner(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    backgroundImage = models.ImageField(upload_to=bannerBackgroundImage_path)
    rightImage = models.ImageField(upload_to=bannerRightImage_path, null=True, blank=True)
    leftImage = models.ImageField(upload_to=bannerLeftImage_path)
    btnText = models.CharField(max_length=20, null=True, blank=True)
    btnUrl = models.URLField(max_length=1000, null=True, blank=True)
    color = models.CharField(max_length=10, default='#000000')
    position = models.IntegerField()
    active = models.BooleanField(default=True)
