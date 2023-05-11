#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import logging

from xtce.generated import SpaceSystem
from xtce.parsers.constants import EntryListTypeAttr, ParameterTypeSetTypeAttr


class TelemetryParser:

    @classmethod
    def from_space_system(cls, space_system: SpaceSystem):
        telemetry_parser = cls()
        parameter_type_set = telemetry_parser._read_parameter_type_set(space_system=space_system)
        parameter_set = telemetry_parser._read_parameter_set(space_system=space_system)
        container_set = telemetry_parser._read_container_set(space_system=space_system)
        telemetry_parser._combine_data(parameter_type_set, parameter_set, container_set)

    @staticmethod
    def _combine_data(parameter_type_set, parameter_set, container_set):
        for container in container_set.values():
            if container.base_container is not None:
                base_container = container_set.get(container.base_container.container_ref)
                if base_container is None:
                    raise KeyError("failed to find base container")
                for comparison in container.base_container.restriction_criteria.comparison_list.comparison:
                    logging.info(f"> {comparison}")
            if container.entry_list is not None:
                for entry_type in EntryListTypeAttr.Types:
                    for entry in getattr(container.entry_list, entry_type):
                        parameter = parameter_set.get(entry.parameter_ref)
                        ptype = parameter_type_set.get(parameter.parameter_type_ref)
                        logging.info(f">> {entry} >> {parameter} >> {ptype}")

    @staticmethod
    def _validate_container_set(space_system: SpaceSystem):
        if space_system.telemetry_meta_data is None:
            return None
        if space_system.telemetry_meta_data.container_set is None:
            return None
        return space_system.telemetry_meta_data.container_set

    @classmethod
    def _read_container_set(cls, space_system):
        container_set = cls._validate_container_set(space_system)
        if container_set is None:
            return None
        containers = {}
        for container in container_set.sequence_container:
            containers[container.name] = container
        return containers

    @staticmethod
    def _validate_parameter_set(space_system: SpaceSystem):
        if space_system.telemetry_meta_data is None:
            return None
        if space_system.telemetry_meta_data.parameter_set is None:
            return None
        return space_system.telemetry_meta_data.parameter_set

    @classmethod
    def _read_parameter_set(cls, space_system):
        parameter_set = cls._validate_parameter_set(space_system)
        if parameter_set is None:
            return None
        parameters = {}
        for parameter in parameter_set.parameter:
            parameters[parameter.name] = parameter
        return parameters

    @staticmethod
    def _validate_parameter_type_set(space_system: SpaceSystem):
        if space_system.telemetry_meta_data is None:
            return None
        if space_system.telemetry_meta_data.parameter_type_set is None:
            return None
        return space_system.telemetry_meta_data.parameter_type_set

    @classmethod
    def _read_parameter_type_set(cls, space_system: SpaceSystem):
        parameter_type_set = cls._validate_parameter_type_set(space_system)
        if parameter_type_set is None:
            return None
        parameter_types = {}
        for type_set_attr in ParameterTypeSetTypeAttr.Types:
            for parameter_type in getattr(parameter_type_set, type_set_attr):
                parameter_types[parameter_type.name] = parameter_type
        return parameter_types
