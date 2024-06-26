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
from odoo import fields, models, api, exceptions

import logging
logger = logging.getLogger(__name__)

class UserManual(models.Model):

    _name = "user_manual_maker"
    _description = 'UMM Module to create user manuals'
    _inherit = ['mail.thread', 'mail.activity.mixin','image.mixin']

    name = fields.Char(string="Manual name", required="True")
    description = fields.Char(string="Description", required="True")
    
    status = fields.Selection([
        ('1','Draft'),
        ('2','Revision'),
        ('3','Approved'),
        ('4','Published'),
    ], string="Status", default="1")

    active = fields.Boolean(string="Active", default=True)
    
    resuser_id = fields.Many2one(comodel_name="res.users", string="Creator", default=lambda self: self.env.uid)
    # Relacion User Manual Sections
    usrmandetalle_ids = fields.One2many( comodel_name="usermanual_seccion", inverse_name="umanual_id" )
    # Relacion Comentarios Manual
    comment_ids = fields.One2many(comodel_name="usermanual_comment", inverse_name="manual_id", string="Comments")
    # Relacion Tipificacion Manual
    typ_id = fields.Many2one(comodel_name="usermanual_typification", string="Typification")
    category_id = fields.Many2one(comodel_name="usermanual_category", string="Category")

    def set_draft(self):
        self.status = '1'

    def set_revision(self):
        self.status = '2'

    def set_approved(self):
        self.status = '3'

    def set_published(self):
        self.status = '4'
    
    def get_reporte(self):
        return self.env.ref('user_manual_maker.action_report_user_manual').report_action(self)
    
    def get_section(self):
        return {
            'name': 'Section',
            'type': 'ir.actions.act_window',
            'res_model': 'usermanual_seccion',
            'view_mode': 'tree',
            'domain': [('umanual_id','=', self.id)],
            'context': '{"create": False}',
        }
    
    def add_comment_kanban(self):

        return {
            'name': 'Add My Comment',
            'type': 'ir.actions.act_window',
            'res_model': 'usermanual_comment',
            'view_mode': 'form',
            'view_id': False,
            'views': [(self.env.ref('user_manual_maker.wizard_usermanual_comment_form').id, 'form')],
            'target':'new',
            'domain': [('manual_id','=', self.id)],
            'context':{'manual_id': self.id},
        }
    
class UserManualSeccion(models.Model):
    _name = "usermanual_seccion"
    _description = "UMM Contents of the user manual"

    name = fields.Char(string='Section Name')
    sequence = fields.Integer(string = "Sequence")
    descripcion = fields.Char(string='Section description')
    binary_img = fields.Binary(string='Img Section/Cap')
    file_name_img = fields.Char()
    binary_video = fields.Binary(string='Video Section/Cap')
    file_name_video = fields.Char()

    # Relacion User Manual 
    umanual_id = fields.Many2one(comodel_name="user_manual_maker", string="Manual")
    # Relacion Paso de cada Manual
    usrmanstep_id = fields.One2many(comodel_name="usermanual_step", inverse_name="seccionman_id", string="Step Manual")

    def get_steps(self):
        return {
            'name': 'Steps',
            'type': 'ir.actions.act_window',
            'res_model': 'usermanual_step',
            'view_mode': 'tree',
            'domain': [('seccionman_id','=', self.id)],
            'context': '{"create": False}',
        }

class UserManualStep(models.Model):
    _name = "usermanual_step"
    _description = "UMM Section step"

    name = fields.Char(string='Section Name')
    sequence = fields.Integer(string = "Sequence")
    note = fields.Text(string='Note')
    binary_audio = fields.Binary(string='Audio Txt/Voz')
    file_name = fields.Char()

    # Relacion con seccion manual 
    seccionman_id = fields.Many2one(comodel_name="usermanual_seccion", string="Section")
    
class UserManualComment(models.Model):
    _name = "usermanual_comment"
    _description = "UMM Model that relates the comments for each manual"

    name = fields.Many2one(comodel_name="res.users", string="Requesting user", default=lambda self: self.env.uid)
    comment = fields.Char(string="Comment")
    manual_id = fields.Many2one(comodel_name="user_manual_maker", string="Manual")

class UserManualTipificacion(models.Model):
    _name = "usermanual_typification"
    _description = "UMM Model that stores suggestions for manuals."

    name = fields.Char(string="Name")    
    umanual_ids = fields.One2many(comodel_name="user_manual_maker", inverse_name="typ_id", string="Manual")

class UserManualCategory(models.Model):
    _name = "usermanual_category"
    _description = "UMM Model that categorys for manuals."

    name = fields.Char(string="Name")    
    cmanual_ids = fields.One2many(comodel_name="user_manual_maker", inverse_name="category_id", string="Manual")



