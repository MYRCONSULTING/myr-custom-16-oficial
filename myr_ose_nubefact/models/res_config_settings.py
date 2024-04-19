# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    flag_nubefact = fields.Boolean(
        string="Nubefact",
        readonly=False,
        related="company_id.flag_nubefact",
        help="""Nubefact""")