# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EquipmentCategory(models.Model):
    _name = 'equipo.categoria'  # Nombre correcto del modelo
    _description = 'Categoría de Equipos'

    name = fields.Char(string="Nombre categoría", required=True)
    description = fields.Text(string="Descripción")

class Proveedor(models.Model):
    _name = 'equipo.proveedor'  # Nombre más claro para el modelo
    _description = 'Proveedor de Equipos'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string="Descripción")  # Cambié a Text para mayor longitud
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo electrónico")
    direccion = fields.Text(string="Dirección")

class Equipo(models.Model):
    _name = "mantenimiento.equipo"
    _description = "Equipos de mantenimiento"

    name = fields.Char(string="Nombre", required=True)
    category_id = fields.Many2one("equipo.categoria", string="Categoría")
    description = fields.Text(string="Descripción")
    ubicacion = fields.Char(string="Ubicación")
    numeroSerie = fields.Char(string="Número de Serie")
    proveedor_id = fields.Many2one("equipo.proveedor", string="Proveedor")  # Cambié a proveedor_id para seguir la convención
