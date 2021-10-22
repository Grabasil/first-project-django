from django.db import models
from django.contrib.auth.models import User

#Create your models here.

class Company(models.Model):
    name_company = models.CharField(max_length=150, verbose_name='Название компании')
    address_company = models.CharField(max_length=150, verbose_name='Адресс компании')

    def __str__(self):
        return self.name_company

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Office(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Название компании')
    name_office = models.CharField(max_length=150, verbose_name='Название офиса')
    name_address = models.CharField(max_length=150, verbose_name='Адресс офиса')

    def __str__(self):
        return self.name_office

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

class Cabinet(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name='Название офиса')
    floor_office = models.CharField(max_length=50, verbose_name='Номер этажа')
    numbers_cabinet = models.CharField(max_length=50, verbose_name='Номер кабинета')

    def __str__(self):
        return self.numbers_cabinet

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Assistant(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Введите логин')
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name='Название кабинета')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    patronymic_name = models.CharField(max_length=150, verbose_name='Отчество')
    post = models.CharField(max_length=100, verbose_name='Должность')
    e_mail = models.EmailField(max_length=250, verbose_name='e-mail')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic_name} ({self.post})"

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
