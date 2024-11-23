from marshmallow import Schema, fields, validateError

class RequestSchema(Schema):
    radius = fields.Float(required=True)
    layers = fields.Integer(required=True)
    topping = fields.String(required=True)