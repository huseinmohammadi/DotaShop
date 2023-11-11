# Generated by Django 4.2.7 on 2023-11-11 13:29

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
            name='BankGateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'نام درگاه تکراری است'}, max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField()),
                ('wage', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BankGatewayReceiveTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(default='', max_length=24)),
                ('module', models.CharField(choices=[('WALLET', 'Wallet')], db_index=True, default='WALLET', max_length=255)),
                ('type', models.CharField(choices=[('SHETAB', 'Shaparak')], db_index=True, max_length=255)),
                ('details', models.JSONField(default=dict)),
                ('amount', models.DecimalField(db_index=True, decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('SUCCEEDED', 'Succeeded'), ('FAILED', 'Failed'), ('REQUESTED', 'Requested')], db_index=True, max_length=255)),
                ('desc', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gateway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='bank_gateway.bankgateway')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
