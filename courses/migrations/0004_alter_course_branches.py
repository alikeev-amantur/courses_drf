# Generated by Django 4.1.1 on 2022-09-16 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='courses.branch'),
        ),
    ]
