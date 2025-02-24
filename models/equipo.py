# -*- coding: utf-8 -*-
from odoo import models, fields

class Equipo(models.Model):
    _name = "mantenimiento.equipo"
    _description = "Equipos de mantenimiento"

    name = fields.Char(string="Nombre", required=True)
    category_id = fields.Many2one("mantenimiento.categoria", string="Categoría")
    description = fields.Text(string="Descripción")
    ubicacion = fields.Char(string="Ubicación")
    numeroSerie = fields.Char(string="Número de Serie")
    proveedor_id = fields.Many2one("mantenimiento.proveedor", string="Proveedor")