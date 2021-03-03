# Generated by Django 3.0.7 on 2021-03-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210302_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('Photo', models.FileField(upload_to='img')),
            ],
        ),
        migrations.DeleteModel(
            name='Indian',
        ),
    ]