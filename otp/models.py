import os
from random import randrange
from captcha.image import ImageCaptcha
from django.db import models
from django.utils import timezone
from uuid import uuid4


# Create your models here.


def captcha_image(filename):
    return "%s" % filename


class Captcha(models.Model):
    uuid = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    expired_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=captcha_image, null=True, blank=True, max_length=255)

    @staticmethod
    def create_captcha():
        captcha = Captcha()
        captcha.uuid = str(uuid4())[:5]
        captcha.code = str(randrange(1000, 9999, 1))
        captcha.expired_at = timezone.now() + timezone.timedelta(minutes=5)
        image_file = os.path.join('media', captcha.uuid + ".png")
        image = ImageCaptcha(width=280, height=90)
        image.generate(captcha.code)
        image.write(captcha.code, image_file)
        captcha.save()
        return {'captcha_image': image_file, 'captcha_uuid': captcha.uuid}


