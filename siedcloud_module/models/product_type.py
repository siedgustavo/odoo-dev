from odoo import models, fields


class ProductType(models.Model):
     _name = 'product_type'

     name = fields.Char(string="Nombre", required=True)
     description = fields.Text('Descripcion', required=True)
     state = fields.Selection([('activo', 'Activo'), ('desactivado', 'Desactivado')])