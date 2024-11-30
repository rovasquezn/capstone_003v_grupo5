from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#from .models import Administrador, Atendedor, Tecnico

User = get_user_model()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and not instance.is_superuser:
#         if instance.user_type == 1:
#             Administrador.objects.create(user=instance)
#         elif instance.user_type == 2:
#             Atendedor.objects.create(user=instance)
#         elif instance.user_type == 3:
#             Tecnico.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        if instance.user_type == 1 and hasattr(instance, 'administrador'):
            instance.administrador.save()
        elif instance.user_type == 2 and hasattr(instance, 'atendedor'):
            instance.atendedor.save()
        elif instance.user_type == 3 and hasattr(instance, 'tecnico'):
            instance.tecnico.save()

def send_password_reset_success_email(user):
    subject = 'Contraseña restablecida con éxito'
    logo_url = f"{settings.SITE_URL}{settings.STATIC_URL}images/Optica Cruz-Calada.jpg"
    html_message = render_to_string('optica/password_reset_success_email.html', {'user': user, 'logo_url': logo_url})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def send_user_creation_email(user, password):
    subject = 'Cuenta creada con éxito'
    logo_url = f"{settings.SITE_URL}{settings.STATIC_URL}images/Optica Cruz-Calada.jpg"
    site_url = settings.SITE_URL
    html_message = render_to_string('optica/user_creation_email.html', {
        'user': user,
        'password': password,
        'logo_url': logo_url,
        'site_url': site_url
    })
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)