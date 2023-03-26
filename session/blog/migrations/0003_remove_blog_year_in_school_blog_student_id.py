# Generated by Django 4.1.7 on 2023-03-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='blog',
            name='student_id',
            field=models.CharField(choices=[(17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23')], default=23, max_length=2),
        ),
    ]