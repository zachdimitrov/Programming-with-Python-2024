# Generated by Django 5.1.6 on 2025-02-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_exercise_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Fn', 'Fiction'), ('Nf', 'Non-Fiction'), ('Sf', 'Science Fiction'), ('Hr', 'Horror')], max_length=20)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_available', models.BooleanField(default=True)),
                ('rating', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
