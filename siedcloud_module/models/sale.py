from odoo import models, fields


class Sale(models.Model):
     _name = 'sale'

     customer_id = fields.Many2one(comodel_name="customer", string="Cliente", required=True)
     product_ids = fields.Many2many("product", string="Productos")
     state = fields.Selection([('pending','Pendiente'),('finalized','Finalizada')])


     def boton_finalizar(self):
          self.state = "finalized"
