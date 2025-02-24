# -*- coding: utf-8 -*-
from odoo import models, fields

class MantenimientoOrden(models.Model):
    _name = "mantenimiento.orden"
    _description = "Orden de Mantenimiento"

    tipo_mantenimiento = fields.Selection([
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo')
    ], string="Tipo de Mantenimiento", required=True)

    fecha_programada = fields.Date(string="Fecha Programada")
    fecha_realizacion = fields.Date(string="Fecha de Realización")
    equipo_id = fields.Many2one('mantenimiento.equipo', string="Equipo", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='pendiente')
    descripcion = fields.Text(string="Descripción")