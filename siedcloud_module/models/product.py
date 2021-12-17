from odoo import models, fields


class Product(models.Model):
     _name = 'product'

     name = fields.Char(string="Nombre de producto", required=True)
     description = fields.Text(string="Description", required=True)
     product_category_id = fields.Many2one(comodel_name="product_category", string="Categoria", required=True)
     price = fields.Float(string="Precio")
     state = fields.Selection([('activo','Activo'),('desactivado','Desactivado')])