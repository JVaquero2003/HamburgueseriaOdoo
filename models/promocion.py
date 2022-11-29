# -*- coding: utf-8 -*-

from odoo import models, fields, api

class promocion(models.Model):
    _name = 'hamburgueseria.promocion'
    _descripcion = 'Permite definir las características de una promoción'
    name=fields.Char(string='Nombre')
    descripcion=fields.Text(string='Descripción')

    
    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    tienda_id = fields.Many2one('hamburgueseria.tienda', string="Tienda")
    hamburguesa_ids = fields.Many2many('hamburgueseria.hamburguesa', string="Hamburguesas")
    bebida_ids = fields.Many2many('hamburgueseria.bebida', string="Bebidas")