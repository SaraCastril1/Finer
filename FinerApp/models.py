from asyncio.windows_events import NULL
from distutils import text_file
from django.db import models
from django import forms


# iterable
Tipo_empresa =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class EMPRESA(models.Model):
   empresa_id = models.CharField(primary_key= True, max_length=15)
   nombre = models.CharField(max_length=50)
   contraseña = models.CharField(max_length=20)
   #tipo_empresa_id = forms.ChoiceField(choices = Tipo_empresa)
   #cantidad_productos = models.SmallIntegerField()
   margen_contribucion_Total = models.FloatField()
   

   
   
   
   
class PRODUCTO(models.Model): #LIBROS
   producto_id = models.CharField(primary_key= True, max_length=15)
   empresa_id = models.ForeignKey(EMPRESA, on_delete=models.CASCADE, 
                                  null = False, blank = False) #Llave foranea 
   nombre = models.CharField(max_length=30)
   c_v_u = models.FloatField(default=0) 
   p_v_u = models.FloatField(default=0)
   participacion_ventas = models.FloatField()
   
   
class COSTO_VARIABLE(models.Model):
   producto_id = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
   concepto = models.CharField(max_length=50) 
   unidad_compra = models.FloatField()
   precio_compra = models.SmallIntegerField()
   unidades_utilizada = models.FloatField()
   factor = models.FloatField()
   margen_contribucion_peso = models.FloatField()
   margen_contribucion_porcentaje = models.IntegerField()
   
   
class Meta:
   model = EMPRESA

   fields = [
      'empresa_id',
      'nombre',
      'contraseña',
      'tipo_empresa_id',
      'cantidad_productos',
      'margen_contribucion_Total',
   ]

   labels = {
      'empresa_id': 'Empresa ID',
      'nombre': 'Nombre',
      'contraseña': 'Contraseña',
      'tipo_empresa_id': 'Tipo de empresa',
      'cantidad_productos': 'Cantidad de productos',
      'margen_contribucion_Total': 'Margen de contribución TOTAL',
   }

   widgets = {
      'empresa_id':forms.TextInput(),
      'nombre':forms.TextInput(),
      'contraseña':forms.TextInput(),
      'tipo_empresa_id':forms.Select(),
      'cantidad_productos':forms.Select(),
      'margen_contribucion_Total': forms.TextInput(attrs={'required': False}),
      
   }
