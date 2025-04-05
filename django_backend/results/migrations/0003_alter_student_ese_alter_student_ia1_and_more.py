# Generated by Django 4.2.10 on 2025-04-05 06:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_student_created_at_student_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ese',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='ia1',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='ia2',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
