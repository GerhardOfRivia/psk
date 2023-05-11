#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser

from miniature.xtce.exceptions import XtceInputError
from miniature.xtce.generated import SpaceSystem
from miniature.xtce.parsers import TelemetryParser


class Xtce:
    """
    Telemetry/Telecommand (TM/TC) definitions across the widest possible range
    of space domain activities. The goal is to allow TM/TC definitions to be
    exchanged between different organizations and systems, often at the
    boundaries of mission phases, without the need for customized import/export,
    re-validation, or even re-implementation of mission databases.
    """

    @classmethod
    def from_string(cls, source: str) -> SpaceSystem:
        """Load from a file"""
        try:
            space_system = XmlParser().from_string(source, SpaceSystem)
        except ParserError as err:
            raise XtceInputError("invalid input") from err

        TelemetryParser.from_space_system(space_system)
