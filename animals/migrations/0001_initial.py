# Generated by Django 3.0.8 on 2020-07-09 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=200, verbose_name='Вид')),
                ('breed', models.CharField(blank=True, max_length=200, verbose_name='Порода')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('entry_date', models.DateField(blank=True, verbose_name='Дата поступления')),
                ('weight', models.FloatField(blank=True, verbose_name='Вес')),
                ('height', models.FloatField(blank=True, verbose_name='Рост')),
                ('special_signs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('position', models.PositiveIntegerField(default=0)),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='animals.Animal', verbose_name='Животное')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
