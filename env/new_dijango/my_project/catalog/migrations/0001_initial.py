# Generated by Django 2.2 on 2022-06-01 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('parrent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=254)),
                ('url', models.CharField(max_length=500)),
                ('price', models.BigIntegerField()),
                ('special_price', models.BigIntegerField()),
                ('category_ids', models.ManyToManyField(related_name='product_category_id', to='catalog.Category')),
                ('images', models.ManyToManyField(related_name='product_image', to='catalog.Category')),
            ],
        ),
    ]