# evaluacion_desempeño/__manifest__.py

{
    'name': 'Evaluacion Desempeño',
    'version': '1.0',
    'summary': 'Módulo para gestionar las evaluaciones de desempeño de los empleados',
    'category': 'Productivity',
    'author': 'Gonzalo Carretero',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail','hr'],
    'icon': '/evaluacion_desempeno/static/description/icon53.png',
    'data': [
        'views/evaluacion_desempeno.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """
        Módulo de Odoo para gestionar las evaluaciones de desempeño de los empleados,
        incluyendo vistas Kanban y formulario detallado.
    """,''
    'assets': {
        'web.assets_backend': [
            '/evaluacion_desempeno/static/src/css/styles.css',
        ],
    },
}
