# Generated by Django 3.0.1 on 2022-06-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'تماس باما',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'قوانین',
                'verbose_name_plural': 'قوانین',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'حدمت',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='عنوان سایت')),
                ('logo', models.ImageField(upload_to='', verbose_name='لوگو')),
                ('address', models.CharField(max_length=500, verbose_name='آدرس')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('instagram', models.URLField(blank=True, verbose_name='اینستاگرام')),
                ('linkedin', models.URLField(blank=True, verbose_name='لینکدین')),
                ('twitter', models.URLField(blank=True, verbose_name='واتساپ')),
                ('facebook', models.URLField(blank=True, verbose_name='فیس بوک')),
                ('copyrights', models.CharField(max_length=500, verbose_name='کپی رایت')),
                ('lang', models.FloatField(blank=True, verbose_name='طول جغرافیایی')),
                ('lat', models.FloatField(blank=True, verbose_name='عرض جغرافیایی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
        migrations.CreateModel(
            name='WorkWith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'همکاری با ما',
                'verbose_name_plural': 'همکاری با ما',
            },
        ),
    ]
