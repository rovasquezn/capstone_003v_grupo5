# Generated by Django 4.2.15 on 2024-09-08 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abono',
            fields=[
                ('idAbono', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('fechaAbono', models.DateTimeField(auto_now_add=True)),
                ('valorAbono', models.IntegerField(blank=True, null=True)),
                ('formaPagoAbono', models.CharField(blank=True, max_length=10, null=True)),
                ('numeroVoucherAbono', models.IntegerField(blank=True, null=True)),
                ('numeroAbono', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('rutAdministrador', models.IntegerField(primary_key=True, serialize=False)),
                ('dvRutAdministrador', models.CharField(max_length=1)),
                ('nombreAdministrador', models.CharField(max_length=20)),
                ('apPaternoAdministrador', models.CharField(max_length=20)),
                ('apMaternoAdministrador', models.CharField(max_length=20)),
                ('celularAdministrador', models.IntegerField(blank=True, null=True)),
                ('emailAdministrador', models.EmailField(blank=True, max_length=50, null=True)),
                ('nombreUsuarioAdministrador', models.CharField(max_length=20)),
                ('claveAdministrador', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Atendedor',
            fields=[
                ('rutAtendedor', models.IntegerField(primary_key=True, serialize=False)),
                ('dvRutAtendedor', models.CharField(max_length=1)),
                ('nombreAtendedor', models.CharField(max_length=20)),
                ('apPaternoAtendedor', models.CharField(max_length=20)),
                ('apMaternoAtendedor', models.CharField(max_length=20)),
                ('celularAtendedor', models.IntegerField(blank=True, null=True)),
                ('emailAtendedor', models.EmailField(blank=True, max_length=30, null=True)),
                ('nombreUsuarioAtendedor', models.CharField(max_length=15)),
                ('claveAtendedor', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rutCliente', models.IntegerField(primary_key=True, serialize=False)),
                ('dvRutCliente', models.CharField(max_length=1)),
                ('nombreCliente', models.CharField(max_length=20)),
                ('apPaternoCliente', models.CharField(max_length=20)),
                ('apMaternoCliente', models.CharField(blank=True, max_length=20, null=True)),
                ('celularCliente', models.IntegerField(blank=True, null=True)),
                ('telefonoCliente', models.IntegerField(blank=True, null=True)),
                ('emailCliente', models.EmailField(blank=True, max_length=50, null=True)),
                ('direccionCliente', models.CharField(blank=True, max_length=100, null=True)),
                ('creacionCliente', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('rutTecnico', models.IntegerField(primary_key=True, serialize=False)),
                ('dvRutTecnico', models.CharField(max_length=1)),
                ('nombreTecnico', models.CharField(max_length=20)),
                ('apPaternoTecnico', models.CharField(max_length=20)),
                ('apMaternoTecnico', models.CharField(max_length=20)),
                ('celularTecnico', models.IntegerField(blank=True, null=True)),
                ('emailTecnico', models.EmailField(blank=True, max_length=30, null=True)),
                ('nombreUsuarioTecnico', models.CharField(max_length=15)),
                ('claveTecnico', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('idReceta', models.BigAutoField(primary_key=True, serialize=False)),
                ('numeroReceta', models.IntegerField(blank=True, null=True)),
                ('fechaReceta', models.DateField(blank=True, null=True)),
                ('creacionReceta', models.DateTimeField(auto_now_add=True)),
                ('lejosOd', models.CharField(blank=True, max_length=10, null=True)),
                ('lejosOi', models.CharField(blank=True, max_length=10, null=True)),
                ('cercaOd', models.CharField(blank=True, max_length=10, null=True)),
                ('cercaOi', models.CharField(blank=True, max_length=10, null=True)),
                ('dpCerca', models.CharField(blank=True, max_length=10, null=True)),
                ('dpLejos', models.CharField(blank=True, max_length=10, null=True)),
                ('tipoLente', models.CharField(blank=True, max_length=20, null=True)),
                ('institucion', models.CharField(blank=True, max_length=20, null=True)),
                ('doctorOftalmologo', models.CharField(blank=True, max_length=40, null=True)),
                ('linkFotoReceta', models.CharField(blank=True, max_length=200, null=True)),
                ('rutCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('idOrdenTrabajo', models.BigAutoField(primary_key=True, serialize=False)),
                ('fechaOrdenTrabajo', models.DateTimeField(auto_now_add=True)),
                ('valorOrdenTrabajo', models.IntegerField(blank=True, null=True)),
                ('fechaEntregaOrdenTrabajo', models.DateField(blank=True, null=True)),
                ('horaEntregaOrdenTrabajo', models.TimeField(blank=True, null=True)),
                ('lejosDp', models.CharField(blank=True, max_length=10, null=True)),
                ('laboratorioLejos', models.CharField(blank=True, max_length=30, null=True)),
                ('cilLejosOd', models.CharField(blank=True, max_length=10, null=True)),
                ('cilLejosOi', models.CharField(blank=True, max_length=10, null=True)),
                ('gradoLejosOd', models.CharField(blank=True, max_length=10, null=True)),
                ('gradoLejosOi', models.CharField(blank=True, max_length=10, null=True)),
                ('prismaLejosOd', models.CharField(blank=True, max_length=10, null=True)),
                ('prismaLejosOi', models.CharField(blank=True, max_length=10, null=True)),
                ('tipoCristalLejos', models.CharField(blank=True, max_length=25, null=True)),
                ('colorLejos', models.CharField(blank=True, max_length=20, null=True)),
                ('marco', models.CharField(blank=True, max_length=25, null=True)),
                ('altura', models.CharField(blank=True, max_length=25, null=True)),
                ('laboratorioCerca', models.CharField(blank=True, max_length=30, null=True)),
                ('cilCercaOd', models.CharField(blank=True, max_length=10, null=True)),
                ('cilCercaOi', models.CharField(blank=True, max_length=10, null=True)),
                ('gradoCercaOd', models.CharField(blank=True, max_length=10, null=True)),
                ('gradoCercaOi', models.CharField(blank=True, max_length=10, null=True)),
                ('prismaCercaOd', models.CharField(blank=True, max_length=10, null=True)),
                ('prismaCercaOi', models.CharField(blank=True, max_length=10, null=True)),
                ('tipoCristalCerca', models.CharField(blank=True, max_length=25, null=True)),
                ('colorCerca', models.CharField(blank=True, max_length=20, null=True)),
                ('numeroVoucherOrdenTrabajo', models.IntegerField(blank=True, null=True)),
                ('idAbono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.abono')),
                ('idReceta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.receta')),
                ('rutAtendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.atendedor')),
                ('rutCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('idCertificado', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('fechaCertificado', models.DateTimeField(auto_now_add=True)),
                ('valorMarcoLejos', models.IntegerField(blank=True, null=True)),
                ('valorCristalesLejos', models.IntegerField(blank=True, null=True)),
                ('valorMarcoCerca', models.IntegerField(blank=True, null=True)),
                ('valorCristalesCerca', models.IntegerField(blank=True, null=True)),
                ('totalCerca', models.IntegerField(blank=True, null=True)),
                ('totalLejos', models.IntegerField(blank=True, null=True)),
                ('idOrdenTrabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.ordentrabajo')),
                ('idReceta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.receta')),
                ('rutCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='abono',
            name='rutCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optica.cliente'),
        ),
    ]