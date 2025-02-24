# -*- coding: utf-8 -*-
from odoo import models, fields

class MantenimientoReparacion(models.Model):
    _name = "mantenimiento.reparacion"
    _description = "Reparaciones de Artículos de Mantenimiento"

    fecha = fields.Date(string="Fecha")
    descripcion = fields.Text(string="Descripción")
    costo = fields.Float(string="Costo")
    tecnico = fields.Char(string="Técnico")
    articulo_id = fields.Many2one('mantenimiento.articulo', string="Artículo")