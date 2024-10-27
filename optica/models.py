import os
from django.db import models

class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True, verbose_name="RUN Cliente") 
    dvRutCliente = models.CharField(max_length=1, verbose_name="Digito")
    nombreCliente = models.CharField(max_length=20, verbose_name="Nombre")
    apPaternoCliente = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apMaternoCliente = models.CharField(max_length=20, null=True, blank=True, verbose_name="Apellido Materno")
    celularCliente = models.IntegerField(null=True, blank=True, verbose_name="Celular")
    telefonoCliente = models.IntegerField(null=True, blank=True, verbose_name="Teléfono")
    emailCliente = models.EmailField(max_length=50, null=True, blank=True, verbose_name="Correo Electrónico")
    direccionCliente = models.CharField(max_length=100, null=True, blank=True, verbose_name="Dirección")
    creacionCliente = models.DateTimeField(auto_now_add=True, verbose_name="Creado el día")

    def __str__(self):
        return f"{self.rutCliente}"

class Atendedor(models.Model): 
    rutAtendedor = models.IntegerField(primary_key=True, verbose_name="RUN Atendedor") 
    dvRutAtendedor = models.CharField(max_length=1, verbose_name="Digito")
    nombreAtendedor = models.CharField(max_length=20, verbose_name="Nombre")
    apPaternoAtendedor = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apMaternoAtendedor = models.CharField(max_length=20, verbose_name="Apellido Materno")
    celularAtendedor = models.IntegerField(null=True, blank=True, verbose_name="Celular")
    emailAtendedor = models.EmailField(max_length=30, null=True, blank=True, verbose_name="Correo Electrónico")  
    nombreUsuarioAtendedor = models.CharField(max_length=15, verbose_name="Nombre de Usuario") #Nombre de usuario
    claveAtendedor = models.CharField(max_length=15, verbose_name="Clave") #Clave

    def __str__(self):
        return f"{self.nombreAtendedor} {self.apPaternoAtendedor} {self.apMaternoAtendedor}"

class Tecnico(models.Model): 
    rutTecnico = models.IntegerField(primary_key=True, verbose_name="RUN Técnico") 
    dvRutTecnico = models.CharField(max_length=1, verbose_name="Digito")
    nombreTecnico = models.CharField(max_length=20, verbose_name="Nombre")
    apPaternoTecnico = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apMaternoTecnico = models.CharField(max_length=20, verbose_name="Apellido Materno")
    celularTecnico = models.IntegerField(null=True, blank=True, verbose_name="Celular")
    emailTecnico = models.EmailField(max_length=30, null=True, blank=True, verbose_name="Correo Electrónico")  
    nombreUsuarioTecnico = models.CharField(max_length=15, verbose_name="Nombre de Usuario") #Nombre de usuario
    claveTecnico = models.CharField(max_length=15, verbose_name="Clave") #Clave

    def __str__(self):
        return f"{self.nombreTecnico} {self.apPaternoTecnico} {self.apMaternoTecnico}"

class Administrador(models.Model): 
    rutAdministrador = models.IntegerField(primary_key=True, verbose_name="RUN Administrador") 
    dvRutAdministrador = models.CharField(max_length=1, verbose_name="Digito")
    nombreAdministrador = models.CharField(max_length=20, verbose_name="Nombre")
    apPaternoAdministrador = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apMaternoAdministrador = models.CharField(max_length=20, verbose_name="Apellido Materno")
    celularAdministrador = models.IntegerField(null=True, blank=True, verbose_name="Celular")
    emailAdministrador = models.EmailField(max_length=50, null=True, blank=True, verbose_name="Correo Electrónico")   
    nombreUsuarioAdministrador = models.CharField(max_length=20, verbose_name="Nombre de Usuario") #Nombre de usuario
    claveAdministrador = models.CharField(max_length=20, verbose_name="Clave") #Clave

    def __str__(self):
        return f"{self.nombreAdministrador} {self.apPaternoAdministrador} {self.apMaternoAdministrador}"
    
