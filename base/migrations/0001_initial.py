# Generated by Django 4.1.7 on 2023-03-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=110)),
                ('phone', models.TextField(max_length=110)),
                ('email', models.TextField(max_length=110)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]