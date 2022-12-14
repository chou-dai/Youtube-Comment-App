# Generated by Django 3.0.5 on 2022-10-14 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_trend', '0005_videodata_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRankData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField()),
                ('rank', models.IntegerField(default=0)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_data', to='youtube_trend.VideoData')),
            ],
        ),
    ]
