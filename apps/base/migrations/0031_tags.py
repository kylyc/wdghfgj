# Generated by Django 5.0.3 on 2024-03-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_blogs_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя тега')),
            ],
            options={
                'verbose_name': 'Блоги пользователя',
                'verbose_name_plural': 'Блоги пользователей',
            },
        ),
    ]
