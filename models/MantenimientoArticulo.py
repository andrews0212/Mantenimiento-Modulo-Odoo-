# -*- coding: utf-8 -*-
from odoo import models, fields

class MantenimientoArticulo(models.Model):
    _name = "mantenimiento.articulo"
    _description = "Artículos de Mantenimiento"

    name = fields.Char(string="Nombre", required=True)
    reparaciones_ids = fields.One2many('mantenimiento.reparacion', 'articulo_id', string="Historial de Reparaciones")