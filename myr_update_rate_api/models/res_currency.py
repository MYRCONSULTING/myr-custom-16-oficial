# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from odoo import api, fields, models, tools
import requests
import json
from datetime import datetime


TYPES = [('purchase', 'Compra'), ('sale', 'Venta')]

_logger = logging.getLogger(__name__)

class Currency(models.Model):
    _inherit = "res.currency"
    _description = "Currency"

   
    def action_exchange_rate_sale(self):
        session = requests.Session()
        headers = requests.utils.default_headers()
        headers = {'Content-Type': 'application/json'}
        url_rucpe = "https://ruc.com.pe/api/v1/consultas"
        data = {}
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime('%d/%m/%Y')
        
        company_id = self.env.company.id
        CurrencyRate = self.env['res.currency.rate']

        payload = json.dumps({
                    "token": "1cd7783e-8888-49c8-9301-ac790f5af258-9fa7a5e0-299e-4f88-aae0-60938cb36771",
                    "tipo_cambio": {
                        "moneda" : "PEN",
                        "fecha_inicio" : "01/12/2023",                        
                        "fecha_fin" : fecha_formateada}
                    })

        res = {'error': True, 'message': None, 'data': data}
        try:
            response = session.post(url=url_rucpe, headers=headers, data=payload)
        except requests.exceptions.ConnectionError as e:
            res['message'] = 'Error en la conexion : ' + str(e)
            return res
        
        if response.status_code == 200:
            res['error'] = False
            res['message'] = response.json()['success']
            res['data'] = response.json()['exchange_rates']
            #_logger.info(res['data'])
            for elemento in res['data']:
                
                fecha_parseada = datetime.strptime(elemento['fecha'], '%d/%m/%Y')
                fecha_convertida = fecha_parseada.strftime('%Y-%m-%d')
                date_rate = fecha_convertida
                rate_value = elemento['venta']

                already_existing_rate = CurrencyRate.search([('currency_id', '=', self.id), ('name', '=', date_rate), ('company_id', '=', company_id)])
                if not already_existing_rate:
                    CurrencyRate.create({'currency_id': self.id, 'rate': 1/rate_value, 'name': date_rate, 'company_id': company_id})

        elif response.status_code == 500:
            res['message'] = "Error en el servicio de API de Tipo de Cambio"
            return res
        else:
            try:
                res['message'] = response.json()['error']

            except Exception as e:
                res['error'] = True
        return res



