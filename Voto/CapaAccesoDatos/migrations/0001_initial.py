# Generated by Django 3.2.9 on 2021-12-17 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_datos_eleccion',
            fields=[
                ('id_datos_eleccion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_eleccion', models.CharField(max_length=50)),
                ('fecha_eleccion', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='t_padron_electoral',
            fields=[
                ('elector_ci', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_elector', models.CharField(max_length=50)),
                ('apellido_elector', models.CharField(max_length=50)),
                ('correo_institucional', models.EmailField(max_length=50)),
                ('nivel_elector', models.CharField(max_length=50)),
                ('hash', models.CharField(max_length=50)),
                ('registro_voto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_partido',
            fields=[
                ('id_partido', models.AutoField(primary_key=True, serialize=False)),
                ('partido_img', models.ImageField(upload_to='partidos/')),
                ('partido_nombre', models.CharField(max_length=50)),
                ('partido_candidato_img', models.ImageField(upload_to='partidos/')),
                ('nombre_candidato_principal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_voto',
            fields=[
                ('id_voto', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_voto', models.CharField(max_length=50)),
                ('voto_fecha', models.DateField()),
                ('id_partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CapaAccesoDatos.t_partido')),
            ],
        ),
        migrations.CreateModel(
            name='t_escrutinio',
            fields=[
                ('id_escrutinio', models.AutoField(primary_key=True, serialize=False)),
                ('votos_totales', models.IntegerField()),
                ('votos_validos', models.IntegerField()),
                ('votos_invalidos', models.IntegerField()),
                ('votos_nulos', models.IntegerField()),
                ('votos_blancos', models.IntegerField()),
                ('id_voto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CapaAccesoDatos.t_voto')),
            ],
        ),
        migrations.CreateModel(
            name='auditoria',
            fields=[
                ('id_auditoria', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_voto', models.CharField(max_length=50)),
                ('voto_fecha', models.DateField()),
                ('id_partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CapaAccesoDatos.t_partido')),
                ('id_voto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CapaAccesoDatos.t_voto')),
            ],
        ),
    ]
