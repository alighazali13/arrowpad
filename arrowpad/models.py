from django.db import models
import uuid

def categoryVector_path(instance, fileName):
    folderName = instance.title
    if ' ' in instance.title:
        folderName = instance.title.replace(' ','_')
    if '.' in instance.title:
        folderName = instance.title.replace('.','_')

    fileName = 'cv_' + uuid.uuid4().hex + uuid.uuid4().hex + '.webp'

    return 'Images/Blogs/{0}/{1}'.format(folderName, fileName)


class categories(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    vector = models.ImageField(upload_to=categoryVector_path)
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
