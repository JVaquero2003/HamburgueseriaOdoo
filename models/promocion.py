# -*- coding: utf-8 -*-

from odoo import models, fields, api

class promocion(models.Model):
    _name = 'hamburgueseria.promocion'
    _descripcion = 'Permite definir las características de una promoción'
    name=fields.Char(string='Nombre')
    descripcion=fields.Text(string='Descripción')

    
    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    precio1 = fields.Float(string='Precio1')
    precio2 = fields.Float(string='Precio2')
    media_precio = fields.Float(string='Media Precio')
    tienda_id = fields.Many2one('hamburgueseria.tienda', string="Tienda")
    hamburguesa_ids = fields.Many2many('hamburgueseria.hamburguesa', string="Hamburguesas")
    bebida_ids = fields.Many2many('hamburgueseria.bebida', string="Bebidas")


    @api.onchange('precio1', 'precio2')
    def _onchange_media_precio(self):
        self.media_precio = (self.precio1 + self.precio2) / 2