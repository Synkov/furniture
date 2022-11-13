# Generated by Django 2.2.28 on 2022-11-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_fill_db"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategory",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="категория активна"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="address",
            field=models.CharField(max_length=254, verbose_name="адресс"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="электронная почта"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, verbose_name="описание продукта"),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="description",
            field=models.TextField(blank=True, verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="name",
            field=models.CharField(max_length=64, unique=True, verbose_name="имя"),
        ),
    ]
