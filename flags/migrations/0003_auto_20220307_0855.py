# Generated by Django 3.2.12 on 2022-03-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0002_auto_20210909_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
        migrations.AddField(
            model_name='classifier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classifier',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
        migrations.AddField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
        migrations.AddField(
            model_name='flag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
        migrations.AddField(
            model_name='irregularity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='irregularity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
        migrations.AddField(
            model_name='lot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lot',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
        migrations.AddField(
            model_name='tender',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-02-01', help_text='Time of creation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tender',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Last update time'),
        ),
    ]
