class Schema:
    def __init__(self,
                title,
                description,
                type,
                properties,
                required,
                minimum=None,
                exclusiveMinimum=None,
                maximum=None,
                exclusiveMaximum=None,
                multipleOf=None,
                maxLength=None,
                minLength=None,
                pattern=None
                ):
        self.schema_draft = "http://json-schema.org/draft-04/schema#"
        self.title = title
        self.description = description
        self.type = type
        self.properties = properties
        self.required = required
        self.exclusiveMinimum = exclusiveMinimum
        self.maximum = maximum
        self.exclusiveMaximum = exclusiveMaximum
        self.multipleOf = multipleOf
        self.maxLength = maxLength
        self.minLength = minLength
        self.pattern = pattern
    
class Types:
    STRING = "string"
    NUMERIC_TYPES = "Numeric types"
    INTEGER = "integer"
    NUMBER = "number"
    OBJECT = "object"
    ARRAY = "array"
    BOOLEAN = "boolean"
    NULL = "null"