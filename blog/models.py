from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from user.models import User


# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Category, self).save()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    content = models.TextField()
    image = models.CharField(null=True, blank=True, max_length=500)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Blog, self).save()


class Comment(models.Model):
    class Type(models.TextChoices):
        TEXT = "TEXT"
        LIKE = "LIKE"

    text = models.TextField(null=True, blank=True)
    like = models.BooleanField(default=False)
    type = models.CharField(choices=Type.choices, db_index=True, max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        super(Comment, self).save()
