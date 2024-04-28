from odoo import models, fields


class Alumno(models.Model):
    _name = 'alumno'
    _description = 'Alumnos'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    alergias = fields.Text(string='Alergias')
    excursion_ids = fields.Many2many('excursion', string='Excursiones')
