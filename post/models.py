from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    class Meta():
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание', max_length=500, blank=True)

    def __str__(self):
        return "{}".format(f'{self.name}')


class Post(models.Model):
    class Meta():
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=100)
    text = RichTextField()
    create = models.DateTimeField("Создан", auto_now_add=True)
    moder = models.BooleanField("Модерация", default=False)
    update = models.DateTimeField("Обновлено", auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def get_absolut_url(self):
        return reverse("post_single", kwargs={"pk": self.id})

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


class Mailing(models.Model):
    class Meta():
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_send = models.DateTimeField('Последняя отправка')
    content = models.TextField('Контент', blank=True)

    def __str__(self):
        return "{}".format(f'{self.user.username} от {self.last_send}')