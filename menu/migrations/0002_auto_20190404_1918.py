# Generated by Django 2.1.7 on 2019-04-04 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'pages'), ('model', 'page')), models.Q(('app_label', 'news'), ('model', 'post')), models.Q(('app_label', 'news'), ('model', 'сategory')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Ссылка на'),
        ),
    ]
