# Generated by Django 4.2 on 2023-07-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0003_remove_projects_project_skills_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('message', models.CharField(max_length=1000)),
                ('content', models.TextField(max_length=100000)),
            ],
            options={
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]