class Receta(models.Model):
    idReceta = models.BigAutoField(primary_key=True, verbose_name="ID receta")
    rutCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="RUN Cliente")
    rutAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Administrador")
    rutTecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Técnico")
    rutAtendedor = models.ForeignKey(Atendedor, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Atendedor") 

    dvRutCliente = models.CharField(max_length=1, null=True, blank=True, verbose_name="Dígito")
    nombreCliente = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nombre")
    apPaternoCliente = models.CharField(max_length=20, null=True, blank=True, verbose_name="Apellido Paterno")
    apMaternoCliente = models.CharField(max_length=20, null=True, blank=True, verbose_name="Apellido Materno")
    celularCliente = models.IntegerField(null=True, blank=True, verbose_name="Celular")
    telefonoCliente = models.IntegerField(null=True, blank=True, verbose_name="Teléfono")
    

    numeroReceta = models.IntegerField(null=True, blank=True, verbose_name="Número de Receta")
    fechaReceta = models.DateField(null=True, blank=True, verbose_name="Fecha Receta") 
    creacionReceta = models.DateTimeField(auto_now_add=True, verbose_name="Creado el día")
    imagenReceta = models.ImageField(upload_to='imagenes/', null=True, blank=True, verbose_name="Imagen")
    
    lejosOdEsfera = models.CharField(max_length=10, null=True, blank=True, verbose_name="Esfera")
    lejosOdCilindro = models.CharField(max_length=10, null=True, blank=True, verbose_name="Cilindro")
    lejosOdEje = models.CharField(max_length=10, null=True, blank=True, verbose_name="Eje")
    
    lejosOiEsfera = models.CharField(max_length=10, null=True, blank=True, verbose_name="Esfera")
    lejosOiCilindro = models.CharField(max_length=10, null=True, blank=True, verbose_name="Cilindro")
    lejosOiEje = models.CharField(max_length=10, null=True, blank=True, verbose_name="Eje")
    
    dpLejos = models.CharField(max_length=10, null=True, blank=True, verbose_name="Distancia Pupilar")

    cercaOdEsfera = models.CharField(max_length=10, null=True, blank=True, verbose_name="Esfera")
    cercaOdCilindro = models.CharField(max_length=10, null=True, blank=True, verbose_name="Cilindro")
    cercaOdEje = models.CharField(max_length=10, null=True, blank=True, verbose_name="Eje")

    cercaOiEsfera = models.CharField(max_length=10, null=True, blank=True, verbose_name="Esfera")
    cercaOiCilindro = models.CharField(max_length=10, null=True, blank=True, verbose_name="Cilindro")
    cercaOiEje = models.CharField(max_length=10, null=True, blank=True, verbose_name="Eje")

    dpCerca = models.CharField(max_length=10, null=True, blank=True, verbose_name="Distancia Pupilar")
   
    tipoLente = models.CharField(max_length=20, null=True, blank=True, verbose_name="Tipo de Lente")
    institucion = models.CharField(max_length=20, null=True, blank=True, verbose_name="Institucion")
    doctorOftalmologo = models.CharField(max_length=40, null=True, blank=True, verbose_name="Médico Oftalmología")
    observacionReceta = models.CharField(max_length=300, null=True, blank=True, verbose_name="Observaciones")

    def __str__(self):
        return f"{self.idReceta}"
    
    def save(self, *args, **kwargs):
        # Verifica si ya hay una imagen antes de guardar la nueva
        try:
            this = Receta.objects.get(idReceta=self.idReceta)
            if this.imagenReceta != self.imagenReceta and this.imagenReceta:
                # Si la imagen ha cambiado, eliminar la anterior
                if os.path.isfile(this.imagenReceta.path):
                    os.remove(this.imagenReceta.path)
        except Receta.DoesNotExist:
            pass  # El objeto no existe aún (primera vez que se guarda)
        
        # Guarda normalmente después de eliminar la imagen anterior
        super().save(*args, **kwargs)
    
    
    def delete(self, using=None, keep_parents=False):
    # Borra la imagen asociada si existe
        if self.imagenReceta:
            self.imagenReceta.storage.delete(self.imagenReceta.name)

    # Llamar al método delete del modelo base pasando los argumentos correctos
        super().delete(using=using, keep_parents=keep_parents)
    

class OrdenTrabajo(models.Model): 
    idOrdenTrabajo = models.BigAutoField(primary_key=True, verbose_name="ID Orden de Trabajo")
    rutCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="RUN Cliente") 
    
    rutAtendedor = models.ForeignKey(Atendedor, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Atendedor") 
    rutTecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Técnico")
    rutAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Administrador")

    idReceta = models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="ID Receta")
    numeroOrdenTrabajo = models.IntegerField(null=True, blank=True, verbose_name="Total (Lejos)") 
    fechaOrdenTrabajo = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Orden de Trabajo")
    fechaEntregaOrdenTrabajo = models.DateField(null=True, blank=True, verbose_name="Fecha Entrega") 
    horaEntregaOrdenTrabajo = models.TimeField(null=True, blank=True, verbose_name="Hora de Entrega")
 
    laboratorioLejos = models.CharField(max_length=30, null=True, blank=True, verbose_name="Laboratorio (Lejos)")
    gradoLejosOd = models.CharField(max_length=10, null=True, blank=True, verbose_name="Grado Lejos OD")
    gradoLejosOi = models.CharField(max_length=10, null=True, blank=True, verbose_name="Grado Lejos OI")
    prismaLejosOd = models.CharField(max_length=10, null=True, blank=True, verbose_name="Prisma Lejos OD")
    prismaLejosOi = models.CharField(max_length=10, null=True, blank=True, verbose_name="Prisma Lejos OI")
    adicionLejosOd = models.CharField(max_length=10, null=True, blank=True, verbose_name="Adición Lejos OD")
    adicionLejosOi = models.CharField(max_length=10, null=True, blank=True, verbose_name="Adición Lejos OI")    
    tipoCristalLejos = models.CharField(max_length=25, null=True, blank=True, verbose_name="Tipo de Cristal (Lejos)")
    colorCristalLejos = models.CharField(max_length=20, null=True, blank=True, verbose_name="Color (Lejos)")
    marcoLejos = models.CharField(max_length=25, null=True, blank=True, verbose_name="Marco (Lejos)")
    valorMarcoLejos = models.IntegerField(null=True, blank=True, verbose_name="Valor Marco (Lejos)") 
    valorCristalesLejos = models.IntegerField(null=True, blank=True, verbose_name="Valor Cristal (Lejos)") 
    totalLejos = models.IntegerField(null=True, blank=True, verbose_name="Total (Lejos)") 
    altura = models.CharField(max_length=25, null=True, blank=True, verbose_name="Altura")
    laboratorioCerca = models.CharField(max_length=30, null=True, blank=True, verbose_name="Laboratotio (Cerca)")
    gradoCercaOd = models.CharField(max_length=10, null=True, blank=True, verbose_name="Grado Cerca OD")
    gradoCercaOi = models.CharField(max_length=10, null=True, blank=True, verbose_name="Grado Cerca OI")
    prismaCercaOd = models.CharField(max_length=10, null=True, blank=True, verbose_name="Prisma Cerca OD")
    prismaCercaOi = models.CharField(max_length=10, null=True, blank=True, verbose_name="Prisma Cerca OI")
    adicionCercaOd = models.CharField(max_length=10, null=True, blank=True, verbose_name="Adición Cerca OD")
    adicionCercaOi = models.CharField(max_length=10, null=True, blank=True, verbose_name="Adición Cerca OI")
    tipoCristalCerca = models.CharField(max_length=25, null=True, blank=True, verbose_name="Tipo de Cristal (Cerca)")
    colorCristalCerca = models.CharField(max_length=20, null=True, blank=True, verbose_name="Color (Cerca)")
    marcoCerca = models.CharField(max_length=25, null=True, blank=True, verbose_name="Marco (Cerca)")
    valorMarcoCerca = models.IntegerField(null=True, blank=True, verbose_name="Valor Marco (Cerca)") 
    valorCristalesCerca = models.IntegerField(null=True, blank=True, verbose_name="Valor Cristal (Cerca)") 
    totalCerca = models.IntegerField(null=True, blank=True, verbose_name="Total (Cerca)")     
    totalOrdenTrabajo= models.IntegerField(null=True, blank=True, verbose_name="Total") 
    numeroVoucherOrdenTrabajo = models.IntegerField(null=True, blank=True, verbose_name="Número de Voucher")
    observacionOrdenTrabajo = models.CharField(max_length=300, null=True, blank=True, verbose_name="Observaciones")


    def __str__(self):
        return f"{self.numeroOrdenTrabajo} {self.fechaOrdenTrabajo} {self.totalOrdenTrabajo}"

