#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class ParameterTypeSetTypeAttr:
    Types = [
        "string_parameter_type",
        "enumerated_parameter_type",
        "integer_parameter_type",
        "binary_parameter_type",
        "float_parameter_type",
        "boolean_parameter_type",
        "relative_time_parameter_type",
        "absolute_time_parameter_type",
        "array_parameter_type",
        "aggregate_parameter_type",
    ]


class EntryListTypeAttr:
    Types = [
        "parameter_ref_entry",
        "parameter_segment_ref_entry",
        "container_ref_entry",
        "container_segment_ref_entry",
        "stream_segment_entry",
        "indirect_parameter_ref_entry",
        "array_parameter_ref_entry",
    ]
