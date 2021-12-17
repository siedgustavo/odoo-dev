# -*- coding: utf-8 -*-

from odoo import models, fields, api, http
from odoo.exceptions import ValidationError
from odoo.http import request

 class sc_product(models.Model):
     _name = 'sc_product'

     name = fields.Char('Nombre')
     description = fields.Text('Descripcion')
     product_category_id = fields.many2one('sc_product_category', 'Categoria')
     price = fields.Float('Precio')
     state = fields.Selection([('activo','Activo'),('desactivado','Desactivado')])


class sc_product_category(models.Model):
    _name = 'sc_product_category'

    name = fields.Char('Nombre')
    product_type_id = fields.many2one('sc_product_type', 'Tipo')
    description = fields.Text('Descripcion')
    state = fields.Selection([('activo', 'Activo'), ('desactivado', 'Desactivado')])


class sc_product_type(models.Model):
    _name = 'sc_product_type'

    name = fields.Char('Nombre')
    description = fields.Text('Descripcion')
    state = fields.Selection([('activo', 'Activo'), ('desactivado', 'Desactivado')])
