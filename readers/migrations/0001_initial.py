# Generated by Django 3.2.9 on 2021-11-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
    ]
