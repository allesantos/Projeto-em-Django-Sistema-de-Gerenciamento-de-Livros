# Generated by Django 5.0.4 on 2024-06-25 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_alter_emprestimo_data_devolucao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_duracao',
        ),
    ]