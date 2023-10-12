from odoo import fields, models,_

class LibrosPrestados(models.Model):
    _name="libros.prestados"

    libro_id = fields.Many2one(
        comodel_name="libro",
    )
    prestatario_id = fields.Many2one(
        comodel_name="prestatario",
    )
    fecha_devolucion = fields.Date()
