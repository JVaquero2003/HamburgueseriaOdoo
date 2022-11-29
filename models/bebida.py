from odoo import models, fields, api

class bebida(models.Model):
    _name = 'hamburgueseria.bebida'
    _descripcion = 'Permite definir las características de una bebida'
    name=fields.Char(string='Nombre')
    descripcion=fields.Text(string='Descripción')
    nombre = fields.Char(string='Nombre')

    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    promocion_ids = fields.Many2many('hamburgueseria.promocion', string="Promociones")