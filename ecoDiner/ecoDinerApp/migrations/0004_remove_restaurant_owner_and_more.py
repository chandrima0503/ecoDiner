# Generated by Django 4.2.2 on 2023-06-28 02:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("ecoDinerApp", "0003_alter_carbonfootprint_energy_consumption_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="restaurant",
            name="owner",
        ),
        migrations.AddField(
            model_name="carbonfootprint",
            name="date_submitted",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="city",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="state",
            field=models.CharField(
                choices=[("UK", "United Kingdom")], default="UK", max_length=2
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="zip_code",
            field=models.CharField(default="", max_length=5),
        ),
        migrations.AlterField(
            model_name="carbonfootprint",
            name="energy_consumption",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="carbonfootprint",
            name="waste_production",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="carbonfootprint",
            name="water_consumption",
            field=models.FloatField(),
        ),
    ]
