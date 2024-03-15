# Generated by Django 4.2.10 on 2024-02-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0003_employeemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=115, null=True)),
                ('age', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]