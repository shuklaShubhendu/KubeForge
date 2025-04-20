from marshmallow import Schema, fields

class HabitSchema(Schema):
    habit = fields.String(required=True)
    created_at = fields.DateTime()
    logs = fields.List(fields.DateTime(), missing=[])
    streak = fields.Integer(missing=0)
