# Generated by Django 3.2.8 on 2022-12-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_doctor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/'),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/'),
        ),
    ]
