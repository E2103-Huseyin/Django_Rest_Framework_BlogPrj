# Generated by Django 3.1.6 on 2021-02-03 11:52

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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('EC', 'Education '), ('HL', 'Health '), ('FM', 'Family '), ('TN', 'Technology '), ('EN', 'Economy '), ('RL', 'Religion ')], default='TN', max_length=50)),
                ('status', models.CharField(choices=[('D', 'Draft '), ('P', 'Published ')], default='Published', max_length=50)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('content', models.TextField()),
                ('publish_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]