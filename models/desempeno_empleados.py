# evaluacion_empleados/models/desempeno_empleados.py

from odoo import models, fields, api

class DesempenoEmpleados(models.Model):

    _name = 'desempeno.empleados'
    _description = 'Tarea de desempeno'
    _inherit = ['mail.thread']

    name  = fields.Char(string='Titulo', required=True , tracking=True)
    description  = fields.Text(string='Comentarios', tracking=True)
    date = fields.Date(string='Fecha de Evaluacion', required=True)
    score = fields.Integer(
        string="Puntuacion",
        required=True,
        tracking=True,
        help="Puntuacion del empleado"
    )
    
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Progreso'),
        ('done', 'Hecho'),
    ], string='Estado', default='draft',tracking=True)

    assigned_to = fields.Many2one(
        "hr.employee", 
        string="Empleado Asignado",
        required=True,
        tracking=True,
        ondelete='restrict'
    )


    @api.constrains('punctuation')
    def _check_punctuation(self):
        for record in self:
            if record.punctuation > 10 or record.punctuation < 0:
                raise ValidationError(_('La puntuación debe estar entre 0 y 10'))
