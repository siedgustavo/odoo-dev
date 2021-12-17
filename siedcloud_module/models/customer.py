from odoo import models, fields


class Customer(models.Model):
     _name = 'customer'

     name = fields.Char(string="Nombre", required=True)
     address = fields.Char(string="Dirección", required=True)
     city = fields.Char(string="Ciudad", required=True)
     zip_code = fields.Char(string="Código Postal", required=True)
     province = fields.Char(string="Provincia", required=True)
     country = fields.Char(string="Pais", required=True)
     identification_type = fields.Char(string="Tipo Identificación", required=True)
     identification_number = fields.Char(string="Numero Identificación", required=True)
     contact = fields.Char(string="Contacto", required=True)
     contact_number = fields.Char(string="Numero de contacto", required=True)
     contact_email = fields.Char(string="Email de contacto", required=True)
     state = fields.Selection([('activo','Activo'),('desactivado','Desactivado')], required=True)