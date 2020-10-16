from django.db import models

from django.contrib.auth.models import User


class Tags(models.Model):
    name = models.CharField(verbose_name='Tag', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Images(models.Model):
    name = models.CharField(verbose_name='Image', max_length=50, default='Unknown')
    post = models.ImageField('picture', null=True, upload_to='userImage/')
    view = models.IntegerField(default=0)
    tag = models.ForeignKey(Tags, verbose_name='Tag', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'




