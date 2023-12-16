# Generated by Django 4.2.6 on 2023-12-16 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('cotent', models.TextField(null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('writer', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('about', models.TextField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/')),
            ],
        ),
    ]