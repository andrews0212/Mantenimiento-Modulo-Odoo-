from odoo import models, fields, api

class MantenimientoReparacion(models.Model):
    _name = "mantenimiento.reparacion"
    _description = "Reparaciones de Artículos de Mantenimiento"

    fecha = fields.Date(string="Fecha")
    descripcion = fields.Text(string="Descripción")
    costo = fields.Float(string="Costo")
    tecnico = fields.Char(string="Técnico")
    articulo_id = fields.Many2one('mantenimiento.articulo', string="Artículo")
    equipo_id = fields.Many2one('mantenimiento.equipo', string="Equipo", compute="_compute_equipo_id", store=True)

    @api.depends('articulo_id')
    def _compute_equipo_id(self):
        for record in self:
            record.equipo_id = record.articulo_id.equipo_id if record.articulo_id else False