# Generated by Django 3.2.7 on 2021-09-28 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=150, verbose_name='Название компании')),
                ('address_company', models.CharField(max_length=150, verbose_name='Адресс компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_office', models.CharField(max_length=150, verbose_name='Название офиса')),
                ('name_address', models.CharField(max_length=150, verbose_name='Адресс офиса')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company', verbose_name='Название компании')),
            ],
            options={
                'verbose_name': 'Офис',
                'verbose_name_plural': 'Офисы',
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_office', models.CharField(max_length=50, verbose_name='Номер этажа')),
                ('numbers_cabinet', models.CharField(max_length=50, verbose_name='Номер кабинета')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.office', verbose_name='Название офиса')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('patronymic_name', models.CharField(max_length=150, verbose_name='Отчество')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
                ('e_mail', models.EmailField(max_length=250, verbose_name='e-mail')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.cabinet', verbose_name='Название кабинета')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Введите логин')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудник',
            },
        ),
    ]
