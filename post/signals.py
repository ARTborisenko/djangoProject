from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post, CommentPost, Mailing, User
from django.core.mail import send_mail
from datetime import datetime, timedelta


# Сигнал который реагирует на публикацию новых постов и осуществляет рассылку пользователям
@receiver(post_save, sender=Post)
def post_moder(**kwargs):
    post = kwargs['instance']
    # Eстанавливаем периодичность рассылки
    send_date = datetime.now() - timedelta(minutes=5)
    recipients = []
    if post.moder:
        # Циклом загоняем всех новых пользователей в список рассылки если их там нет
        for user in User.objects.all():
            try:
                if Mailing.objects.get(user=user):
                    pass
            except BaseException:
                add_mailer = Mailing()
                add_mailer.user = user
                add_mailer.last_send = datetime.now()
                add_mailer.save()
                # Собираем список тех, кому давно не делали рассылки
        for recipient in Mailing.objects.filter(last_send__lt=send_date):
            recipients.append(recipient.user.email)

            # Собираем контент из контента новых статей стетей
        content = 'Новые статьи!!! \n'
        for text in Post.objects.filter(update__gt=send_date):
            content += f'{text.text[:45]}... | '
        # print(recipients)
        # print(content)

        # Отправляем письма
        mail = send_mail(
            "New articles!",
            content,
            'TemaB1og@yandex.ru',
            recipients,
            fail_silently=False
        )
        if mail:
            # Обнуляем счетчик отправки писем
            print('Письмо отправлено')
            for recipient in Mailing.objects.filter(last_send__lt=send_date):
                recipient.last_send = datetime.now()
                recipient.content = content
                recipient.save()
        else:
            print('Какая-то ошивка при отправке')
    else:
        print('Статья внесена как черновик.')

        # Сигнал для откликов


@receiver(post_save, sender=CommentPost)
def post_moder(**kwargs):
    comment = kwargs['instance']
    if comment.moder:
        mail = send_mail(
            "The author has accepted your response",
            f'Пользователь {comment.post.author.username} принял Ваш отклик!',
            'TemaB1og@yandex.ru',
            [comment.user.email],
            fail_silently=False
        )
        if mail:
            print('Письмо отправлено')
        else:
            print('Какая-то ошивка при отправке')
    else:
        mail = send_mail(
            'A new response to your article!',
            f'Пользователь {comment.user.username} оставил вам новый отклик, проверьте в разделе "Новые"!',
            'TemaB1og@yandex.ru',
            [comment.post.author.email],
            fail_silently=False
        )
        if mail:
            print('Письмо отправлено')
        else:
            print('Какая-то ошивка при отправке')
