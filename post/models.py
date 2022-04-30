from django.db import models


class Post(models.Model):
    class Meta():
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['create']

    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст статьи", max_length=1500)
    image = models.ImageField("Изображение", upload_to="post/", blank=True)
    create = models.DateTimeField("Создан", auto_now_add=True)
    moder = models.BooleanField("Модерация", default=False)
    update = models.DateTimeField("Обновлено", auto_now=True)

    def __str__(self):
        return "{}".format(f'{self.title}: {self.text[0:20]}...')

