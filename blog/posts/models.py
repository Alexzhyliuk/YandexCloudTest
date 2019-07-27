from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
	CATEGORY_CHOICES = (
			("Cooking","Кулинария"),
			("Auto","Авто"),
			("Home","Дом"),
			("Children","Дети"),
			("Another","Другое")
		)

	slug = models.SlugField(max_length=250)
	title = models.CharField(max_length=250, choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='when_published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    when_published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, related_name="posts", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title



# Create your models here.
