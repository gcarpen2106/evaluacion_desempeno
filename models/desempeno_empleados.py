# evaluacion_empleados/models/desempeno_empleados.py

from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluacion de Desempeno'
    _inherit = ['mail.thread']

    name = fields.Char(string='Titulo', required=True, tracking=True)
    comentarios = fields.Text(string='Comentarios', tracking=True)
    fechaEvaluacion = fields.Date(string='Fecha de Evaluacion', required=True)
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
    ], string='Estado', default='draft')

    empleadoAsignado = fields.Many2one(
        "hr.employee", 
        string="Empleado Asignado",
        required=True,
        tracking=True,
        ondelete='restrict'
    )

    def iniciar_evaluacion(self):
        self.state = 'in_progress'

    def finalizar_evaluacion(self):
        self.state = 'done'

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'completed':
            self.priority = 0

    @api.constrains('score')
    def _check_punctuation(self):
        for record in self:
            if record.score > 10 or record.score < 0:
                raise ValidationError(_('La puntuación debe estar entre 0 y 10'))