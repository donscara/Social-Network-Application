from django.db import models
from django.urls import reverse
from core.models import Base
# internal
from core.utils import generate_slug
from publish.models import Publish
from django.utils.translation import gettext_lazy as _



class Post(Publish):
    body = models.TextField()

    class Meta:
        db_table = 't_post'

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-detail',
                       args=[
                           self.pk
                       ])

