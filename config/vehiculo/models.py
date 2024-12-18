from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    MARCA_CHOICE =[
        ('fiat', 'Fiat'),
        ('chevrolet', 'Chevrolet'),
        ('ford', 'Ford'),
        ('toyota', 'Toyota'),   
    ]

    CATEGORIA_CHOICE=[
        ('particular', 'Particular'),
        ('transporte', 'Transporte'),
        ('carga', 'Carga'),
    ]

    #Creando modelo de vehiculo
    marca = models.CharField(max_length=20, choices=MARCA_CHOICE, default='ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICE, default='particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede ver el catalogo de vehiculos"),
        ]

    def __str__(self):
        return f" Marca: {self.marca} --- Modelo: {self.modelo}"
    
    @property
    def condicion_precio(self):
        if self.precio <= 10000:
            return "Bajo"
        elif 10000 < self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"


