from odoo import models, fields


class Excursion(models.Model):
    _name = 'excursion'
    _description = 'Excursiones para colegios'

    nombre = fields.Char(string='Nombre', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    destino = fields.Char(string='Destino', required=True)
    descripcion = fields.Text(string='Descripción')
    alumnos_ids = fields.Many2many('alumno', string='Alumnos')
    profesores_ids = fields.Many2many('profesor', string='Profesores')