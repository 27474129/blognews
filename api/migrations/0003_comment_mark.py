# Generated by Django 3.2.15 on 2022-10-29 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0019_auto_20221029_1843'),
        ('api', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_liked', models.JSONField()),
                ('users_disliked', models.JSONField()),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.article')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.JSONField()),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.article')),
            ],
        ),
    ]