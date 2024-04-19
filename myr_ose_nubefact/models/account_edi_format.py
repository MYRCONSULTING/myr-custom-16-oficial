# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import zipfile
import io
from requests.exceptions import ConnectionError as ReqConnectionError, HTTPError, InvalidSchema, InvalidURL, ReadTimeout
from zeep.wsse.username import UsernameToken
from zeep import Client, Settings
from zeep.transports import Transport
from lxml import etree
from lxml import objectify
from copy import deepcopy

from odoo import models, api, _, _lt
from odoo.addons.iap.tools.iap_tools import iap_jsonrpc
from odoo.exceptions import AccessError
from odoo.tools import float_round, html_escape
import logging

_logger = logging.getLogger(__name__)

DEFAULT_IAP_ENDPOINT = 'https://iap-pe-edi.odoo.com'
DEFAULT_IAP_TEST_ENDPOINT = 'https://l10n-pe-edi-proxy-demo.odoo.com'


class AccountEdiFormat(models.Model):
    _inherit = 'account.edi.format'


    def _l10n_pe_edi_get_digiflow_credentials(self, company):
        self.ensure_one()
        res = {'fault_ns': 's'}
        if company.l10n_pe_edi_test_env:
            if company.flag_nubefact:
                res.update({
                    'wsdl': 'https://demo-ose.nubefact.com/ol-ti-itcpe/billService?wsdl',
                    'token': UsernameToken('20557912879MODDATOS', 'moddatos'),
                })
            else: #Digiflow
                res.update({
                    'wsdl': 'https://ose-test.com/ol-ti-itcpe/',
                    'token': UsernameToken('20557912879MODDATOS', 'moddatos'),
                })
        else:
            if company.flag_nubefact:
                res.update({
                    'wsdl': 'https://ose.nubefact.com/ol-ti-itcpe/billService?wsdl',                
                    'token': UsernameToken(company.sudo().l10n_pe_edi_provider_username, company.sudo().l10n_pe_edi_provider_password),
                })
            else: #Digiflow
                res.update({
                    'wsdl': 'https://ose.pe/ol-ti-itcpe/billService',                
                    'token': UsernameToken(company.sudo().l10n_pe_edi_provider_username, company.sudo().l10n_pe_edi_provider_password),
                })
        return res
