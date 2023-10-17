from odoo import fields, models


class PartnerGender(models.Model):
    _name = 'partner.gender'

    name = fields.Char('Name')


class PosCustomer(models.Model):
    _inherit = 'res.partner'

    customerid = fields.Char(string='Customer ID', store=True, readonly=False, required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('ذكر', 'ذكر'), ('أنثى', 'أنثى')], string='Gender')
    gender_id = fields.Many2one('partner.gender')


class PosSession(models.Model):
    _inherit = "pos.session"
    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].extend(['customerid', 'gender', 'gender_id'])
        return result


    fields_get(self, allfields=None, attributes=None):
        fields = super().fields_get(allfields=allfields, attributes=attributes)
        # add additional fields here
        return fields

    def _pos_ui_models_to_load(self):
        # res = super(PosSession, self)._pos_ui_models_to_load(params)
        # return self.env['res.partner'].search_read(**params['search_params'])
        result = super()._pos_ui_models_to_load()
        print(">>>>>>res<<<<<<<<<< ",result)
        result.append('partner.gender')
        return result