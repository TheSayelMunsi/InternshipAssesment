# Generated by Django 4.1.7 on 2023-02-21 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.CharField(max_length=100)),
                ('work_type', models.CharField(choices=[('1', 'YOUTUBE'), ('2', 'INSTAGRAM'), ('3', 'OTHERS')], default='None', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='client_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artist_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('work', models.ManyToManyField(max_length=50, to='assignment.client_table')),
            ],
        ),
    ]
