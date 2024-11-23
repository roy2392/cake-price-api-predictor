from marshmallow import Schema, fields, ValidationError

class RequestSchema(Schema):
    radius = fields.Float(required=True)
    layers = fields.Integer(required=True)
    topping = fields.String(required=True)