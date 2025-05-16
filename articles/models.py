from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Maqola nomi")
    summary = models.CharField(max_length=200, blank=True, verbose_name="Annotatsiya")
    body = HTMLField(blank=True, verbose_name="Maqola matni")
    # photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='media/', verbose_name="fayl yuklash", )  # Hujjat fayli uchun qo'shimcha maydon

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    approved = models.BooleanField(default=False)  # Admin tasdiqlash maydoni
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")
    
