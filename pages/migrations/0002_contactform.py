# Generated by Django 2.1.7 on 2019-03-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
                ('text', models.TextField(verbose_name='Сообщение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-created'],
            },
        ),
    ]
