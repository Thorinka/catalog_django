from django.db import models


# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    post = models.TextField(verbose_name='публикация')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='статус')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.blog_title}'

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
