# filepath: /C:/Users/ANDREWS/OneDrive/Escritorio/odoo_16_bluehat/addons/mantenimiento/models/MantenimientoArticulo.py
# -*- coding: utf-8 -*-
from odoo import models, fields

class MantenimientoArticulo(models.Model):
    _name = "mantenimiento.articulo"
    _description = "Artículos de Mantenimiento"

    equipo_id = fields.Many2one('mantenimiento.equipo', string="Equipo", required=True)
    reparaciones_ids = fields.One2many('mantenimiento.reparacion', 'articulo_id', string="Historial de Reparaciones")