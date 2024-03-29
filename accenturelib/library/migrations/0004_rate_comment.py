# Generated by Django 4.1.7 on 2023-03-23 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_categoria_editora_alter_book_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.book')),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.rate')),
            ],
        ),
    ]
