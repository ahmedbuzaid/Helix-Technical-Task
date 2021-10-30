# -*- coding: utf-8 -*-
{
    'name': 'Clash Of Clans',
    'version': '1.0',
    'category': 'any',
    'summary': 'Centralize clash of clans troops attributes',
    'description': """
                This module defines clash of clans game troops attributes and uses
                factors of BI to facilitate data representation and analysis.
                """,
    'website': 'https://www.helix.com',
    'depends': [
        'base',
    ],
    'images': [
        'static/src/img/default_image.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/clash_of_clans_views.xml',
        'data/clash_of_clans_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
