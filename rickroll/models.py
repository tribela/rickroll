import base58
from django.db import models
from django.urls import reverse


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(
        upload_to='rickroll.LinkPicture/bytes/filename/mimetype',
        blank=True, null=True
    )
    destination = models.URLField()

    @property
    def id_str(self):
        return base58.b58encode_int(self.id)

    def get_absolute_url(self):
        return reverse('link_view', args=[self.id_str])

    def get_preview_url(self):
        return reverse('preview', args=[self.id_str])

    def __str__(self):
        return f'{self.title} → {self.destination}'


class LinkPicture(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
