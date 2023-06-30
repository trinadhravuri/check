# Generated by Django 4.2 on 2023-06-30 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_img', models.ImageField(null=True, upload_to='media')),
                ('Project_quote', models.CharField(max_length=500)),
                ('project_teamsize', models.IntegerField()),
                ('project_roles', models.TextField(max_length=10000)),
                ('project_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.skills')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]