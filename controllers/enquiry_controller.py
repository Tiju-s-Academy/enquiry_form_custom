
from odoo import http
from odoo.http import request, Response
import json

class EnquiryController(http.Controller):

    @http.route('/enquiry/submit', type='json', auth='public', methods=['POST'], csrf=False, website=True)
    def submit_enquiry(self, **kwargs):
        try:
            name = kwargs.get('name')
            phone = kwargs.get('phone')
            email = kwargs.get('email')
            course = kwargs.get('course')

            lead = request.env['crm.lead'].sudo().create({
                'name': f"Enquiry from {name}",
                'contact_name': name,
                'phone': phone,
                'email_from': email,
                'description': f"Interested in course: {course}",
            })

            return json.dumps({'success': True, 'lead_id': lead.id})

        except Exception as e:
            return json.dumps({'success': False, 'error': str(e)})

    @http.route('/enquiry/cors', type='http', auth='public', methods=['OPTIONS'], csrf=False)
    def cors_enquiry(self, **kwargs):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return Response(status=200, headers=headers)
