# Generated by Django 4.1.7 on 2023-03-22 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_autor_alter_book_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.categoria'),
        ),
        migrations.AlterField(
            model_name='book',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.editora'),
        ),
    ]
