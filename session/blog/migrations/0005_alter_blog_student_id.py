# Generated by Django 4.1.7 on 2023-03-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_created_at_blog_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='student_id',
            field=models.CharField(choices=[('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], default='23', max_length=2),
        ),
    ]
