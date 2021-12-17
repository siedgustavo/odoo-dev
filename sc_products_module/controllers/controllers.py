# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

 class sc_product_controller(http.Controller):
     @http.route('/sc_products_module/', auth='public', website=True)
     def index(self, **kw):
         return "SiedCloud - Products - " + request.params["testParam"]

     @http.route('/sc_products_module/products/', auth='user')
     def list(self, **kw):
         return http.request.render('sc_products_module.listing', {
             'root': '/sc_products_module/products',
             'objects': http.request.env['sc_products_module.sc_product'].search([]),
         })

     @http.route('/sc_products_module/products/<model("sc_products_module.sc_product"):obj>/', auth='user')
     def object(self, product, **kw):
         return http.request.render('sc_products_module.sc_product', {
             'product': product
         })