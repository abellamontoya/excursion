{
    'name': 'Gestión de Excursiones Escolares',
    'summary': 'Módulo para la gestión de excursiones escolares en Odoo',
    'version': '1.0',
    'author': 'Pol Abella',
    'website': 'https://mynameispolabellamontoya.com',
    'category': 'Educación',
    'depends': ['base'],
    'data': [
        'views/excursion_views.xml',
        'views/alumno_views.xml',
        'views/profesor_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}