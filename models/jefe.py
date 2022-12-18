from odoo import models, fields, api
from . import personal

class jefe(models.Model):
    _name = 'hamburgueseria.jefe'
    _descripcion = 'Permite definir las características de un jefe'
    _inherit = 'hamburgueseria.personal'

    
    rango = fields.Char(string='Rango')
    # Añadimos el campo para la relación con el empleado
    empleado_id = fields.Many2one('hamburgueseria.empleado', string='Empleado')