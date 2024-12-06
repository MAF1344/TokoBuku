# Generated by Django 5.1.3 on 2024-12-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('published_year', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=100)),
                ('synopsis', models.TextField()),
            ],
        ),
    ]