# Generated by Django 5.0 on 2024-01-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_city_remove_customuser_destrict_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name_plural': 'CustomUser'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
