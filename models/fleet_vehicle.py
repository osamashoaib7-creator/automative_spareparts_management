from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    spare_part_ids = fields.One2many(comodel_name='fleet.spare.part', inverse_name='vehicle_id', string='Spare Parts')