from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    watermark = models.CharField(
        max_length=50,
        verbose_name="Водяной знак"
    )
    about = models.CharField(
        max_length=20,
        verbose_name="Второй заголовок",
        null=True,
    )  
    about_us = models.TextField(
        verbose_name="Текст для второго заголовка",
        null=True,
    )
    title_end = models.CharField(
        max_length=50,
        verbose_name="Текст в конце",
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name="Номер телефона"
    )
    email = models.CharField(
        max_length=50,
        verbose_name="Почта"
    )
    description = models.CharField(
        max_length=50,
        verbose_name="Название компании"
    )

    def __str__(self):
        return f"Изменение {self.description}"

    class Meta:
        verbose_name="Настройки сайта"
        verbose_name_plural="Добавить изменения"


class Team(models.Model):
    photo_team = models.ImageField(
        upload_to="photo_team/",
        verbose_name="Фото участника (в формате 337/667)"
    )
    fullname = models.CharField(
        max_length=50,
        verbose_name="ФИО участника"
    )
    job_title = models.CharField(
        max_length=50,
        verbose_name="Должность"
    )

    def __str__(self):
        return f"Добавлен {self.fullname}"


    class Meta:
        verbose_name="Добавление участника"
        verbose_name_plural="Добавить участника"

