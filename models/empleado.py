from odoo import models, fields, api
from . import personal

class empleado(models.Model):
    _name = 'hamburgueseria.empleado'
    _descripcion = 'Permite definir las características de un empleado'
    _inherit = 'hamburgueseria.personal'

    jornada = fields.Char(string='Jornada')
    # Añadimos el campo para la relación con el jefe
    jefe_ids = fields.One2many('hamburgueseria.jefe','empleado_id', string='Jefe')



