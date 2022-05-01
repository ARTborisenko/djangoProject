from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta():
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание', max_length=500)

    def __str__(self):
        return "{}".format(f'{self.name}')


class Post(models.Model):
    class Meta():
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст статьи", max_length=1500)
    image = models.ImageField("Изображение", upload_to="post/", blank=True)
    create = models.DateTimeField("Создан", auto_now_add=True)
    moder = models.BooleanField("Модерация", default=False)
    update = models.DateTimeField("Обновлено", auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(f'{self.title}: {self.text[0:20]}...')


class CommentPost(models.Model):
    class Meta():
        db_table = 'commentpost'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Текст комментария")
    create = models.DateTimeField("Создан", auto_now_add=True)
    update = models.DateTimeField("Обновлен", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return "{}".format(f'{self.text}')