# -*- coding: utf-8 -*-
from odoo import models, fields

class Proveedor(models.Model):
    _name = 'mantenimiento.proveedor'
    _description = 'Proveedor de Equipos'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string="Descripción")
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo electrónico")
    direccion = fields.Text(string="Dirección")