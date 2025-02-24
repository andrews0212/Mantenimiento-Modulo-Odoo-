# -*- coding: utf-8 -*-
from odoo import models, fields

class EquipmentCategory(models.Model):
    _name = 'mantenimiento.categoria'
    _description = 'Categoría de Equipos'

    name = fields.Char(string="Nombre categoría", required=True)
    description = fields.Text(string="Descripción")