from odoo import models, fields


class ProductCategory(models.Model):
     _name = 'product_category'

     name = fields.Char(string="Nombre", required=True)
     product_type_id = fields.Many2one(comodel_name="product_type", string="Tipo", required=True)
     description = fields.Text(string="Descripcion")
     state = fields.Selection([('activo', 'Activo'), ('desactivado', 'Desactivado')])