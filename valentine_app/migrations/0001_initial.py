# Generated by Django 4.1.2 on 2023-02-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
