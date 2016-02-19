# -*- coding: utf-8 -*-

{
    'name': 'Open Academy',
    'version': '0.1',
    'depends': ['base'],
    'summary': 'Ejemplo para practica en construccion de modulos',
    'description': """
Titulo.
======================================== 

Contenido:
------------
    - Ejemplo

If you need to manage your meetings, you should install the Example module.
    """,
    'author': 'Pistacho',
    'category': 'Base',#como buscarlo en la tienda de distribucion de modulos
    'website': 'https://www.odoo.com/page/crm',
    'demo': ['calendar_demo.xml'],#para datos de prueba
    'data': ['openacademy.xml'],
    'qweb': [],# para hacer reportes
    'test': [        
    ], # para hacer pruebas automaticas
    'installable': True,# para permitir que se instale solo o atravez de otro
    'application': True,
    'auto_install': False,
}
