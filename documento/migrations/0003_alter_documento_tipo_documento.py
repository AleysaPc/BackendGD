# Generated by Django 5.2 on 2025-04-10 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0002_alter_documento_correspondencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='documento.tipodocumento'),
        ),
    ]
