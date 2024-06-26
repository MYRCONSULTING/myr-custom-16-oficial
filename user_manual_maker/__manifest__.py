# -*- coding:utf-8 -**-
###############################################################################
#
#   Copyright (C) 2004-today Wakamole Code
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   For Module Support : amadeobarush@gmail.com
###############################################################################

{
    'name': 'User Manual Maker',
    'version': '16.0.1.0.1',
    'category': 'Productivity',
    'description': 'Module to create user manuals',
    'summary': 'Module to create user manuals',
    'depends': ['base','mail'],
    'data': [
        'data/data_init.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/usermanual_maker_views.xml',
        'views/usermanual_seccion_views.xml',
        'views/usermanual_step_views.xml',
        'views/usermanual_comment_views.xml',
        'views/usermanual_tipificacion_views.xml',
        'report/report_manual.xml',
        ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'Wakamole Code',
    'maintainer': 'Wakamole Code Team',
    'license': 'AGPL-3',
}
