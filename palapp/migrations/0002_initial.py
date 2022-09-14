# Generated by Django 4.0.5 on 2022-09-05 04:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('palapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appat', models.CharField(max_length=50, null=True, verbose_name='Apellido Paterno')),
                ('apmat', models.CharField(max_length=50, null=True, verbose_name='Apellido Materno')),
                ('nomb', models.CharField(max_length=50, verbose_name='Nombre')),
                ('dni', models.CharField(default=' ', max_length=8, verbose_name='DNI')),
                ('direccion', models.TextField(default='AREQUIPA', verbose_name='Dirección Casa')),
                ('directra', models.TextField(default='AREQUIPA', verbose_name='Dirección Trabajo')),
                ('pais', models.CharField(default='PERU', max_length=50, verbose_name='Nacionalidad')),
                ('correo', models.EmailField(default='@', max_length=254, verbose_name='eMail')),
                ('telfij', models.CharField(default='', max_length=15, verbose_name='Teléfono Fijo')),
                ('cel1', models.CharField(default='', max_length=15, verbose_name='Celular 1')),
                ('cel2', models.CharField(default='', max_length=15, verbose_name='Celular 2')),
                ('ocupacion', models.CharField(default='', max_length=100, verbose_name='Ocupación')),
                ('percon', models.TextField(default='', verbose_name='Persona de contacto')),
                ('celcon', models.CharField(default='', max_length=15, verbose_name='Numero contacto')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecact', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmobiliaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='RUC')),
                ('rassoc', models.CharField(default='', max_length=80, unique=True, verbose_name='Razón Social')),
                ('direccion', models.CharField(default='AREQUIPA', max_length=150, verbose_name='Dirección')),
                ('correo', models.EmailField(default='@', max_length=254, verbose_name='eMail')),
                ('telfij', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Teléfono Fijo')),
                ('cel1', models.CharField(default='', max_length=15, verbose_name='Celular 1')),
                ('cel2', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Celular 2')),
                ('activo', models.BooleanField(default=1)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_act', models.DateTimeField(auto_now=True, null=True)),
                ('usuario', models.CharField(default='', max_length=50, null=True, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Jefe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appat', models.CharField(max_length=50, null=True, verbose_name='Apellido Paterno')),
                ('apmat', models.CharField(max_length=50, null=True, verbose_name='Apellido Materno')),
                ('nomb', models.CharField(max_length=50, verbose_name='Nombre')),
                ('correo', models.EmailField(default='@', max_length=254, verbose_name='eMail')),
                ('telfij', models.CharField(default='', max_length=15, null=True, verbose_name='Teléfono Fijo')),
                ('cel1', models.CharField(default='', max_length=15, verbose_name='Celular 1')),
                ('cel2', models.CharField(default='', max_length=15, null=True, verbose_name='Celular 2')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecact', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palapp.inmobiliaria')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('manzana', models.CharField(default='A', max_length=2, verbose_name='Manzana')),
                ('lote', models.IntegerField(null=True, verbose_name='Lote')),
                ('area', models.DecimalField(decimal_places=2, default=100, max_digits=8, verbose_name='Area m2')),
                ('preciod', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='P.Venta US$')),
                ('precios', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='P.Venta S/')),
                ('comision', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Comisión %')),
                ('lfrente', models.TextField(default='', null=True, verbose_name='Limite de Frente')),
                ('mlfrente', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Mts Lin. de Frente')),
                ('lder', models.TextField(default='', null=True, verbose_name='Limite Derecho')),
                ('mlder', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Mts Lin. Derecha')),
                ('lizq', models.TextField(default='', null=True, verbose_name='Limite Izquierda')),
                ('mlizq', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Mts Lin. Izquierda')),
                ('lfondo', models.TextField(default='', null=True, verbose_name='Limite Fondo')),
                ('mlfondo', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Mts Lin. Fondo')),
                ('norte', models.TextField(default='', null=True, verbose_name='Norte')),
                ('sur', models.TextField(default='', null=True, verbose_name='Sur')),
                ('este', models.TextField(default='', null=True, verbose_name='Este')),
                ('oeste', models.TextField(default='', null=True, verbose_name='Oeste')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('estado', models.CharField(choices=[('L', 'Libre'), ('S', 'Separado'), ('V', 'Vendido')], default='L', max_length=1, verbose_name='Estado')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecact', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palapp.cliente')),
            ],
            options={
                'verbose_name': 'terreno',
                'verbose_name_plural': 'terrenos',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appat', models.CharField(max_length=50, null=True, verbose_name='Apellido Paterno')),
                ('apmat', models.CharField(max_length=50, null=True, verbose_name='Apellido Materno')),
                ('nomb', models.CharField(max_length=50, verbose_name='Nombre')),
                ('dni', models.CharField(default='', max_length=8, verbose_name='DNI')),
                ('ruc', models.CharField(default='', max_length=11, verbose_name='RUC')),
                ('direccion', models.TextField(default='AREQUIPA', verbose_name='Dirección Casa')),
                ('correo', models.EmailField(default='@', max_length=254, verbose_name='eMail')),
                ('telfij', models.CharField(default='', max_length=15, verbose_name='Teléfono Fijo')),
                ('cel1', models.CharField(default='', max_length=15, verbose_name='Celular 1')),
                ('cel2', models.CharField(default='', max_length=15, verbose_name='Celular 2')),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecact', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('jefe', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='palapp.jefe')),
            ],
        ),
        migrations.CreateModel(
            name='Tramites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip', models.TextField(verbose_name='Detalle')),
                ('por_hacer', models.CharField(choices=[('L', 'Llamar'), ('R', 'Reunirse'), ('C', 'Correo'), ('W', 'Whatsapp'), ('M', 'Messenger')], max_length=1, verbose_name='Via')),
                ('resultado', models.TextField(verbose_name='Resultado Gestión')),
                ('fec_prox', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha proximo trámite')),
                ('lugar', models.CharField(choices=[('C', 'Casa'), ('O', 'Oficina'), ('V', 'Otro lugar')], max_length=1, verbose_name='Donde')),
                ('nivel', models.CharField(choices=[('B', 'Bajo'), ('R', 'Regular'), ('I', 'Interesado'), ('M', 'Muy Interesado'), ('T', 'Totalmente Convencido')], max_length=1, verbose_name='Nivel de Interes')),
                ('observ', models.TextField(verbose_name='Observaciones')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecact', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='palapp.cliente')),
                ('terreno', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='palapp.terreno')),
                ('vendedor', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='palapp.vendedor')),
            ],
            options={
                'verbose_name': 'tramite',
                'verbose_name_plural': 'tramites',
            },
        ),
        migrations.AddField(
            model_name='terreno',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palapp.vendedor'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palapp.vendedor'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palapp.question')),
            ],
        ),
    ]
