import re

rule_messages = {
    'accepted': 'The :attribute must be accepted.',
    'active_url': 'The :attribute is not a valid URL.',
    'after': 'The :attribute must be a date after :date_0.',
    'after_or_equal': 'The :attribute must be a date after or equal to :date_0.',
    'alpha': 'The :attribute may only contain letters.',
    'alpha_dash': 'The :attribute may only contain letters, numbers, dashes and underscores.',
    'alpha_num': 'The :attribute may only contain letters and numbers.',
    'array': 'The :attribute must be an array.',
    'before': 'The :attribute must be a date before :date_0.',
    'before_or_equal': 'The :attribute must be a date before or equal to :date_0.',
    'between': {
        'numeric': 'The :attribute must be between :min_0 and :max_1.',
        'file': 'The :attribute must be between :min_0 and :max_1 kilobytes.',
        'string': 'The :attribute must be between :min_0 and :max_1 characters.',
        'array': 'The :attribute must have between :min_0 and :max_1 items.',
    },
    'boolean': 'The :attribute field must be true or false.',
    'confirmed': 'The :attribute confirmation does not match.',
    'date': 'The :attribute is not a valid date.',
    'date_equals': 'The :attribute must be a date equal to :date_0.',
    'date_format': 'The :attribute does not match the format :format_0.',
    'different': 'The :attribute and :other_0 must be different.',
    'digits': 'The :attribute must be :digits_0 digits.',
    'digits_between': 'The :attribute must be between :min_0 and :max_1 digits.',
    'dimensions': 'The :attribute has invalid image dimensions.',
    'distinct': 'The :attribute field has a duplicate value.',
    'email': 'The :attribute must be a valid email address.',
    'exists': 'The selected :attribute is invalid.',
    'file': 'The :attribute must be a file.',
    'filled': 'The :attribute field must have a value.',
    'gt': {
        'numeric': 'The :attribute must be greater than :value_0.',
        'file': 'The :attribute must be greater than :value_0 kilobytes.',
        'string': 'The :attribute must be greater than :value_0 characters.',
        'array': 'The :attribute must have more than :value_0 items.',
    },
    'gte': {
        'numeric': 'The :attribute must be greater than or equal :value_0.',
        'file': 'The :attribute must be greater than or equal :value_0 kilobytes.',
        'string': 'The :attribute must be greater than or equal :value_0 characters.',
        'array': 'The :attribute must have :value_0 items or more.',
    },
    'image': 'The :attribute must be an image.',
    'in': 'The selected :attribute is invalid.',
    'in_array': 'The :attribute field does not exist in :other_0.',
    'integer': 'The :attribute must be an integer.',
    'ip': 'The :attribute must be a valid IP address.',
    'ipv4': 'The :attribute must be a valid IPv4 address.',
    'ipv6': 'The :attribute must be a valid IPv6 address.',
    'json': 'The :attribute must be a valid JSON string.',
    'lt': {
        'numeric': 'The :attribute must be less than :value_0.',
        'file': 'The :attribute must be less than :value_0 kilobytes.',
        'string': 'The :attribute must be less than :value_0 characters.',
        'array': 'The :attribute must have less than :value_0 items.',
    },
    'lte': {
        'numeric': 'The :attribute must be less than or equal :value_0.',
        'file': 'The :attribute must be less than or equal :value_0 kilobytes.',
        'string': 'The :attribute must be less than or equal :value_0 characters.',
        'array': 'The :attribute must not have more than :value_0 items.',
    },
    'max': {
        'numeric': 'The :attribute may not be greater than :max_0.',
        'file': 'The :attribute may not be greater than :max_0 kilobytes.',
        'string': 'The :attribute may not be greater than :max_0 characters.',
        'array': 'The :attribute may not have more than :max_0 items.',
    },
    'mime_types': 'The :attribute must be a file of type: :values_0.',
    'min': {
        'numeric': 'The :attribute must be at least :min_0.',
        'file': 'The :attribute must be at least :min_0 kilobytes.',
        'string': 'The :attribute must be at least :min_0 characters.',
        'array': 'The :attribute must have at least :min_0 items.',
    },
    'not_in': 'The selected :attribute is invalid.',
    'not_regex': 'The :attribute format is invalid.',
    'numeric': 'The :attribute must be a number.',
    'present': 'The :attribute field must be present.',
    'regex': 'The :attribute format is invalid.',
    'required': 'The :attribute field is required.',
    'required_if': 'The :attribute field is required when :other_0 is :value_1.',
    'required_unless': 'The :attribute field is required unless :other_0 is in :values_rest.',
    'required_with': 'The :attribute field is required when :values_all is present.',
    'required_with_all': 'The :attribute field is required when :values_all are present.',
    'required_without': 'The :attribute field is required when :values_all is not present.',
    'required_without_all': 'The :attribute field is required when none of :values_all are present.',
    'same': 'The :attribute and :other_0 must match.',
    'size': {
        'numeric': 'The :attribute must be :size_0.',
        'file': 'The :attribute must be :size_0 kilobytes.',
        'string': 'The :attribute must be :size_0 characters.',
        'array': 'The :attribute must contain :size_0 items.',
    },
    'starts_with': 'The :attribute must start with one of the following: :values_all',
    'string': 'The :attribute must be a string.',
    'timezone': 'The :attribute must be a valid zone.',
    'unique': 'The :attribute has already been taken.',
    'uploaded': 'The :attribute failed to upload.',
    'url': 'The :attribute format is invalid.',
    'uuid': 'The :attribute must be a valid UUID.',
}
