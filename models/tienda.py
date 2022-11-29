# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tienda(models.Model):
    _name = 'hamburgueseria.tienda'
    _descripcion = 'Permite definir las características de una tienda'
    name=fields.Char(string='Nombre')
    descripcion=fields.Text(string='Descripción')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    web = fields.Char(string='Web')


    promocion_ids = fields.One2many('hamburgueseria.promocion', 'tienda_id', string="Promociones")