class Abono(models.Model): 
    idAbono = models.AutoField(primary_key=True, default=1, verbose_name="ID Abono")
    idOrdenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, verbose_name="ID Orden de Trabajo")
    rutCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="RUN Cliente") 
   
    rutAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Administrador")
    rutTecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Técnico")
    rutAtendedor = models.ForeignKey(Atendedor, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Atendedor") 

    fechaAbono = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Abono")
    valorAbono = models.IntegerField(null=True, blank=True, verbose_name="Valor Abono")
    saldo = models.IntegerField(null=True, blank=True, verbose_name="Saldo")
    formaPagoAbono = models.CharField(max_length=10, null=True, blank=True, verbose_name="Forma de pago")
    numeroVoucherAbono = models.IntegerField(null=True, blank=True, verbose_name="Número de Voucher")
    numeroAbono = models.IntegerField(null=True, blank=True, verbose_name="Abono Número")
    

    def __str__(self):
        return f"{self.fechaAbono} {self.valorAbono}"


class Certificado(models.Model): 
    idCertificado = models.AutoField(primary_key=True, default=1, verbose_name="ID Certificado")
    idOrdenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, verbose_name="ID Orden de Trabajo") 
    rutCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="RUN Cliente") 

    rutTecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Técnico") 
    rutAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Administrador")
    rutAtendedor = models.ForeignKey(Atendedor, on_delete=models.CASCADE, null=True, blank=True, verbose_name="RUN Atendedor") 

    idReceta = models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="ID Receta") 
    fechaCertificado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Certificado")
    
    def __str__(self):
        return f"{self.rutCliente} {self.fechaCertificado}"
    
    
