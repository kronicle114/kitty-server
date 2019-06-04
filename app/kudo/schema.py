from marshmallow import Schema, fields 

class KittySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()
    age = fields.Str()