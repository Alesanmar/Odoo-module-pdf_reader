# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "PDF Reader",
    'summary': "Let an user see PDF archives",
    'category': 'Productivity',
    'version': '1.0',
    'depends': ['base_setup','mail'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/webclient_templates.xml',
        'views/document.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}