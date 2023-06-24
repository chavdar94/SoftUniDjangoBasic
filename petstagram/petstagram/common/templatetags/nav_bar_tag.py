from django.template import Library
# from petstagram.accounts.models import User -> когато имаме потребител

register = Library()


@register.simple_tag
def get_user():
    # user = Profile.objects.first() -> това ще вземе първия обект от таблицата 'Profile', а като имаме вече потребители ще се промени малко логиката
    user = True
    return user
