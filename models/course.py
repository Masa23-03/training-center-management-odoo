from odoo import fields , models

class KriozaCourse(models.Model):
    _name="krioza.course"
    _description="Training Course"

    name= fields.Char(
        string="Course Name",
        required=True
    ) 
    code=fields.Char(
        string="Course Code"
    )
    description=fields.Text(
        string="Description"
    )
    duration_hours=fields.Float(
        string="Duration (Hours)"
    )
    max_seats=fields.Integer(
        string="Maximum Seats", default=20
    )
    level=fields.Selection(
        [
            ("beginner" , "Beginner"),
            ("intermediate" , "Intermediate"),
            ("advanced" , "Advanced")
        ],
        string="Course Level"

    )
    image=fields.Image(
        string="Course Image"
    )