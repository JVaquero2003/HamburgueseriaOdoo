from odoo import models, fields, api

class hamburguesa(models.Model):
    _name = 'hamburgueseria.hamburguesa'
    _descripcion = 'Permite definir las características de una hamburguesa'
    name=fields.Char(string='Nombre')
    descripcion=fields.Text(string='Descripción')

    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    promocion_ids = fields.Many2many('hamburgueseria.promocion', string="Promociones")