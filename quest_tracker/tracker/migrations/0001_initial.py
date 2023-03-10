# Generated by Django 4.0.7 on 2023-01-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeetask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('EmpID', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('EmpID', models.CharField(max_length=20)),
                ('Projectname', models.CharField(max_length=20)),
                ('Document', models.FileField(upload_to='document')),
            ],
        ),
    ]
