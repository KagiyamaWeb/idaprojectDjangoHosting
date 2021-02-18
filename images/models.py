import datetime
import os

from django.db import models
from django.utils import timezone
from django.core.files import File


class ImageForm(models.Model):
    image = models.ImageField(upload_to = 'images/', width_field='image_width', height_field='image_height')
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    image_url = models.URLField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    def was_published_recently(self):
       return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_remote_image(self):
        if self.image_url and not self.image:
            result = urllib.urlretrieve(self.image_url)
            self.image.save(
                    os.path.basename(self.image_url),
                    File(open(result[0]))
                )
            self.save()    