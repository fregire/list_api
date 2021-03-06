# Generated by Django 3.2.6 on 2021-10-05 18:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Наименование элемента не должно быть пустым, состоять или начинаться с пробела или\n                        нечитаемого символа, в качестве разделителя между словами может быть только\n                        одиночный пробел, исключены знаки препинания, возможно использование русских букв\n                        и латиницы;', regex='[А-Яа-я _]+')])),
                ('item_type', models.CharField(choices=[(0, 'Root'), (1, 'End item'), (2, 'Search and filter')], default=1, max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='list.listitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
