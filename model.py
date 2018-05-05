# -*- coding: utf-8 -*- 

from odoo import models, fields


class CitaRecord(models.Model):

    _name = "cita.cita"
    cita = fields.Char(string='Cita', required=True)
    autor = fields.Char(string='Autor de la cita', required=True)
    orden = fields.Integer(string='Orden de visualización')
    fecha_visualizacion = fields.Date(string="Fecha de visualización")