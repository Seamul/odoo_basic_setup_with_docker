{
    'name': 'My Custom Module',
    'version': '16.0.1.0.0',
    'summary': 'A custom module for CRUD operations',
    'description': 'This module demonstrates CRUD operations in Odoo 16.',
    'author': 'Seamul Islam',
    'website': 'http://www.example.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'views/my_model_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
