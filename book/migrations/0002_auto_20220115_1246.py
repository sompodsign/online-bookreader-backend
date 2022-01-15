# Generated by Django 3.2.11 on 2022-01-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]