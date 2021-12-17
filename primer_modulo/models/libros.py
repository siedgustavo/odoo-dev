from odoo import models, fields


#Creando un modelo (tabla de la base de datos) a partir de una clase
class Libros(models.Model):
    _name = 'libros' #nombre de la tabla que se va a generar

    name = fields.Char(string="Nombre del libro") #nombre del campo que es de tipo cadena
    editorial = fields.Char(string="Editorial")
