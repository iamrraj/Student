# Generated by Django 2.0.4 on 2018-06-13 09:18

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, max_length=600, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('credits', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sems.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProvimetMundshme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1)),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=1)),
                ('level', models.CharField(choices=[('1', 'Bachelor'), ('2', 'Master')], default='Bachelor', max_length=100)),
                ('course', models.ManyToManyField(to='sems.Course')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sems.Program')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.BooleanField()),
                ('featured', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sems.Course')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sems.Program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, default='no-img.png', null=True, upload_to='')),
                ('website', models.URLField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('viti', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1)),
                ('semester', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=1)),
                ('level', models.CharField(choices=[('1', 'Bachelor'), ('2', 'Master')], default=1, max_length=100)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sems.State')),
                ('course', models.ManyToManyField(related_name='course', to='sems.Course')),
                ('course_teacher', models.ManyToManyField(related_name='course_teacher', to='sems.Course')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sems.Program')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])),
                ('upload_time', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sems.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sems.Program'),
        ),
    ]
