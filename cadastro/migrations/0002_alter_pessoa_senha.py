# Generated by Django 4.0.3 on 2022-03-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='senha',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
