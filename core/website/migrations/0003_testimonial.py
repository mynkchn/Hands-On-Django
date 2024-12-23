# Generated by Django 5.1.4 on 2024-12-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_emp_working'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]