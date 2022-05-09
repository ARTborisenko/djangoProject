from django import template
from ..models import Category, User
from allauth.account.admin import EmailAddress



register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_verified_emails():
    emails = []
    context = EmailAddress.objects.filter(verified=True)
    for _ in context:
        emails.append(_.email)
    return emails
