# Generated by Django 5.0.2 on 2024-03-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_principal', '0002_alter_setop_custo_unitario_alter_setop_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setop',
            name='codigo',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
