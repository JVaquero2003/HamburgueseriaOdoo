from odoo import models, fields, api

class personal(models.Model):
    _name = 'hamburgueseria.personal'
    _descripcion = 'Permite definir las características de un empleado'

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    fecha_contratacion = fields.Date(string='Fecha de contratación')
    salario = fields.Float(string='Salario')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')