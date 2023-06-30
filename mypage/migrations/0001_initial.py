# Generated by Django 4.2 on 2023-06-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_img', models.ImageField(upload_to='media')),
                ('skill_quote', models.CharField(max_length=350)),
                ('skill_desc', models.TextField(max_length=10000)),
            ],
            options={
                'verbose_name_plural': 'Skills',
            },
        ),
    ]