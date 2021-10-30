# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.modules.module import get_module_resource
from odoo import tools
import base64


"""
    This model for defining key attributes of clash of clans game troops
    and centralize main features and characteristics ...................
"""
class ClashOfClans(models.Model):

    _name = "clash.of.clans.troops"
    _description = "Clash Of Clans Troops"

    # method to set default image space holder attached with module and import versus size
    @api.model
    def _default_image(self):
        image_path = get_module_resource('clash_of_clans', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    name = fields.Char(string="Troop Name", required="True")
    level = fields.Integer(string="Level", required=True, default=1)
    image = fields.Binary(
        "Photo", default=_default_image, attachment=True,
        help="This field holds the image used as photo for the Troop, limited to 1024x1024px.")
    damage_per_second = fields.Integer(string="Damage Per Second", default=5)
    damage_per_second_temp = fields.Integer(compute="compute_damage_per_second_temp")
    maximum_damage_per_second_rate = fields.Integer(string="Max Damage Rate", default=100)
    hit_points = fields.Integer(string="Hit Points", default=10, required=True)
    hit_points_temp = fields.Integer(compute="compute_hit_points_temp")
    maximum_hit_points_rate = fields.Integer(string="Max Hitpoints Rate", default=100)
    training_cost = fields.Integer(string="Training Cost", required=True)
    training_time = fields.Integer(string="Training Time Seconds", required=True)
    favourite_target = fields.Selection([
        ('any', 'Any'),
        ('defences', 'Defences'),
        ('resources', 'Resources'),
    ], string="Favourite Target", default="any")
    damage_type = fields.Selection([
        ('single', 'Single'),
        ('area', 'Area Splash'),
    ], string="Damage Type", default="single")
    targets = fields.Selection([
        ('ground', 'Ground'),
        ('both', 'Ground & Air'),
    ], string="Targets", default="ground")
    housing_space = fields.Integer(string="Housing Space", required=True, default=1)
    movement_speed = fields.Integer(string="Movement Speed", required=True, default=12)
    description = fields.Text(string="Short Description")
    active = fields.Boolean(string="Archive", default=True)


    # this method using fields damage_per_second_temp, damage_per_second to suport the UX/UI
    @api.depends('damage_per_second')
    def compute_damage_per_second_temp(self):
        if self.damage_per_second:
            self.damage_per_second_temp = self.damage_per_second

    # this method using fields hit_points_temp, hit_points to suport the UX/UI 
    @api.depends('hit_points')
    def compute_hit_points_temp(self):
        if self.hit_points:
            self.hit_points_temp = self.hit_points
