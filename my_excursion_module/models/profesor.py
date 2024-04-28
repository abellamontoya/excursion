from odoo import models, fields


class Profesor(models.Model):
    _name = 'profesor'
    _description = 'Profesores'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    especialidad = fields.Char(string='Especialidad')
    excursion_ids = fields.Many2many('excursion', string='Excursiones')
