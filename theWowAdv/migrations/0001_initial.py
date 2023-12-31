# Generated by Django 4.2.2 on 2023-07-17 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('T', 'Танки'), ('HM', 'Хилы'), ('DD', 'ДД'), ('TrM', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('FM', 'Кузнецы'), ('LM', 'Кожевники'), ('PM', 'Зельевары'), ('WM', 'Мастера заклинаний')], default='T', max_length=3, verbose_name='Категория')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('exp_date', models.DateTimeField(blank=True, null=True, verbose_name='Актуально до')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advert', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(verbose_name='Принято')),
                ('text', models.TextField(max_length=512)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('responseAdvertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theWowAdv.advertisement')),
                ('responseUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
    ]
