# Generated by Django 5.0.3 on 2024-04-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=30)),
                ('is_admin', models.BooleanField(max_length=200)),
                ('add_date', models.DateTimeField()),
            ],
        ),
    ]
