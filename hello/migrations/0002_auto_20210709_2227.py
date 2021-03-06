# Generated by Django 3.2.5 on 2021-07-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField()),
                ('lname', models.TextField()),
                ('email', models.TextField()),
                ('gender', models.TextField()),
                ('phone', models.TextField()),
                ('gname', models.TextField()),
                ('gphone', models.TextField()),
                ('address', models.TextField()),
                ('sec', models.TextField()),
                ('hsec', models.TextField()),
                ('wbjee', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
