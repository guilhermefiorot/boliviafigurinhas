from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    image = fields.Str()
    price = fields.Float(required=True)
    condition = fields.Float(required=True)
    rarity = fields.Str(required=True)
    quantity = fields.Int(required=True)
