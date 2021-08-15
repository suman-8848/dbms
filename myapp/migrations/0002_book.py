# Generated by Django 3.2.4 on 2021-08-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('publication', models.CharField(max_length=50)),
                ('Isbn_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Author', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=50, null=True)),
                ('Price', models.IntegerField()),
                ('Edition', models.CharField(max_length=20)),
                ('Qty', models.IntegerField()),
                ('CoverImage', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
    ]