# -*- coding: utf-8 -*-
{
    'name' : 'Fleet Custom Dashboard',
    'version' : '17.0.0.1',
    'summary': 'all about Fleet modle Dashboard',
    'sequence': -1,
    'description': """show over all data of Fleet""",
    'category': 'Fleet Dashboard',
    'depends' : ['board'],
    'data': [
        'views/fleet_dashboard.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'fleet_custom_dashboard/static/src/components/**/*.js',
            'fleet_custom_dashboard/static/src/components/**/*.xml',
            'fleet_custom_dashboard/static/src/components/**/*.scss',
        ],
    },
}
