# Generated by Django 4.0 on 2022-05-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('email', models.EmailField(max_length=20, verbose_name='email')),
                ('comments', models.TextField(max_length=255, verbose_name='comments')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['-id'],
            },
        ),
    ]
