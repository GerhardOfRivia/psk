from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration

__NAMESPACE__ = "http://www.omg.org/spec/XTCE/20180204"


@dataclass
class AlgorithmTextType:
    """This optional element may be used to enter Pseudo or actual code for the
    algorithm.

    The language for the algorithm is specified with the language
    attribute
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: str = field(
        default="pseudo",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AliasType:
    """Used to contain an alias (alternate) name or ID for the object.

    For example, a parameter may have a mnemonic, an on-board id, and
    special IDs used by various ground software applications; all of
    these are alias's.  Some ground system processing equipment has some
    severe naming restrictions on parameters (e.g., names must less then
    12 characters, single case or integral id's only); their alias's
    provide a means of capturing each name in a "nameSpace".  Note: the
    name is not reference-able (it cannot be used in a name reference
    substituting for the name of the item of interest).  See
    NameDescriptionType.

    :ivar name_space: Aliases should be grouped together in a
        "namespace" so that they can be switched in and out of data
        extractions.  The namespace generally identifies the purpose of
        the alternate name, whether for software variable names,
        additional operator names, or whatever the purpose.
    :ivar alias: The alternate name or ID to use.  The alias does not
        have the restrictions that apply to name attributes.  This is
        useful for capturing legacy identifiers for systems with unusual
        naming conventions.  It is also useful for capturing variable
        names in software, amongst other things.
    """

    name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameSpace",
            "type": "Attribute",
            "required": True,
        },
    )
    alias: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AncillaryDataType:
    """Use for any other data associated with a named item.

    May be used to include administrative data (e.g., version, CM or
    tags) or potentially any MIME type.  Data may be included or given
    as an href.

    :ivar value:
    :ivar name: Identifier for this Ancillary Data characteristic,
        feature, or data.
    :ivar mime_type: Optional text encoding method for the element text
        content of this element.  The default is "text/plain".
    :ivar href: Optional Uniform Resource Identifier for this
        characteristic, feature, or data.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    mime_type: str = field(
        default="text/plain",
        metadata={
            "name": "mimeType",
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentAssignmentType:
    """Describe an assignment of an argument with a calibrated/engineering
    value.

    See ArgumentAssignmentListType.

    :ivar argument_name: The named argument from the base MetaCommand to
        assign/restrict with a value.
    :ivar argument_value: Specify value as a string compliant with the
        XML schema (xs) type specified for each XTCE type:
        integer=xs:integer; float=xs:double; string=xs:string;
        boolean=xs:boolean; binary=xs:hexBinary; enum=xs:string from
        EnumerationList; relative time=xs:duration; absolute
        time=xs:dateTime.  Supplied value must be within the ValidRange
        specified for the type.
    """

    argument_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "argumentName",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    argument_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "argumentValue",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ArgumentInstanceRefType:
    """
    An argument instance is the name of an argument as the reference is always
    resolved locally to the metacommand.

    :ivar argument_ref: Give the name of the argument.  There is no
        path, this is a local reference.
    :ivar use_calibrated_value: Typically the calibrated/engineering
        value is used and that is the default.
    """

    argument_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "argumentRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^./:\[\] ]+",
        },
    )
    use_calibrated_value: bool = field(
        default=True,
        metadata={
            "name": "useCalibratedValue",
            "type": "Attribute",
        },
    )


@dataclass
class AuthorSetType:
    """Describe an unordered collection of authors.

    See AuthorType.

    :ivar author: Contains information about an author, maintainer, or
        data source regarding this document.
    """

    author: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class BaseConditionsType:
    """
    A base type for boolean expression related elements that improves the
    mapping produced by data binding tools.
    """


@dataclass
class BaseTriggerType:
    """
    A base type for the various triggers, purely to improve the mappings
    created by data binding compilers.
    """


class BasisType(Enum):
    """Defines to type of update rates: perSecond and perContainerUpdate.

    See RateInStreamType.
    """

    PER_SECOND = "perSecond"
    PER_CONTAINER_UPDATE = "perContainerUpdate"


class BitOrderType(Enum):
    """Defines two bit-order types: most significant bit first and least
    significant bit first.

    See DataEncodingType.
    """

    LEAST_SIGNIFICANT_BIT_FIRST = "leastSignificantBitFirst"
    MOST_SIGNIFICANT_BIT_FIRST = "mostSignificantBitFirst"


class ByteOrderCommonType(Enum):
    """
    Common byte orderings: most significant byte first (also known as big
    endian) and least significant byte first (also known as little endian).
    """

    MOST_SIGNIFICANT_BYTE_FIRST = "mostSignificantByteFirst"
    LEAST_SIGNIFICANT_BYTE_FIRST = "leastSignificantByteFirst"


@dataclass
class ByteType:
    byte_significance: Optional[int] = field(
        default=None,
        metadata={
            "name": "byteSignificance",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )


class ChangeBasisType(Enum):
    """Defines absoluteChange and percentageChange for use in rate of change
    alarms.

    Used by ChangeAlarmRangesType.
    """

    ABSOLUTE_CHANGE = "absoluteChange"
    PERCENTAGE_CHANGE = "percentageChange"


class ChangeSpanType(Enum):
    """Defines a changePerSecond and changePerSample for use in rate of change
    alarms.

    Used by ChangeAlarmRangesType.
    """

    CHANGE_PER_SECOND = "changePerSecond"
    CHANGE_PER_SAMPLE = "changePerSample"


@dataclass
class ChangeValueType:
    """Describe a change value used to test verification status.

    See CommandVerifierType.

    :ivar value: Value as a floating point number.
    """

    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class CharacterWidthType(Enum):
    VALUE_8 = 8
    VALUE_16 = 16


class ChecksumTypeName(Enum):
    """
    :cvar UNIX_SUM:
    :cvar SUM8:
    :cvar SUM16:
    :cvar SUM24:
    :cvar SUM32:
    :cvar FLETCHER4:
    :cvar FLETCHER8:
    :cvar FLETCHER16:
    :cvar FLETCHER32:
    :cvar ADLER32:
    :cvar LUHN:
    :cvar VERHOEFF:
    :cvar DAMM:
    :cvar CUSTOM: Document a custom checksum algorithm
    """

    UNIX_SUM = "unix_sum"
    SUM8 = "sum8"
    SUM16 = "sum16"
    SUM24 = "sum24"
    SUM32 = "sum32"
    FLETCHER4 = "fletcher4"
    FLETCHER8 = "fletcher8"
    FLETCHER16 = "fletcher16"
    FLETCHER32 = "fletcher32"
    ADLER32 = "adler32"
    LUHN = "luhn"
    VERHOEFF = "verhoeff"
    DAMM = "damm"
    CUSTOM = "custom"


class ComparisonOperatorsType(Enum):
    """
    Operators to use when testing a boolean condition for a validity check.
    """

    VALUE = "=="
    VALUE_1 = "!="
    VALUE_2 = "&lt;"
    VALUE_3 = "&lt;="
    VALUE_4 = "&gt;"
    VALUE_5 = "&gt;="


class ConcernLevelsType(Enum):
    """Defines six levels: Normal, Watch, Warning, Distress, Critical and
    Severe.

    Typical implementations color the "normal" level as green, "warning"
    level as yellow, and "critical" level as red. These level
    definitions are used throughout the alarm definitions. Some systems
    provide a greater fidelity with the additional levels provided here.
    The "normal" level is not typically needed because "normal" should
    be construed as none of the concern levels evaluating to true. For
    cases where definiing "normal" is needed, refer to the specific
    alarm definition types.
    """

    NORMAL = "normal"
    WATCH = "watch"
    WARNING = "warning"
    DISTRESS = "distress"
    CRITICAL = "critical"
    SEVERE = "severe"


class ConsequenceLevelType(Enum):
    """Defines the criticality level of a command.

    Criticality levels follow ISO 14950.

    :cvar NORMAL: Normal command.  Corresponds to ISO 14950 Level D
        telecommand criticality.
    :cvar VITAL: Command that is not a critical command but is essential
        to the success of the mission and, if sent at the wrong time,
        could cause momentary loss of the mission.  Corresponds to ISO
        14950 Level C telecommand criticality.
    :cvar CRITICAL: Command that, if executed at the wrong time or in
        the wrong configuration, could cause irreversible loss or damage
        for the mission.  Corresponds to ISO 14950 Level B telecommand
        criticality.  Some space programs have called this "restricted"
        and may be implemented with a secondary confirmation before
        transmission.
    :cvar FORBIDDEN: Command that is not expected to be used for nominal
        or foreseeable contingency operations, that is included for
        unforeseen contingency operations, and that could cause
        irreversible damage if executed at the wrong time or in the
        wrong configuration.  Corresponds to ISO 14950 Level A
        telecommand criticality.  Some space programs have called this
        "prohibited".
    :cvar USER1: In the event that a program uses this value, that
        program will need to define the meaning of this value to their
        system.
    :cvar USER2: In the event that a program uses this value, that
        program will need to define the meaning of this value to their
        system.
    """

    NORMAL = "normal"
    VITAL = "vital"
    CRITICAL = "critical"
    FORBIDDEN = "forbidden"
    USER1 = "user1"
    USER2 = "user2"


@dataclass
class ConstantType:
    """Names and provides a value for a constant input to the algorithm.

    There are two attributes to Constant, constantName and value.
    constantName is a variable name in the algorithm to be executed.
    value is the value of the constant to be used.
    """

    constant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "constantName",
            "type": "Attribute",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ContainerRefType:
    """
    Holds a reference to a container.

    :ivar container_ref: name of container
    """

    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


class EpochTimeEnumsType(Enum):
    """
    Union values of common epoch definitions for document convenience.
    """

    TAI = "TAI"
    J2000 = "J2000"
    UNIX = "UNIX"
    GPS = "GPS"


@dataclass
class ExternalAlgorithmType:
    """This is the external algorithm.

    Multiple entries are provided so that the same database may be used
    for multiple implementation s
    """

    implementation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementationName",
            "type": "Attribute",
            "required": True,
        },
    )
    algorithm_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "algorithmLocation",
            "type": "Attribute",
            "required": True,
        },
    )


class FlagBitType(Enum):
    ZEROS = "zeros"
    ONES = "ones"


class FloatEncodingSizeInBitsType(Enum):
    """
    :cvar VALUE_16: At the time of this writing, 16 bit encoding size is
        only valid in cases of IEEE754 and vendor specific MILSTD_1750A
        variation that is not a part of the standard.  This is not meant
        to preclude use in the event that future floating point formats
        may also define this value.
    :cvar VALUE_32: At the time of this writing, 32 bit encoding size is
        only valid in cases of IEEE754_1985, IEEE754, MILSTD_1750A, DEC,
        IBM, and TI.  This is not meant to preclude use in the event
        that future floating point formats may also define this value.
        The IEEE754 enumeration and the IEEE754_1985 enumeration are
        allowed in this case and the interpretation is the same.
    :cvar VALUE_40: At the time of this writing, 40 bit encoding size is
        only valid in the case of TI.  This is not meant to preclude use
        in the event that future floating point formats may also define
        this value.
    :cvar VALUE_48: At the time of this writing, 48 bit encoding size is
        only valid in the case of MILSTD_1750A.  This is not meant to
        preclude use in the event that future floating point formats may
        also define this value.
    :cvar VALUE_64: At the time of this writing, 64 bit encoding size is
        only valid in cases of IEEE754_1985, IEEE754, DEC, and IBM.
        This is not meant to preclude use in the event that future
        floating point formats may also define this value.  The IEEE754
        enumeration and the IEEE754_1985 enumeration are allowed in this
        case and the interpretation is the same.
    :cvar VALUE_80: At the time of this writing, 80 bit encoding size is
        only valid in the case of IEEE754_1985.  This is not meant to
        preclude use in the event that future floating point formats may
        also define this value.
    :cvar VALUE_128: At the time of this writing, 128 bit encoding size
        is only valid in the case of IEEE754_1985 and IEEE754.  This is
        not meant to preclude use in the event that future floating
        point formats may also define this value.  The IEEE754
        enumeration and the IEEE754_1985 enumeration are allowed in this
        case and the interpretation is the same.
    """

    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_40 = 40
    VALUE_48 = 48
    VALUE_64 = 64
    VALUE_80 = 80
    VALUE_128 = 128


class FloatEncodingType(Enum):
    IEEE754_1985 = "IEEE754_1985"
    IEEE754 = "IEEE754"
    MILSTD_1750_A = "MILSTD_1750A"
    DEC = "DEC"
    IBM = "IBM"
    TI = "TI"


@dataclass
class FloatRangeType:
    """Describe a floating point based range, several types of ranges are
    supported -- one sided and two sided, inclusive or exclusive.

    It would not make sense to set two mins or maxes. Used in a number
    of locations related to ranges: ValidFloatRangeSetType or
    AlarmRangeType for example.

    :ivar min_inclusive: Minimum decimal/real number value including
        itself.
    :ivar min_exclusive: Minimum decimal/real number value excluding
        itself.
    :ivar max_inclusive: Maximum decimal/real number value including
        itself.
    :ivar max_exclusive: Maximum decimal/real number value excluding
        itself.
    """

    min_inclusive: Optional[float] = field(
        default=None,
        metadata={
            "name": "minInclusive",
            "type": "Attribute",
        },
    )
    min_exclusive: Optional[float] = field(
        default=None,
        metadata={
            "name": "minExclusive",
            "type": "Attribute",
        },
    )
    max_inclusive: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxInclusive",
            "type": "Attribute",
        },
    )
    max_exclusive: Optional[float] = field(
        default=None,
        metadata={
            "name": "maxExclusive",
            "type": "Attribute",
        },
    )


class FloatSizeInBitsType(Enum):
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_128 = 128


class FloatingPointNotationType(Enum):
    NORMAL = "normal"
    SCIENTIFIC = "scientific"
    ENGINEERING = "engineering"


@dataclass
class HistorySetType:
    """Describe an unordered collection of History elements.

    Usage is user defined.  See HistoryType.

    :ivar history: Contains a history record related to the evolution of
        this document.
    """

    history: List[str] = field(
        default_factory=list,
        metadata={
            "name": "History",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


class IntegerEncodingType(Enum):
    UNSIGNED = "unsigned"
    SIGN_MAGNITUDE = "signMagnitude"
    TWOS_COMPLEMENT = "twosComplement"
    ONES_COMPLEMENT = "onesComplement"
    BCD = "BCD"
    PACKED_BCD = "packedBCD"


@dataclass
class IntegerRangeType:
    """Describe an integral based range: minInclusive and maxInclusive.

    Used in a number of locations related to ranges:
    ValidIntegerRangeSetType for example.

    :ivar min_inclusive: Minimum integer value including itself.
    :ivar max_inclusive: Maximum integer value including itself.
    """

    min_inclusive: Optional[int] = field(
        default=None,
        metadata={
            "name": "minInclusive",
            "type": "Attribute",
        },
    )
    max_inclusive: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxInclusive",
            "type": "Attribute",
        },
    )


@dataclass
class LeadingSizeType:
    """Like PASCAL strings, the size of the string is given as an integer at
    the start of the string.

    SizeTag must be an unsigned Integer
    """

    size_in_bits_of_size_tag: int = field(
        default=16,
        metadata={
            "name": "sizeInBitsOfSizeTag",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )


@dataclass
class LinearAdjustmentType:
    """
    A slope and intercept may be applied to scale or shift the value of the
    parameter in the dynamic value.
    """

    slope: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    intercept: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        },
    )


class MathOperatorsType(Enum):
    """Mathematical operators used in the math operation.

    Behavior of each operator on the stack is described using notation
    (before -- after), where "before" represents the stack before
    execution of the operator and "after" represent the stack after
    execution.

    :cvar VALUE: addition (x1 x2 -- x1+x2)
    :cvar VALUE_1: subtraction (x1 x2 -- x1-x2)
    :cvar VALUE_2: multiplication (x1 x2 -- x1*x2)
    :cvar VALUE_3: division (x1 x2 -- x1/x2)
    :cvar VALUE_4: modulo (x1 x2 -- x3) Divide x1 by x2, giving the
        modulo x3
    :cvar VALUE_5: power function (x1 x2 -- x1**x2)
    :cvar Y_X: reverse power function (x1 x2 -- x2**x1)
    :cvar LN: natural (base e) logarithm (x -- ln(x))
    :cvar LOG: base-10 logarithm (x-- log(x))
    :cvar E_X: exponentiation (x -- exp(x))
    :cvar VALUE_1_X: inversion (x -- 1/x)
    :cvar X: factorial (x -- x!)
    :cvar TAN: tangent (x -- tan(x)) radians
    :cvar COS: cosine (x -- cos(x)) radians
    :cvar SIN: sine (x -- sin(x)) radians
    :cvar ATAN: arctangent (x -- atan(x)) radians
    :cvar ATAN2: arctangent (x1 x2 -- atan2(x2, x1)) radians
    :cvar ACOS: arccosine (x -- acos(x)) radians
    :cvar ASIN: arcsine (x -- asin(x)) radians
    :cvar TANH: hyperbolic tangent (x -- tanh(x))
    :cvar COSH: hyperbolic cosine (x -- cosh(x))
    :cvar SINH: hyperbolic sine (x -- sinh(x))
    :cvar ATANH: hyperbolic arctangent (x -- atanh(x))
    :cvar ACOSH: hyperbolic arccosine (x -- acosh(x))
    :cvar ASINH: hyperbolic arcsine (x -- asinh(x))
    :cvar SWAP: swap the top two stack items (x1 x2 -- x2 x1)
    :cvar DROP: Remove top item from the stack (x -- )
    :cvar DUP: Duplicate top item on the stack (x -- x x)
    :cvar OVER: Duplicate top item on the stack (x1 x2 -- x1 x2 x1)
    :cvar VALUE_6: signed bitwise left shift (x1 x2 -- x1 &lt;&lt; x2)
    :cvar VALUE_7: signed bitwise right shift (x1 x2 -- x1 &gt;&gt; x2)
    :cvar VALUE_8: bitwise and (x1 x2 -- x1 &amp; x2)
    :cvar VALUE_9: bitwise or (x1 x2 -- x1 | x2)
    :cvar VALUE_10: logical and (x1 x2 -- x1 &amp;&amp; x2)
    :cvar VALUE_11: logical or (x1 x2 -- x1 || x2)
    :cvar VALUE_12: logical not (x1 x2 -- x1 ! x2)
    :cvar ABS: absolute value (x1 -- abs(x1))
    :cvar DIV: Euclidean division quotient (x1 -- div(x1))
    :cvar INT: integer part (x1 -- int(x1))
    :cvar VALUE_13: greater than x,y (x1 x2 -- x1 &gt; x2)
    :cvar VALUE_14: greater than or equal x,y (x1 x2 -- x1 &gt;= x2)
    :cvar VALUE_15: less than x,y (x1 x2 -- x1 &lt; x2)
    :cvar VALUE_16: less than or equal x,y (x1 x2 -- x1 &lt;= x2)
    :cvar VALUE_17: equal x,y (x1 x2 -- x1 == x2)
    :cvar VALUE_18: not equal x,y (x1 x2 -- x1 != x2)
    :cvar MIN: minimum of x,y (x1 x2 -- min(x1, x2))
    :cvar MAX: maximum of x,y (x1 x2 -- max(x1, x2))
    :cvar XOR: Bitwise exclusive or (XOR) (x1 x2 -- x1 xor x2)
    :cvar VALUE_19: Bitwise not operation (x1 x2 -- x1 ~ x2) The result
        of this can only be 0 or 1
    """

    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"
    VALUE_4 = "%"
    VALUE_5 = "^"
    Y_X = "y^x"
    LN = "ln"
    LOG = "log"
    E_X = "e^x"
    VALUE_1_X = "1/x"
    X = "x!"
    TAN = "tan"
    COS = "cos"
    SIN = "sin"
    ATAN = "atan"
    ATAN2 = "atan2"
    ACOS = "acos"
    ASIN = "asin"
    TANH = "tanh"
    COSH = "cosh"
    SINH = "sinh"
    ATANH = "atanh"
    ACOSH = "acosh"
    ASINH = "asinh"
    SWAP = "swap"
    DROP = "drop"
    DUP = "dup"
    OVER = "over"
    VALUE_6 = "&lt;&lt;"
    VALUE_7 = "&gt;&gt;"
    VALUE_8 = "&amp;"
    VALUE_9 = "|"
    VALUE_10 = "&amp;&amp;"
    VALUE_11 = "||"
    VALUE_12 = "!"
    ABS = "abs"
    DIV = "div"
    INT = "int"
    VALUE_13 = "&gt;"
    VALUE_14 = "&gt;="
    VALUE_15 = "&lt;"
    VALUE_16 = "&lt;="
    VALUE_17 = "=="
    VALUE_18 = "!="
    MIN = "min"
    MAX = "max"
    XOR = "xor"
    VALUE_19 = "~"


@dataclass
class MessageRefType:
    """
    Holds a reference to a message.

    :ivar message_ref: name of message
    """

    message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class NoteSetType:
    """Contains an unordered collection of Notes.

    Usage is user defined.  See NoteType.

    :ivar note: Contains a program defined technical note regarding this
        document.
    """

    note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


class Pcmtype(Enum):
    NRZL = "NRZL"
    NRZM = "NRZM"
    NRZS = "NRZS"
    BI_PHASE_L = "BiPhaseL"
    BI_PHASE_M = "BiPhaseM"
    BI_PHASE_S = "BiPhaseS"


@dataclass
class ParameterRefType:
    """A reference to a Parameter.

    Uses Unix ‘like’ naming across the SpaceSystem Tree (e.g.,
    SimpleSat/Bus/EPDS/BatteryOne/Voltage).  To reference an individual
    member of an array use the zero based bracket notation commonly used
    in languages like C, C++, and Java.
    """

    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


class ParityFormType(Enum):
    EVEN = "Even"
    ODD = "Odd"


@dataclass
class PhysicalAddressType:
    """Describe the physical address(s) that this parameter is collected from.

    Examples of physical addresses include a memory location on the
    spacecraft or a location on a data collection bus, with the source
    identified with a descriptive name for the region of memory, such as
    RAM, Flash, EEPROM, and other possibilities that can be adapted for
    program specific usage.

    :ivar sub_address: A sub-address may be used to further specify the
        location if it fractionally occupies the address.  Additional
        possibilities exist for separating partitions of memory or other
        address based storage mechanisms.  This specification does not
        specify spacecraft specific hardware properties, so usage of
        addressing information is largely program and platform specific.
    :ivar source_name: A descriptive name for the location, such as a
        memory type, where this address is located.
    :ivar source_address: The address within the memory location.  This
        specification does not specify program and hardware specific
        attributes, such as address size and address region starting
        location.  These are part of the spacecraft hardware properties.
    """

    sub_address: Optional["PhysicalAddressType"] = field(
        default=None,
        metadata={
            "name": "SubAddress",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    source_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Attribute",
        },
    )
    source_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceAddress",
            "type": "Attribute",
        },
    )


class RadixType(Enum):
    """
    Specifies the number base.
    """

    DECIMAL = "Decimal"
    HEXADECIMAL = "Hexadecimal"
    OCTAL = "Octal"
    BINARY = "Binary"


class RangeFormType(Enum):
    """Defines whether the defined range between the minimum and maximum is the
    outside or inside the range being defined.

    The default, outside matches values less than the minimum and
    greater than the maximum.  Inside matches values between the minimum
    and maximum.
    """

    OUTSIDE = "outside"
    INSIDE = "inside"


class ReferenceLocationType(Enum):
    """The location may be relative to the start of the container
    (containerStart), relative to the end of the previous entry
    (previousEntry), relative to the end of the container (containerEnd), or
    relative to the entry that follows this one (nextEntry).

    If going forward (containerStart and previousEntry) then the
    location refers to the start of the
    Entry. If going backwards (containerEnd and nextEntry) then, the
    location refers to the end of the entry.
    """

    CONTAINER_START = "containerStart"
    CONTAINER_END = "containerEnd"
    PREVIOUS_ENTRY = "previousEntry"
    NEXT_ENTRY = "nextEntry"


class ReferencePointType(Enum):
    START = "start"
    END = "end"


@dataclass
class ServiceRefType:
    """
    A reference to a Service.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    service_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class SplinePointType:
    """
    A spline, or piecewise defined function, is a set on points from which a
    curve may be drawn to interpolate raw to calibrated values.

    :ivar order: The order of a SplineCalibrator refers to the
        interpolation function.  Order 0 is a flat line from the defined
        point (inclusive) to the next point (exclusive).  Order 1 is
        linear interpolation between two points.  Order 2 is quadratic
        fit and requires at least 3 points (unusual case).  This order
        is generally not needed, but may be used to override the
        interpolation order for this point.
    :ivar raw: The raw encoded value.
    :ivar calibrated: The engineering/calibrated value associated with
        the raw value for this point.
    """

    order: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    raw: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    calibrated: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StreamRefType:
    """
    Holds a reference to a stream.

    :ivar stream_ref: name of reference stream
    """

    stream_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "streamRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


class StringEncodingType(Enum):
    """Defines string encodings.

    US-ASCII (7-bit), ISO-8859-1 (8-bit Extended ASCII), Windows-1252
    (8-bit Extended ASCII), UTF-8 (Unicode), UTF-16 (Unicode with Byte
    Order Mark), UTF-16LE (Unicode Little Endian), UTF-16BE (Unicode Big
    Endian).  See StringDataEncodingType.

    :cvar US_ASCII:
    :cvar ISO_8859_1:
    :cvar WINDOWS_1252:
    :cvar UTF_8:
    :cvar UTF_16: With UTF-16, encoded bits must be prepended with a
        Byte Order Mark.  This mark indicates whether the data is
        encoded in big or little endian.
    :cvar UTF_16_LE: With UTF-16LE, encoded bits will always be
        represented as little endian.  Bits are not prepended with a
        Byte Order Mark.
    :cvar UTF_16_BE: With UTF-16BE, encoded bits will always be
        represented as big endian.  Bits are not prepended with a Byte
        Order Mark.
    :cvar UTF_32: With UTF-32, encoded bits must be prepended with a
        Byte Order Mark.  This mark indicates whether the data is
        encoded in big or little endian.
    :cvar UTF_32_LE: With UTF-32LE, encoded bits will always be
        represented as little endian.  Bits are not prepended with a
        Byte Order Mark.
    :cvar UTF_32_BE: With UTF-32BE, encoded bits will always be
        represented as big endian.  Bits are not prepended with a Byte
        Order Mark.
    """

    US_ASCII = "US-ASCII"
    ISO_8859_1 = "ISO-8859-1"
    WINDOWS_1252 = "Windows-1252"
    UTF_8 = "UTF-8"
    UTF_16 = "UTF-16"
    UTF_16_LE = "UTF-16LE"
    UTF_16_BE = "UTF-16BE"
    UTF_32 = "UTF-32"
    UTF_32_LE = "UTF-32LE"
    UTF_32_BE = "UTF-32BE"


@dataclass
class SyncPatternType:
    """
    The pattern of bits used to look for frame synchronization.

    :ivar pattern: CCSDS ASM for non-turbocoded frames = 1acffc1d
    :ivar bit_location_from_start_of_container:
    :ivar mask:
    :ivar mask_length_in_bits: truncate the mask from the left
    :ivar pattern_length_in_bits: truncate the pattern from the left
    """

    pattern: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "format": "base16",
        },
    )
    bit_location_from_start_of_container: int = field(
        default=0,
        metadata={
            "name": "bitLocationFromStartOfContainer",
            "type": "Attribute",
        },
    )
    mask: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "format": "base16",
        },
    )
    mask_length_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "maskLengthInBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    pattern_length_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "patternLengthInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


class TelemetryDataSourceType(Enum):
    """A telemetered Parameter is one that will have values in telemetry.

    A derived Parameter is one that is calculated, usually by an
    Algorithm. A constant Parameter is one that is used as a constant in
    the system (e.g. a vehicle id). A local Parameter is one that is
    used purely by the software locally (e.g. a ground command counter).
    A ground Parameter is one that is generated by an asset which is not
    the spacecraft.
    """

    TELEMETERED = "telemetered"
    DERIVED = "derived"
    CONSTANT = "constant"
    LOCAL = "local"
    GROUND = "ground"


@dataclass
class TermType:
    """
    A term in a polynomial expression.

    :ivar coefficient: The coefficient in a single term of a polynomial
        expression.
    :ivar exponent: The exponent in a single term of a polynomial
        expression.  Should negative exponents be required, use a Math
        Calibrator style of definition for this type.
    """

    coefficient: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    exponent: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )


class TimeAssociationUnitType(Enum):
    """
    Time units the time association decimal value is in.
    """

    SI_NANOSECOND = "si_nanosecond"
    SI_MICROSECOND = "si_microsecond"
    SI_MILLSECOND = "si_millsecond"
    SI_SECOND = "si_second"
    MINUTE = "minute"
    DAY = "day"
    JULIAN_YEAR = "julianYear"


class TimeUnitsType(Enum):
    """base time units.

    days, months, years have obvoius ambiguity and should be avoided
    """

    SECONDS = "seconds"
    PICO_SECONDS = "picoSeconds"
    DAYS = "days"
    MONTHS = "months"
    YEARS = "years"


class TimeWindowIsRelativeToType(Enum):
    COMMAND_RELEASE = "commandRelease"
    TIME_LAST_VERIFIER_PASSED = "timeLastVerifierPassed"


class UnitFormType(Enum):
    """
    Optionally specify if this information pertains to something other than the
    calibrated/engineering value.
    """

    CALIBRATED = "calibrated"
    UNCALIBRATED = "uncalibrated"
    RAW = "raw"


class ValidationStatusType(Enum):
    UNKNOWN = "Unknown"
    WORKING = "Working"
    DRAFT = "Draft"
    TEST = "Test"
    VALIDATED = "Validated"
    RELEASED = "Released"
    WITHDRAWN = "Withdrawn"


@dataclass
class ValueEnumerationType:
    """
    Describe a value and an associated string label, see EnumerationListType.

    :ivar value: Numeric raw/uncalibrated value to associate with a
        string enumeration label.
    :ivar max_value: If max value is given, the label maps to a range
        where value is less than or equal to maxValue. The range is
        inclusive.
    :ivar label: String enumeration label to apply to this value
        definition in the enumeration.
    :ivar short_description: An optional additional string description
        can be specified for this enumeration label to provide extended
        information if desired.
    """

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    max_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Attribute",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Attribute",
        },
    )


class VerifierEnumerationType(Enum):
    """
    An enumerated list of verifier types.
    """

    RELEASE = "release"
    TRANSFERRED_TO_RANGE = "transferredToRange"
    SENT_FROM_RANGE = "sentFromRange"
    RECEIVED = "received"
    ACCEPTED = "accepted"
    QUEUED = "queued"
    EXECUTING = "executing"
    COMPLETE = "complete"
    FAILED = "failed"


@dataclass
class AliasSetType:
    """
    Contains an unordered collection of Alias elements to describe alternate
    names or IDs for this named item.

    :ivar alias: An alternate name, ID number, and sometimes flight
        software variable name in the code for this item.
    """

    alias: List[AliasType] = field(
        default_factory=list,
        metadata={
            "name": "Alias",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class AncillaryDataSetType:
    """Describe an unordered collection of ancillary data.

    AncillaryData elements capture platform/program/implementation
    specific data about the parent element object that is non-standard
    and would not fit into the schema.  See AncillaryDataType.

    :ivar ancillary_data: Optional list of AncillaryData elements
        associated with this item.
    """

    ancillary_data: List[AncillaryDataType] = field(
        default_factory=list,
        metadata={
            "name": "AncillaryData",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ArgumentAssignmentListType:
    """Argument Assignments specialize a MetaCommand or BlockMetaCommand when
    inheriting from another MetaCommand.

    General argument values can be restricted to specific values to
    further specialize the MetaCommand.  Use it to ‘narrow’ a
    MetaCommand from its base MetaCommand by specifying values of
    arguments for example, a power command may be narrowed to a power
    on’ command by assigning the value of an argument to ‘on’.  See
    ArgumentAssignmentType and MetaCommandType.

    :ivar argument_assignment: Specialize this command definition when
        inheriting from a more general MetaCommand by restricting the
        specific values of otherwise general arguments.
    """

    argument_assignment: List[ArgumentAssignmentType] = field(
        default_factory=list,
        metadata={
            "name": "ArgumentAssignment",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class Crctype:
    """Cyclic Redundancy Check (CRC) definition.

    The polynomial coefficients for the CRC are defined as a truncated
    hex value.  The coefficient for the nth bit of an n-bit CRC will
    always be 1 and is not represented in the truncated hex value.  For
    example, the truncated hex value of CRC-32 (width=32 bits) used in
    the Ethernet specification is 0x04C11DB7, where each non-zero bit of
    the truncated hex represents a coefficient of 1 in the polynomial
    and the bit position represents the exponent. There may also be an
    initial remainder "InitRemainder" and a final XOR "FinalXOR" to
    fully specify the CRC.  reflectData and reflectRemainder may also be
    specified to reverse the bit order in the incoming data and/or the
    result.
    """

    class Meta:
        name = "CRCType"

    polynomial: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Polynomial",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
            "format": "base16",
        },
    )
    init_remainder: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitRemainder",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "format": "base16",
        },
    )
    final_xor: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FinalXOR",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "format": "base16",
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    reflect_data: bool = field(
        default=False,
        metadata={
            "name": "reflectData",
            "type": "Attribute",
        },
    )
    reflect_remainder: bool = field(
        default=False,
        metadata={
            "name": "reflectRemainder",
            "type": "Attribute",
        },
    )
    bits_from_reference: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitsFromReference",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    reference: ReferencePointType = field(
        default=ReferencePointType.START,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CheckWindowType:
    """Used by CommandVerifiers to limit the time allocated to check for the
    verification.

    See CheckWindowAlgorithmsType.
    """

    time_to_start_checking: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "timeToStartChecking",
            "type": "Attribute",
        },
    )
    time_to_stop_checking: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "timeToStopChecking",
            "type": "Attribute",
            "required": True,
        },
    )
    time_window_is_relative_to: TimeWindowIsRelativeToType = field(
        default=TimeWindowIsRelativeToType.TIME_LAST_VERIFIER_PASSED,
        metadata={
            "name": "timeWindowIsRelativeTo",
            "type": "Attribute",
        },
    )


@dataclass
class ContainerRefSetType:
    container_ref: List[ContainerRefType] = field(
        default_factory=list,
        metadata={
            "name": "ContainerRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class EnumerationAlarmLevelType:
    """Describe an alarm level and its enumeration label to trigger from.

    See EnumeratedAlarmType and EnumeratedParameterType.

    :ivar alarm_level: Defines six levels: Normal, Watch, Warning,
        Distress, Critical and Severe. Typical implementations color the
        "normal" level as green, "warning" level as yellow, and
        "critical" level as red. In the case of enumeration alarms, the
        "normal" is assumed by implementations to be any label not
        otherwise in an alarm state.
    :ivar enumeration_label: The enumeration label is the
        engineering/calibrated value for enumerated types.
    """

    alarm_level: Optional[ConcernLevelsType] = field(
        default=None,
        metadata={
            "name": "alarmLevel",
            "type": "Attribute",
            "required": True,
        },
    )
    enumeration_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "enumerationLabel",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EnumerationListType:
    enumeration: List[ValueEnumerationType] = field(
        default_factory=list,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ExternalAlgorithmSetType:
    external_algorithm: List[ExternalAlgorithmType] = field(
        default_factory=list,
        metadata={
            "name": "ExternalAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class FlagType:
    """
    The pattern of bits used to look for frame synchronization.
    """

    flag_size_in_bits: int = field(
        default=6,
        metadata={
            "name": "flagSizeInBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    flag_bit_type: FlagBitType = field(
        default=FlagBitType.ONES,
        metadata={
            "name": "flagBitType",
            "type": "Attribute",
        },
    )


@dataclass
class HeaderType:
    """Schema for a Header record.

    A header contains general information about the system or subsystem.

    :ivar author_set: The AuthorSet contains optional contact
        information for this document.
    :ivar note_set: The NoteSet contains optional technical information
        related to the content of this document.
    :ivar history_set: The HistorySet contains optional evolutionary
        information for data contained in this document.
    :ivar version: This attribute contains an optional version
        descriptor for this document.
    :ivar date: This attribute contains an optional date to be
        associated with this document.
    :ivar classification: This attribute contains optional
        classification status for use by programs for which that is
        applicable.
    :ivar classification_instructions: This attribute contains an
        optional additional instructions attribute to be interpreted by
        programs that use this attribute.
    :ivar validation_status: This attribute contains a flag describing
        the state of this document in the evolution of the project using
        it.
    """

    author_set: Optional[AuthorSetType] = field(
        default=None,
        metadata={
            "name": "AuthorSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    note_set: Optional[NoteSetType] = field(
        default=None,
        metadata={
            "name": "NoteSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    history_set: Optional[HistorySetType] = field(
        default=None,
        metadata={
            "name": "HistorySet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    classification: str = field(
        default="NotClassified",
        metadata={
            "type": "Attribute",
        },
    )
    classification_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "classificationInstructions",
            "type": "Attribute",
        },
    )
    validation_status: Optional[ValidationStatusType] = field(
        default=None,
        metadata={
            "name": "validationStatus",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class InterlockType:
    """Describe a type of constraint on the next command, rather than this
    command.

    Interlocks apply only to the next command.  An interlock will block
    successive commands until this command has reached a certain stage
    of verifier.  Interlocks are scoped to a SpaceSystem basis:  they by
    default apply to the SpaceSystem the MetaCommand is defined in but
    this may be overridden.  See MetaCommandType and VerifierSetType.

    :ivar scope_to_space_system: The name of a SpaceSystem this
        Interlock applies to.  By default, it only applies to the
        SpaceSystem that contains this MetaCommand.
    :ivar verification_to_wait_for: The verification stage of the
        command that releases the interlock, with the default being
        complete.
    :ivar verification_progress_percentage: Only applies when the
        verificationToWaitFor attribute is 'queued' or 'executing'.
    :ivar suspendable: A flag that indicates that under special
        circumstances, this Interlock can be suspended.
    """

    scope_to_space_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "scopeToSpaceSystem",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    verification_to_wait_for: VerifierEnumerationType = field(
        default=VerifierEnumerationType.COMPLETE,
        metadata={
            "name": "verificationToWaitFor",
            "type": "Attribute",
        },
    )
    verification_progress_percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "verificationProgressPercentage",
            "type": "Attribute",
        },
    )
    suspendable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MessageRefSetType:
    message_ref: List[MessageRefType] = field(
        default_factory=list,
        metadata={
            "name": "MessageRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class MultiRangeType(FloatRangeType):
    """The alarm multi-range element type permits users to define multiple
    alarm ranges in a sequence that goes beyond the more typical "inside" and
    "outside" range definitions.

    It can be thought of as a "barber pole" definition.

    :ivar range_form: A value of outside specifies that the most severe
        range is outside all the other ranges: -severe -critical
        -distress -warning -watch normal +watch +warning +distress
        +critical +severe. A value of inside "inverts" these bands:
        -green -watch -warning -distress -critical severe +critical
        +distress +warning +watch. The most common form used is
        "outside" and is the default.
    :ivar level: The level of concern for this alarm definition.
    """

    range_form: RangeFormType = field(
        default=RangeFormType.OUTSIDE,
        metadata={
            "name": "rangeForm",
            "type": "Attribute",
        },
    )
    level: Optional[ConcernLevelsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class NumberFormatType:
    """This type describes how a numeric value should be represented in
    engineering/calibrated form.

    The defaults reflect the most common form.

    :ivar number_base: Describes how the engineering/calibrated value of
        this number should be displayed with respect to the radix.
        Default is base 10.
    :ivar minimum_fraction_digits: Describes how the
        engineering/calibrated value of this number should be displayed
        with respect to the minimum number of fractional digits.  The
        default is 0.
    :ivar maximum_fraction_digits: Describes how the
        engineering/calibrated value of this number should be displayed
        with respect to the maximum or upper bound of the number of
        digits.  There is no default.  No value specified should be
        interpreted as no upper bound such that all requires digits are
        used to fully characterize the value.
    :ivar minimum_integer_digits: Describes how the
        engineering/calibrated value of this number should be displayed
        with respect to the minimum number of integer digits.  The
        default is 1.
    :ivar maximum_integer_digits: Describes how the
        engineering/calibrated value of this number should be displayed
        with respect to the maximum or upper bound of the integer
        digits.  There is no default.  No value specified should be
        interpreted as no upper bound such that all requires digits are
        used to fully characterize the value.
    :ivar negative_suffix: Describes how the engineering/calibrated
        value of this number should be displayed with respect to
        negative values.  This attribute specifies the character or
        characters that should be appended to the numeric value to
        indicate negative values.  The default is none.
    :ivar positive_suffix: Describes how the engineering/calibrated
        value of this number should be displayed with respect to
        positive values.  This attribute specifies the character or
        characters that should be appended to the numeric value to
        indicate positive values.  The default is none.  Zero is
        considered to be specific to the implementation/platform and is
        not implied here.
    :ivar negative_prefix: Describes how the engineering/calibrated
        value of this number should be displayed with respect to
        negative values.  This attribute specifies the character or
        characters that should be prepended to the numeric value to
        indicate negative values.  The default is a minus character "-".
    :ivar positive_prefix: Describes how the engineering/calibrated
        value of this number should be displayed with respect to
        positive values.  This attribute specifies the character or
        characters that should be prepended to the numeric value to
        indicate positive values.  The default is none.  Zero is
        considered to be specific to the implementation/platform and is
        not implied here.
    :ivar show_thousands_grouping: Describes how the
        engineering/calibrated value of this number should be displayed
        with respect to larger values.  Groupings by thousand are
        specific to locale, so the schema only specifies whether they
        will be present and not which character separators are used.
        The default is false.
    :ivar notation: Describes how the engineering/calibrated value of
        this number should be displayed with respect to notation.
        Engineering, scientific, or traditional decimal notation may be
        specified.  The precise characters used is locale specific for
        the implementation/platform.  The default is "normal" for the
        traditional notation.
    """

    number_base: RadixType = field(
        default=RadixType.DECIMAL,
        metadata={
            "name": "numberBase",
            "type": "Attribute",
        },
    )
    minimum_fraction_digits: int = field(
        default=0,
        metadata={
            "name": "minimumFractionDigits",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    maximum_fraction_digits: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumFractionDigits",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    minimum_integer_digits: int = field(
        default=1,
        metadata={
            "name": "minimumIntegerDigits",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    maximum_integer_digits: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumIntegerDigits",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    negative_suffix: str = field(
        default="",
        metadata={
            "name": "negativeSuffix",
            "type": "Attribute",
        },
    )
    positive_suffix: str = field(
        default="",
        metadata={
            "name": "positiveSuffix",
            "type": "Attribute",
        },
    )
    negative_prefix: str = field(
        default="-",
        metadata={
            "name": "negativePrefix",
            "type": "Attribute",
        },
    )
    positive_prefix: str = field(
        default="",
        metadata={
            "name": "positivePrefix",
            "type": "Attribute",
        },
    )
    show_thousands_grouping: bool = field(
        default=False,
        metadata={
            "name": "showThousandsGrouping",
            "type": "Attribute",
        },
    )
    notation: FloatingPointNotationType = field(
        default=FloatingPointNotationType.NORMAL,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class OnContainerUpdateTriggerType(BaseTriggerType):
    """Describe a reference to container that triggers an event when the
    telemetry container referred to is updated (processed).

    See TriggerSetType.

    :ivar container_ref: Reference to the Container whose update/receipt
        triggers this algorithm to evaluate.
    """

    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class OnParameterUpdateTriggerType(BaseTriggerType):
    """Describe a reference to parameter that triggers an event when the
    telemetry parameter referred to is updated (processed) with a new value.

    See TriggerSetType.

    :ivar parameter_ref: Reference to the Parameter whose update
        triggers this algorithm to evaluate.
    """

    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class OnPeriodicRateTriggerType(BaseTriggerType):
    """Describe a periodic time basis to trigger an event.

    See TriggerSetType.

    :ivar fire_rate_in_seconds: The periodic rate in time in which this
        algorithm is triggered to evaluate.
    """

    fire_rate_in_seconds: Optional[float] = field(
        default=None,
        metadata={
            "name": "fireRateInSeconds",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class OutputParameterRefType(ParameterRefType):
    """Names an output parameter to the algorithm.

    There are two attributes to OutputParm, outputName and
    parameterName. parameterName is a parameter reference name for a
    parameter that will be updated by this algorithm.  outputName is an
    optional "friendly" name for the output parameter.
    """

    output_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputName",
            "type": "Attribute",
        },
    )


@dataclass
class ParameterInstanceRefType(ParameterRefType):
    """A reference to an instance of a Parameter.

    Used when the value of a parameter is required for a calculation or
    as an index value.  A positive value for instance is forward in
    time, a negative value for count is backward in time, a 0 value for
    count means use the current value of the parameter or the first
    value in a container.
    """

    instance: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    use_calibrated_value: bool = field(
        default=True,
        metadata={
            "name": "useCalibratedValue",
            "type": "Attribute",
        },
    )


@dataclass
class ParameterToSuspendAlarmsOnType(ParameterRefType):
    """
    Will suspend all Alarms associated with this Parameter for the given
    suspense time after the given verifier.
    """

    suspense_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "suspenseTime",
            "type": "Attribute",
            "required": True,
        },
    )
    verifier_to_trigger_on: VerifierEnumerationType = field(
        default=VerifierEnumerationType.RELEASE,
        metadata={
            "name": "verifierToTriggerOn",
            "type": "Attribute",
        },
    )


@dataclass
class ParameterValueChangeType:
    """
    A parameter change in value or specified delta change in value.
    """

    parameter_ref: Optional[ParameterRefType] = field(
        default=None,
        metadata={
            "name": "ParameterRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    change: Optional[ChangeValueType] = field(
        default=None,
        metadata={
            "name": "Change",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ParityType:
    """
    Bit position starts with 'zero'.
    """

    type: Optional[ParityFormType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    bits_from_reference: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitsFromReference",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    reference: ReferencePointType = field(
        default=ReferencePointType.START,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PhysicalAddressSetType:
    """One or more physical addresses may be associated with each Parameter.

    Examples of physical addresses include a location on the spacecraft
    or a location on a data collection bus.

    :ivar physical_address: Contains the address (e.g., channel
        information) required to process the spacecraft telemetry
        streams. May be an onboard  id, a mux address, or a physical
        location. Contains the address (channel information) required to
        process the spacecraft telemetry streams
    """

    physical_address: List[PhysicalAddressType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAddress",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class RateInStreamType:
    """Define the expected appearance (rate) of a container in a stream where
    the rate is defined on either a perSecond or perContainer update basis.

    Many programs and platforms have variable reporting rates for
    containers and these can be commanded.  As a result, this element is
    only useful to some users and generally does not affect the
    processing of the received containers themselves.  See
    ContainerType.

    :ivar basis: The measurement unit basis for the minimum and maximum
        appearance count values.
    :ivar minimum_value: The minimum rate for the specified basis for
        which this container should appear in the stream.
    :ivar maximum_value: The maximum rate for the specified basis for
        which this container should appear in the stream.
    """

    basis: BasisType = field(
        default=BasisType.PER_SECOND,
        metadata={
            "type": "Attribute",
        },
    )
    minimum_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Attribute",
        },
    )
    maximum_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Attribute",
        },
    )


@dataclass
class SignificanceType:
    """
    Significance provides some cautionary information about the potential
    consequence of each MetaCommand.

    :ivar space_system_at_risk: If none is supplied, then the current
        SpaceSystem is assumed to be the one at risk by the issuance of
        this command
    :ivar reason_for_warning:
    :ivar consequence_level:
    """

    space_system_at_risk: Optional[str] = field(
        default=None,
        metadata={
            "name": "spaceSystemAtRisk",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    reason_for_warning: Optional[str] = field(
        default=None,
        metadata={
            "name": "reasonForWarning",
            "type": "Attribute",
        },
    )
    consequence_level: ConsequenceLevelType = field(
        default=ConsequenceLevelType.NORMAL,
        metadata={
            "name": "consequenceLevel",
            "type": "Attribute",
        },
    )


@dataclass
class SizeInBitsType:
    """
    :ivar fixed: This is the simplest case of a string data type where
        the encoding size of the string does not change.
    :ivar termination_char: The termination character that represents
        the end of the string contents.  For C and most strings, this is
        null (00), which is the default.
    :ivar leading_size: In some string implementations, the size of the
        string contents (not the memory allocation size) is determined
        by a leading numeric value.  This is sometimes referred to as
        Pascal strings.  If a LeadingSize is specified, then the
        TerminationChar element does not have a functional meaning.
    """

    fixed: Optional["SizeInBitsType.Fixed"] = field(
        default=None,
        metadata={
            "name": "Fixed",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    termination_char: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TerminationChar",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "format": "base16",
        },
    )
    leading_size: Optional[LeadingSizeType] = field(
        default=None,
        metadata={
            "name": "LeadingSize",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )

    @dataclass
    class Fixed:
        """
        :ivar fixed_value: Size in bits of this string data type for
            both the memory allocation in the implementing software and
            also the size in bits for this parameter when it appears in
            a container.
        """

        fixed_value: Optional[int] = field(
            default=None,
            metadata={
                "name": "FixedValue",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/XTCE/20180204",
                "required": True,
                "min_inclusive": 1,
            },
        )


@dataclass
class StringAlarmLevelType:
    """Describe a string alarm condition based on matching a regular
    expression.

    The level and regular expression are described.  The specific
    implementation of the regular expression syntax is not specified in
    the schema at this time.  See StringAlarmListType.
    """

    alarm_level: Optional[ConcernLevelsType] = field(
        default=None,
        metadata={
            "name": "alarmLevel",
            "type": "Attribute",
            "required": True,
        },
    )
    match_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "matchPattern",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class UnitType:
    """Describe the exponent, factor, form, and description for a unit.

    The unit itself is in element Unit in UnitSet.  See UnitSetType.
    The attributes are optional because different programs use this
    element in different ways, depending on vendor support.

    :ivar power: Optional attribute used in conjunction with the
        "factor" attribute where some programs choose to specify the
        unit definition with these machine processable algebraic
        features.  For example, a unit text of "meters" may have a
        "power" attribute of 2, resulting "meters squared" as the actual
        unit.  This is not commonly used.  The most common method for
        "meters squared" is to use the text content of the Unit element
        in a form like "m^2".
    :ivar factor: Optional attribute used in conjunction with the
        "power" attribute where some programs choose to specify the unit
        definition with these machine processable algebraic features.
        For example, a unit text of "meters" may have a "factor"
        attribute of 2, resulting "2 times meters" as the actual unit.
        This is not commonly used.  The most common method for "2 times
        meters" is to use the text content of the Unit element in a form
        like "2*m".
    :ivar description: A description of the unit, which may be for
        expanded human readability or for specification of the
        nature/property of the unit.  For example, meters per second
        squared is of a nature/property of acceleration.
    :ivar form: The default value "calibrated" is most common practice
        to specify units at the engineering/calibrated value, it is
        possible to specify an additional Unit element for the
        raw/uncalibrated value.
    :ivar content:
    """

    power: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
        },
    )
    factor: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: UnitFormType = field(
        default=UnitFormType.CALIBRATED,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class ValidFloatRangeSetType:
    """Numerical ranges that define the universe of valid values for this
    argument.

    A single range is the most common, although it is possible to define
    multiple ranges when the valid values are not contiguous.

    :ivar valid_range: A valid range constrains the whole set of
        possible values that could be encoded by the data type to a more
        "valid" or "reasonable" set of values.  This should be treated
        as a boundary check in an implementation to validate the input
        or output value.  Typically, only 1 range is used.  In cases
        where multiple ranges are used, then the value is valid when it
        is valid in any of the provided ranges.  Implementations may
        also use these ranges to enhance user interface displays and
        other visualization widgets as appropriate for the type.
    :ivar valid_range_applies_to_calibrated: By default and general
        recommendation, the valid range is specified in
        engineering/calibrated values, although this can be adjusted.
    """

    valid_range: List[FloatRangeType] = field(
        default_factory=list,
        metadata={
            "name": "ValidRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )
    valid_range_applies_to_calibrated: bool = field(
        default=True,
        metadata={
            "name": "validRangeAppliesToCalibrated",
            "type": "Attribute",
        },
    )


@dataclass
class ValidIntegerRangeSetType:
    """Numerical ranges that define the universe of valid values for this
    argument.

    A single range is the most common, although it is possible to define
    multiple ranges when the valid values are not contiguous.

    :ivar valid_range: A valid range constrains the whole set of
        possible values that could be encoded by the data type to a more
        "valid" or "reasonable" set of values.  This should be treated
        as a boundary check in an implementation to validate the input
        or output value.  Typically, only 1 range is used.  In cases
        where multiple ranges are used, then the value is valid when it
        is valid in any of the provided ranges.  Implementations may
        also use these ranges to enhance user interface displays and
        other visualization widgets as appropriate for the type.
    :ivar valid_range_applies_to_calibrated: By default and general
        recommendation, the valid range is specified in
        engineering/calibrated values, although this can be adjusted.
    """

    valid_range: List[IntegerRangeType] = field(
        default_factory=list,
        metadata={
            "name": "ValidRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )
    valid_range_applies_to_calibrated: bool = field(
        default=True,
        metadata={
            "name": "validRangeAppliesToCalibrated",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentComparisonCheckType(BaseConditionsType):
    """
    Identical to ComparisonCheckType but supports argument instance references.

    :ivar parameter_instance_ref: Left hand side parameter instance.
    :ivar argument_instance_ref: Left hand side argument instance.
    :ivar comparison_operator: Comparison operator.
    :ivar value: Specify as: integer data type using xs:integer, float
        data type using xs:double, string data type using xs:string,
        boolean data type using xs:boolean, binary data type using
        xs:hexBinary, enum data type using label name, relative time
        data type using xs:duration, absolute time data type using
        xs:dateTime.  Values must not exceed the characteristics for the
        data type or this is a validation error. Takes precedence over
        an initial value given in the data type. Values are calibrated
        unless there is an option to override it.
    """

    parameter_instance_ref: List[ParameterInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    argument_instance_ref: List[ArgumentInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "ArgumentInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "max_occurs": 2,
            "sequential": True,
        },
    )
    comparison_operator: Optional[ComparisonOperatorsType] = field(
        default=None,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentComparisonType:
    """
    Identical to ComparisonType but supports argument instance references.

    :ivar parameter_instance_ref: This parameter instance is being
        compared to the value in the parent element using the comparison
        defined there also.
    :ivar argument_instance_ref: This argument instance is being
        compared to the value in the parent element using the comparison
        defined there also.
    :ivar comparison_operator: Comparison operator to use with equality
        being the common default.
    :ivar value: Specify as: integer data type using xs:integer, float
        data type using xs:double, string data type using xs:string,
        boolean data type using xs:boolean, binary data type using
        xs:hexBinary, enum data type using label name, relative time
        data type using xs:duration, absolute time data type using
        xs:dateTime.  Values must not exceed the characteristics for the
        data type or this is a validation error. Takes precedence over
        an initial value given in the data type. Values are calibrated
        unless there is an option to override it.
    """

    parameter_instance_ref: Optional[ParameterInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    argument_instance_ref: Optional[ArgumentInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ArgumentInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    comparison_operator: ComparisonOperatorsType = field(
        default=ComparisonOperatorsType.VALUE,
        metadata={
            "name": "comparisonOperator",
            "type": "Attribute",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ArgumentDynamicValueType:
    """
    Identical to DynamicValueType but supports argument instance references.

    :ivar argument_instance_ref: Retrieve the value by referencing the
        value of an Argument.
    :ivar parameter_instance_ref: Retrieve the value by referencing the
        value of a Parameter.
    :ivar linear_adjustment: A slope and intercept may be applied to
        scale or shift the value selected from the argument or
        parameter.
    """

    argument_instance_ref: Optional[ArgumentInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ArgumentInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_instance_ref: Optional[ParameterInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    linear_adjustment: Optional[LinearAdjustmentType] = field(
        default=None,
        metadata={
            "name": "LinearAdjustment",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class BaseAlarmType:
    """Supplies an optional non-reference-able name and short description for
    alarms.

    Also includes an optional ancillary data for any special local
    flags, note that these may not necessarily transfer to another
    recipient of an instance document.

    :ivar ancillary_data_set:
    :ivar name: The alarm definition may be named.
    :ivar short_description: An optional brief description of this alarm
        definition.
    """

    ancillary_data_set: Optional[AncillaryDataSetType] = field(
        default=None,
        metadata={
            "name": "AncillaryDataSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Attribute",
        },
    )


@dataclass
class BaseCalibratorType:
    """Supplies an optional non-reference-able name and short description for
    calibrators.

    Also includes an optional ancillary data for any special local
    flags, note that these may not necessarily transfer to another
    recipient of an instance document.

    :ivar ancillary_data_set: Optional additional ancillary information
        for this calibrator/algorithm
    :ivar name: Optional name for this calibrator/algorithm
    :ivar short_description: Optional description for this
        calibrator/algorithm
    """

    ancillary_data_set: Optional[AncillaryDataSetType] = field(
        default=None,
        metadata={
            "name": "AncillaryDataSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Attribute",
        },
    )


@dataclass
class BaseMetaCommandType:
    """When specified, a BaseMetaCommand element identifies that this
    MetaCommand inherits (extends) another MetaCommand.

    It’s required ArgumentAssignmentList narrows or this command from
    the parent.  This is typically used when specializing a generic
    MetaCommand to a specific MetaCommand.  See MetaCommandType.

    :ivar argument_assignment_list: Argument Assignments specialize a
        MetaCommand or BlockMetaCommand when inheriting from another
        MetaCommand.  General argument values can be restricted to
        specific values to further specialize the MetaCommand.
    :ivar meta_command_ref: Reference to the MetaCommand definition that
        this MetaCommand extends.
    """

    argument_assignment_list: Optional[ArgumentAssignmentListType] = field(
        default=None,
        metadata={
            "name": "ArgumentAssignmentList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    meta_command_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "metaCommandRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ComparisonCheckType(BaseConditionsType):
    """
    Describe the comparison between the instance (value) of a parameter against
    either a specified value or another parameter instance.

    :ivar parameter_instance_ref: Left hand side parameter instance.
    :ivar comparison_operator: Comparison operator.
    :ivar value: Right hand side value.  Specify as: integer data type
        using xs:integer, float data type using xs:double, string data
        type using xs:string, boolean data type using xs:boolean, binary
        data type using xs:hexBinary, enum data type using label name,
        relative time data type using xs:duration, absolute time data
        type using xs:dateTime.  Values must not exceed the
        characteristics for the data type or this is a validation error.
        Takes precedence over an initial value given in the data type.
        Values are calibrated unless there is an option to override it.
    """

    parameter_instance_ref: List[ParameterInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "max_occurs": 2,
        },
    )
    comparison_operator: Optional[ComparisonOperatorsType] = field(
        default=None,
        metadata={
            "name": "ComparisonOperator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ComparisonType(ParameterInstanceRefType):
    """A simple ParameterInstanceRef to value comparison.

    The string supplied in the value attribute needs to be converted to
    a type matching the Parameter being compared to.  Numerical values
    are assumed to be base 10 unless proceeded by 0x (hexadecimal), 0o
    (octal), or 0b (binary).  The value is truncated  to use the least
    significant bits that match the bit size of the Parameter being
    compared to.

    :ivar comparison_operator: Operator to use for the comparison with
        the common equality operator as the default.
    :ivar value: Specify value as a string compliant with the XML schema
        (xs) type specified for each XTCE type: integer=xs:integer;
        float=xs:double; string=xs:string; boolean=xs:boolean;
        binary=xs:hexBinary; enum=xs:string from EnumerationList;
        relative time= xs:duration; absolute time=xs:dateTime.  Supplied
        value must be within the ValidRange specified for the type.
    """

    comparison_operator: ComparisonOperatorsType = field(
        default=ComparisonOperatorsType.VALUE,
        metadata={
            "name": "comparisonOperator",
            "type": "Attribute",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DescriptionType:
    """Defines an abstract schema type used as basis for NameDescriptionType
    and OptionalNameDescriptionType, includes an attribute for a short
    description and an element for a longer unbounded description.

    This type also provides alias set and ancillary data set  See
    AliasSetType and AncillaryDataSetType.

    :ivar long_description: Optional long form description to be used
        for explanatory descriptions of this item and may include HTML
        markup using CDATA.  Long Descriptions are of unbounded length.
    :ivar alias_set: Used to contain an alias (alternate) name or ID for
        this item.   See AliasSetType for additional explanation.
    :ivar ancillary_data_set: Use for any non-standard data associated
        with this named item.  See AncillaryDataSetType for additional
        explanation.
    :ivar short_description: Optional short description to be used for
        explanation of this item.  It is recommended that the short
        description be kept under 80 characters in length.
    """

    long_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LongDescription",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    alias_set: Optional[AliasSetType] = field(
        default=None,
        metadata={
            "name": "AliasSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    ancillary_data_set: Optional[AncillaryDataSetType] = field(
        default=None,
        metadata={
            "name": "AncillaryDataSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Attribute",
        },
    )


@dataclass
class DynamicValueType:
    """Uses a parameter instance to obtain the value.

    The parameter value may be optionally adjusted by a Linear function
    or use a series of boolean expressions to lookup the value.
    Anything more complex and a DynamicValue with a CustomAlgorithm may
    be used

    :ivar parameter_instance_ref: Retrieve the value by referencing the
        value of a Parameter.
    :ivar linear_adjustment: A slope and intercept may be applied to
        scale or shift the value selected from the argument or
        parameter.
    """

    parameter_instance_ref: Optional[ParameterInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    linear_adjustment: Optional[LinearAdjustmentType] = field(
        default=None,
        metadata={
            "name": "LinearAdjustment",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class EnumerationAlarmListType:
    """
    :ivar enumeration_alarm: Describe an alarm state for an enumeration
        label where the label is engineer/calibrated value. Note that
        labels may represent multiple raw/uncalbrated values.
    """

    enumeration_alarm: List[EnumerationAlarmLevelType] = field(
        default_factory=list,
        metadata={
            "name": "EnumerationAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class InputParameterInstanceRefType(ParameterInstanceRefType):
    """Names an input parameter to the algorithm.

    There are two attributes to InputParm, inputName and parameterName.
    parameterName is a parameter reference name for a parameter that
    will be used in this algorithm.  inputName is an optional "friendly"
    name for the input parameter.
    """

    input_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputName",
            "type": "Attribute",
        },
    )


@dataclass
class MetaCommandStepType:
    """Describe a MetaCommand step, consisting MetaCommand reference and
    argument list.

    See MetaCommandStepListType and NameReferenceType.
    """

    argument_assigment_list: Optional[ArgumentAssignmentListType] = field(
        default=None,
        metadata={
            "name": "ArgumentAssigmentList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    meta_command_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "metaCommandRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class OutputSetType:
    output_parameter_ref: List[OutputParameterRefType] = field(
        default_factory=list,
        metadata={
            "name": "OutputParameterRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ParametersToSuspendAlarmsOnSetType:
    """Sometimes it is necessary to suspend alarms - particularly 'change' alarms for commands that will change the value of a Parameter"""

    parameter_to_suspend_alarms_on: List[ParameterToSuspendAlarmsOnType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterToSuspendAlarmsOn",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class RateInStreamWithStreamNameType(RateInStreamType):
    """Define the expected appearance (rate) of a container in a named stream
    where the rate is defined on either a perSecond or perContainer update
    basis.

    Many programs and platforms have variable reporting rates for
    containers and these can be commanded.  As a result, this element is
    only useful to some users and generally does not affect the
    processing of the received containers themselves.  See ContainerType
    and RateInStreamType.

    :ivar stream_ref: Reference to a named stream for which this rate
        specification applies.
    """

    stream_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "streamRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ReferenceTimeType:
    """Most time values are relative to another time e.g. seconds are relative
    to minutes, minutes are relative to hours.

    This type is used to describe this relationship starting with the
    least significant time Parameter to and progressing to the most
    significant time parameter.

    :ivar offset_from:
    :ivar epoch: Epochs may be specified as an xs date where time is
        implied to be 00:00:00, xs dateTime, or string enumeration of
        common epochs.  The enumerations are TAI (used by CCSDS and
        others), J2000, UNIX (also known as POSIX), and GPS.
    """

    offset_from: Optional[ParameterInstanceRefType] = field(
        default=None,
        metadata={
            "name": "OffsetFrom",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    epoch: Optional[Union[XmlDate, XmlDateTime, EpochTimeEnumsType]] = field(
        default=None,
        metadata={
            "name": "Epoch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class StringAlarmListType:
    """Describe an ordered collection of string alarms, where duplicates are
    valid.

    Evaluate the alarms in list order. The first to evaluate to true
    takes precedence.  See StringAlarmLevelType.
    """

    string_alarm: List[StringAlarmLevelType] = field(
        default_factory=list,
        metadata={
            "name": "StringAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class TimeAssociationType(ParameterInstanceRefType):
    """Describes a time association consisting of an instance of an absolute
    time parameter (parameterRef) and this entry.

    Because telemetry parameter instances are oftentimes "time-tagged"
    with a timing signal either provided on the ground or on the space
    system.  This data element allows one to specify which of possibly
    many AbsoluteTimeParameters to use to "time-tag" parameter instances
    with.  See AbsoluteTimeParameterType.

    :ivar interpolate_time: If true, then the current value of the
        AbsoluteTime will be projected to current time.  In other words,
        if the value of the AbsoluteTime parameter was set 10 seconds
        ago, then 10 seconds will be added to its value before
        associating this time with the parameter.
    :ivar offset: The offset is used to supply a relative time offset
        from the time association and to this parameter
    :ivar unit: Specify the units the offset is in, the default is
        si_second.
    """

    interpolate_time: bool = field(
        default=True,
        metadata={
            "name": "interpolateTime",
            "type": "Attribute",
        },
    )
    offset: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit: TimeAssociationUnitType = field(
        default=TimeAssociationUnitType.SI_SECOND,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ToStringType:
    """
    :ivar number_format: This element describes how a numeric value
        should be represented in engineering/calibrated form.  The
        defaults reflect the most common form.
    """

    number_format: Optional[NumberFormatType] = field(
        default=None,
        metadata={
            "name": "NumberFormat",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class TriggerSetType:
    """A trigger is used to initiate the processing of some algorithm.

    A trigger may be based on an update of a Parameter, receipt of a
    Container, or on a time basis.  Triggers may also have a maximum
    rate that limits how often the trigger can be invoked.

    :ivar on_parameter_update_trigger: This element instructs the
        trigger to invoke the algorithm evaluation when a Parameter
        update is received.
    :ivar on_container_update_trigger: This element instructs the
        trigger to invoke the algorithm evaluation when a Container is
        received.
    :ivar on_periodic_rate_trigger: This element instructs the trigger
        to invoke the algorithm evaluation using a timer.
    :ivar name: Triggers may optionally be named.
    :ivar trigger_rate: This attribute is a maximum rate that constrains
        how quickly this trigger may evaluate the algorithm to avoid
        flooding the implementation.  The default is once per second.
        Setting to 0 results in no maximum.
    """

    on_parameter_update_trigger: List[OnParameterUpdateTriggerType] = field(
        default_factory=list,
        metadata={
            "name": "OnParameterUpdateTrigger",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    on_container_update_trigger: List[OnContainerUpdateTriggerType] = field(
        default_factory=list,
        metadata={
            "name": "OnContainerUpdateTrigger",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    on_periodic_rate_trigger: List[OnPeriodicRateTriggerType] = field(
        default_factory=list,
        metadata={
            "name": "OnPeriodicRateTrigger",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    trigger_rate: int = field(
        default=1,
        metadata={
            "name": "triggerRate",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )


@dataclass
class UnitSetType:
    """Describe an ordered collection of units that form a unit-expression.

    Units may be described for both calibrated/engineering values and
    also potentially uncalibrated/raw values.  See UnitType.

    :ivar unit: Describe the exponent, factor, form, and description for
        a unit.  The attributes are optional because different programs
        use this element in different ways, depending on vendor support.
    """

    unit: List[UnitType] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class AlarmMultiRangesType(BaseAlarmType):
    """Describe any number of alarm ranges, each with its own level (normal,
    warning, watch, distress, critical, severe) and range form (inside or
    outside).

    Ranges may overlap, be disjoint and so forth. Ranges within the
    value sprectrum non-specified are non-normal. The most severe range
    level of value within the ranges is the level of the alarm. Range
    values are in calibrated engineering units. See FloatRangeType.

    :ivar range: Describe any number of alarm ranges, each with its own
        level (normal, warning, watch, distress, critical, severe) and
        range form (inside or outside). Ranges may overlap, be disjoint
        and so forth. Ranges within the value sprectrum non-specified
        are non-normal. The most severe range level of value within the
        ranges is the level of the alarm. Range values are in calibrated
        engineering units. See FloatRangeType.
    """

    range: List[MultiRangeType] = field(
        default_factory=list,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class AlarmRangesType(BaseAlarmType):
    """Describe up to six ranges where either less severe ranges are a subset
    of more severe ranges (outside), or more severe ranges are a subset of less
    severe ranges (inside).

    In both forms, the undefined least severe range is normal. Range
    values are in calibrated engineering units. See FloatRangeType.

    :ivar watch_range: A range of least concern. Considered to be below
        the most commonly used Warning level.
    :ivar warning_range: A range of concern that represents the most
        commonly used minimum concern level for many software
        applications.
    :ivar distress_range: A range of concern in between the most
        commonly used Warning and Critical levels.
    :ivar critical_range: A range of concern that represents the most
        commonly used maximum concern level for many software
        applications.
    :ivar severe_range: A range of highest concern. Considered to be
        above the most commonly used Critical level.
    :ivar range_form: A value of outside specifies that the most severe
        range is outside all the other ranges: -severe -critical
        -distress -warning -watch normal +watch +warning +distress
        +critical +severe. A value of inside "inverts" these bands:
        -green -watch -warning -distress -critical severe +critical
        +distress +warning +watch. The most common form used is
        "outside" and is the default.
    """

    watch_range: Optional[FloatRangeType] = field(
        default=None,
        metadata={
            "name": "WatchRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    warning_range: Optional[FloatRangeType] = field(
        default=None,
        metadata={
            "name": "WarningRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    distress_range: Optional[FloatRangeType] = field(
        default=None,
        metadata={
            "name": "DistressRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    critical_range: Optional[FloatRangeType] = field(
        default=None,
        metadata={
            "name": "CriticalRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    severe_range: Optional[FloatRangeType] = field(
        default=None,
        metadata={
            "name": "SevereRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    range_form: RangeFormType = field(
        default=RangeFormType.OUTSIDE,
        metadata={
            "name": "rangeForm",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentComparisonListType:
    """
    Identical to ComparisonListType but supports argument instance references.

    :ivar comparison: List of Comparison elements must all be true for
        the comparison to evaluate to true.
    """

    comparison: List[ArgumentComparisonType] = field(
        default_factory=list,
        metadata={
            "name": "Comparison",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ArgumentInputSetType:
    """
    Identical to InputSetType but supports argument instance references.

    :ivar input_parameter_instance_ref: Reference a parameter to serve
        as an input to the algorithm.
    :ivar input_argument_instance_ref: Reference an argument to serve as
        an input to the algorithm.
    """

    input_parameter_instance_ref: List[InputParameterInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "InputParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    input_argument_instance_ref: List[ArgumentInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "InputArgumentInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentOredConditionsType(BaseConditionsType):
    """
    Identical to ORedConditionsType but supports argument instance references.

    :ivar condition: Condition elements describe a test similar to the
        Comparison element except that the arguments/parameters used
        have additional flexibility for the compare.
    :ivar anded_conditions: This element describes tests similar to the
        ComparisonList element except that the arguments/parameters used
        are more flexible and the and/or for multiple checks can be
        specified.
    """

    class Meta:
        name = "ArgumentORedConditionsType"

    condition: List[ArgumentComparisonCheckType] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )
    anded_conditions: List["ArgumentAndedConditionsType"] = field(
        default_factory=list,
        metadata={
            "name": "ANDedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )


@dataclass
class ComparisonListType:
    """
    All comparisons must be true.

    :ivar comparison: List of Comparison elements must all be true for
        the comparison to evaluate to true.
    """

    comparison: List[ComparisonType] = field(
        default_factory=list,
        metadata={
            "name": "Comparison",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class InputSetType:
    input_parameter_instance_ref: List[InputParameterInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "InputParameterInstanceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    constant: List[ConstantType] = field(
        default_factory=list,
        metadata={
            "name": "Constant",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class MathOperationCalibratorType(BaseCalibratorType):
    """
    Describe a mathematical function for calibration where the mathematical
    function is defined using the MathOperationType.

    :ivar value_operand: Use a constant in the calculation.
    :ivar this_parameter_operand: Use the value of this parameter in the
        calculation. It is the calibrator's value only.  If the raw
        value is needed, specify it explicitly using
        ParameterInstanceRefOperand. Note this element has no content.
    :ivar operator: All operators utilize operands on the top values in
        the stack and leaving the result on the top of the stack.
        Ternary operators utilize the top three operands on the stack,
        binary operators utilize the top two operands on the stack, and
        unary operators use the top operand on the stack.
    :ivar parameter_instance_ref_operand: This element is used to
        reference the last received/assigned value of any Parameter in
        this math operation.
    """

    value_operand: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueOperand",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    this_parameter_operand: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ThisParameterOperand",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    operator: List[MathOperatorsType] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_instance_ref_operand: List[ParameterInstanceRefType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterInstanceRefOperand",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class MetaCommandStepListType:
    """Describe the list of MetaCommand definitions that form the block
    command.

    Contains an ordered list of MetaCommandSteps where each step is a
    MetaCommand with associated arguments, duplicates are valid.  See
    BlockMetaCommandType.

    :ivar meta_command_step: A MetaCommand with specific specified
        argument values to include in the BlockMetaCommand.
    """

    meta_command_step: List[MetaCommandStepType] = field(
        default_factory=list,
        metadata={
            "name": "MetaCommandStep",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class NameDescriptionType(DescriptionType):
    """Defines a base schema type definition used by many other schema types
    throughout schema.

    Use it to describe a name with optional descriptions, aliases, and
    ancillary data.  See NameType, LongDescriptionType,
    ShortDescriptionType, AliasSetType and AncillaryDataSetType.

    :ivar name: The name of this defined item.  See NameType for
        restriction information.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^./:\[\] ]+",
        },
    )


@dataclass
class OredConditionsType(BaseConditionsType):
    """Describe two or more conditions that are logically ored together.

    Conditions may be a mix of Condition and ANDedCondition.   See
    ORedConditionType and BooleanExpressionType.

    :ivar condition: Condition elements describe a test similar to the
        Comparison element except that the parameters used have
        additional flexibility for the compare.
    :ivar anded_conditions: This element describes tests similar to the
        ComparisonList element except that the parameters used are more
        flexible and the and/or for multiple checks can be specified.
    """

    class Meta:
        name = "ORedConditionsType"

    condition: List[ComparisonCheckType] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )
    anded_conditions: List["AndedConditionsType"] = field(
        default_factory=list,
        metadata={
            "name": "ANDedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )


@dataclass
class OptionalNameDescriptionType(DescriptionType):
    """
    The type definition used by most elements that have an optional name with
    optional descriptions.

    :ivar name: Optional name of this defined item.  See NameType for
        restriction information.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^./:\[\] ]+",
        },
    )


@dataclass
class PercentCompleteType:
    """Describe a percentage complete that is fixed from 0 to 100, or as value
    from a parameter.

    See ExecutionVerifierType.

    :ivar fixed_value: 0 to 100 percent
    :ivar dynamic_value: Uses a parameter instance to obtain the value.
        The parameter value may be optionally adjusted by a Linear
        function or use a series of boolean expressions to lookup the
        value. Anything more complex and a DynamicValue with a
        CustomAlgorithm may be used.
    """

    fixed_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "FixedValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    dynamic_value: Optional[DynamicValueType] = field(
        default=None,
        metadata={
            "name": "DynamicValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class PolynomialCalibratorType(BaseCalibratorType):
    """Describe a polynomial equation for calibration.

    This is a calibration type where a curve in a raw vs calibrated
    plane is described using a set of polynomial coefficients.  Raw
    values are converted to calibrated values by finding a position on
    the curve corresponding to the raw value. The first coefficient
    belongs with the X^0 term, the next coefficient belongs to the X^1
    term and so on. See CalibratorType.

    :ivar term: A single term in the polynomial function.
    """

    term: List[TermType] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class RateInStreamSetType:
    rate_in_stream: List[RateInStreamWithStreamNameType] = field(
        default_factory=list,
        metadata={
            "name": "RateInStream",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class SplineCalibratorType(BaseCalibratorType):
    """Describe a spline function for calibration using a set of at least 2
    points.

    Raw values are converted to calibrated values by finding a position
    on the line corresponding to the raw value.  The line may be
    interpolated and/or extrapolated as needed. The interpolation order
    may be specified for all the points and overridden on individual
    points.  The algorithm triggers on the input parameter. See
    CalibratorType.

    :ivar spline_point: Describes a single point of the spline or
        piecewise function.
    :ivar order: The interpolation order to apply to the overall spline
        function.  Order 0 is no slope between the points (flat).  Order
        1 is linear interpolation.  Order 2 would be quadratic and in
        this special case, 3 points would be required, etc.
    :ivar extrapolate: Extrapolation allows the closest outside point
        and the associated interpolation to extend outside of the range
        of the points in the spline function.
    """

    spline_point: List[SplinePointType] = field(
        default_factory=list,
        metadata={
            "name": "SplinePoint",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )
    order: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    extrapolate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AndedConditionsType(BaseConditionsType):
    """Describe two or more conditions that are logically anded together.

    Conditions may be a mix of Condition and ORedCondition.   See
    ORedConditionType and BooleanExpressionType.

    :ivar condition: Condition elements describe a test similar to the
        Comparison element except that the parameters used have
        additional flexibility for the compare.
    :ivar ored_conditions: This element describes tests similar to the
        ComparisonList element except that the parameters used are more
        flexible and the and/or for multiple checks can be specified.
    """

    class Meta:
        name = "ANDedConditionsType"

    condition: List[ComparisonCheckType] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )
    ored_conditions: List[OredConditionsType] = field(
        default_factory=list,
        metadata={
            "name": "ORedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )


@dataclass
class ArgumentAndedConditionsType(BaseConditionsType):
    """
    Identical to ANDedConditionsType but supports argument instance references.

    :ivar condition: Condition elements describe a test similar to the
        Comparison element except that the arguments/parameters used
        have additional flexibility for the compare.
    :ivar ored_conditions: This element describes tests similar to the
        ComparisonList element except that the arguments/parameters used
        are more flexible and the and/or for multiple checks can be
        specified.
    """

    class Meta:
        name = "ArgumentANDedConditionsType"

    condition: List[ArgumentComparisonCheckType] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )
    ored_conditions: List[ArgumentOredConditionsType] = field(
        default_factory=list,
        metadata={
            "name": "ORedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 2,
        },
    )


@dataclass
class ArgumentType(NameDescriptionType):
    """An Argument has a name and can take on values with the underlying value
    type described by the ArgumentTypeRef.

    Describe the properties of a command argument referring to a data
    type (argument type). The bulk of properties associated with a
    command argument are in its argument type. The initial value
    specified here, overrides the initial value in the argument type.
    See BaseDataType, BaseTimeDataType and NameReferenceType.

    :ivar argument_type_ref: Specify the reference to the argument type
        from the ArgumentTypeSet area using the path reference rules,
        either local to this SpaceSystem, relative, or absolute.
    :ivar initial_value: Specify as: integer data type using xs:integer,
        float data type using xs:double, string data type using
        xs:string, boolean data type using xs:boolean, binary data type
        using xs:hexBinary, enum data type using label name, relative
        time data type using xs:duration, absolute time data type using
        xs:dateTime.  Values must not exceed the characteristics for the
        data type or this is a validation error. Takes precedence over
        an initial value given in the data type. Values are calibrated
        unless there is an option to override it.
    """

    argument_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "argumentTypeRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class ArrayDataTypeType(NameDescriptionType):
    """A base schema type for describing an array data type.

    The number of and size of each dimension is defined in its two child
    types. See NameReferenceType, ArrayArgumentType and
    ArrayParameterType.

    :ivar array_type_ref: Reference to the data type that represents the
        type of the elements for this array.
    """

    array_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "arrayTypeRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class BlockMetaCommandType(NameDescriptionType):
    """Describe an ordered grouping of MetaCommands into a list, duplicates are
    valid.

    The block contains argument values fully specified.  See
    MetaCommandStepListType.

    :ivar meta_command_step_list: List of the MetaCommands to include in
        this BlockMetaCommand.
    """

    meta_command_step_list: Optional[MetaCommandStepListType] = field(
        default=None,
        metadata={
            "name": "MetaCommandStepList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class CalibratorType(BaseCalibratorType):
    """
    Describe a calibrator to transform a source data type raw/uncalibrated
    value (e.g. an integer count from a spacecraft) to an engineering
    unit/calibrated value for users (e.g. a float).

    :ivar spline_calibrator: Describes a calibrator in the form of a
        piecewise defined function
    :ivar polynomial_calibrator: Describes a calibrator in the form of a
        polynomial function
    :ivar math_operation_calibrator: Describes a calibrator in the form
        of a user/program/implementation defined function
    """

    spline_calibrator: Optional[SplineCalibratorType] = field(
        default=None,
        metadata={
            "name": "SplineCalibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    polynomial_calibrator: Optional[PolynomialCalibratorType] = field(
        default=None,
        metadata={
            "name": "PolynomialCalibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    math_operation_calibrator: Optional[MathOperationCalibratorType] = field(
        default=None,
        metadata={
            "name": "MathOperationCalibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ChangeAlarmRangesType(AlarmRangesType):
    """Describe an alarm when the parameter value's rate-of-change is either
    too fast or too slow.

    The change may be with respect to time (the default) or with respect
    to samples (delta alarms). Use the changeType attribute to select
    the type: changePerSecond (time) or changePerSample (delta). The
    change may also be ether relative (as a percentage change) or
    absolute as set by the changeBasis attribute. (Delta alarms are
    typically absolute but percentage is conceivable). The alarm also
    requires the spanOfInterest in both samples and seconds to have
    passed before it is to trigger. For time based rate of change
    alarms, the time specified in spanOfInterestInSeconds is used to
    calculate the change. For sample based rate of change alarms, the
    change is calculated over the number of samples specified in
    spanOfInterestInSamples. A typical delta alarm would set:
    changeType=changePerSample, changeBasis=absoluteChange,
    spanOfInterestInSamples=1. A typical time based version would set:
    changeType=changePerSecond, changeBasis=percentageChange, and
    spaceOfInterestInSeconds=1. To set the ranges use maxInclusive, the
    following definition applies: | Normal.maxInclusive | &lt;= |
    Watch.maxInclusive | &lt;= | Warning.maxInclusive | &lt;= |
    Distress.maxInclusive | &lt;= | Critical.maxInclusive | &lt;= |
    Severe.maxInclusive |. And it is further assumed the absolute value
    of each range and sampled value it taken to evaluate the alarm. See
    NumericAlarmType.
    """

    change_type: ChangeSpanType = field(
        default=ChangeSpanType.CHANGE_PER_SECOND,
        metadata={
            "name": "changeType",
            "type": "Attribute",
        },
    )
    change_basis: ChangeBasisType = field(
        default=ChangeBasisType.ABSOLUTE_CHANGE,
        metadata={
            "name": "changeBasis",
            "type": "Attribute",
        },
    )
    span_of_interest_in_samples: int = field(
        default=1,
        metadata={
            "name": "spanOfInterestInSamples",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    span_of_interest_in_seconds: float = field(
        default=0.0,
        metadata={
            "name": "spanOfInterestInSeconds",
            "type": "Attribute",
        },
    )


@dataclass
class MathOperationType(MathOperationCalibratorType):
    """Postfix (aka Reverse Polish Notation (RPN)) notation is used to describe
    mathmatical equations.

    It uses a stack where operands (either fixed values or
    ParameterInstances) are pushed onto the stack from first to last in
    the XML. As the operators are specified, each pops off operands as
    it evaluates them, and pushes the result back onto the stack. In
    this case postfix is used to avoid having to specify parenthesis. To
    convert from infix to postfix, use Dijkstra's "shunting yard"
    algorithm.
    """


@dataclass
class MemberType(NameDescriptionType):
    """Describe a member field in an AggregateDataType.

    Each member has a name and a type reference to a data type for the
    aggregate member name.  If this aggregate is a Parameter aggregate,
    then the typeRef is a parameter type reference.  If this aggregate
    is an Argument aggregate, then the typeRef is an argument type
    reference.  References to an array data type is currently not
    supported. Circular references are not allowed.  See MemberListType.
    AggregateParameterType and AggregateArgumentType.

    :ivar type_ref:
    :ivar initial_value: Used to set the initial calibrated values of
        Parameters.  Will overwrite an initial value defined for the
        ParameterType.  For integer types base 10 (decimal) form is
        assumed unless: if proceeded by a 0b or 0B, value is in base two
        (binary form, if proceeded by a 0o or 0O, values is in base 8
        (octal) form, or if proceeded by a 0x or 0X, value is in base 16
        (hex) form.  Floating point types may be specified in normal
        (100.0) or scientific (1.0e2) form.  Time types are specified
        using the ISO 8601 formats described for XTCE time data types.
        Initial values for string types, may include C language style
        (\\n, \\t, \\", \\\\, etc.) escape sequences.
    """

    type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class PcmstreamType(NameDescriptionType):
    """
    A PCM Stream Type is the high level definition for all Pulse Code Modulated
    (PCM) (i.e., binary) streams.
    """

    class Meta:
        name = "PCMStreamType"

    bit_rate_in_bps: Optional[float] = field(
        default=None,
        metadata={
            "name": "bitRateInBPS",
            "type": "Attribute",
        },
    )
    pcm_type: Pcmtype = field(
        default=Pcmtype.NRZL,
        metadata={
            "name": "pcmType",
            "type": "Attribute",
        },
    )
    inverted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ServiceType(NameDescriptionType):
    """
    Holds a set of services, logical groups of containers  OR messages (not
    both).
    """

    message_ref_set: Optional[MessageRefSetType] = field(
        default=None,
        metadata={
            "name": "MessageRefSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_ref_set: Optional[ContainerRefSetType] = field(
        default=None,
        metadata={
            "name": "ContainerRefSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class SimpleAlgorithmType(NameDescriptionType):
    """The simplest form of algorithm, a SimpleAlgorithmType contains an area
    for a free-form pseudo code description of the algorithm plus a Set of
    references to external algorithms.

    External algorithms are usually unique to a ground system type.
    Multiple external algorithms are possible because XTCE documents may
    be used across multiple ground systems.
    """

    algorithm_text: Optional[AlgorithmTextType] = field(
        default=None,
        metadata={
            "name": "AlgorithmText",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    external_algorithm_set: Optional[ExternalAlgorithmSetType] = field(
        default=None,
        metadata={
            "name": "ExternalAlgorithmSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class TimeAlarmRangesType(AlarmRangesType):
    time_units: TimeUnitsType = field(
        default=TimeUnitsType.SECONDS,
        metadata={
            "name": "timeUnits",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentBooleanExpressionType:
    """
    Identical to BooleanExpressionType but supports argument instance
    references.

    :ivar condition: Condition elements describe a test similar to the
        Comparison element except that the arguments/parameters used
        have additional flexibility.
    :ivar anded_conditions: This element describes tests similar to the
        ComparisonList element except that the arguments/parameters used
        are more flexible.
    :ivar ored_conditions: This element describes tests similar to the
        ComparisonList element except that the arguments/parameters used
        are more flexible.
    """

    condition: Optional[ArgumentComparisonCheckType] = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    anded_conditions: Optional[ArgumentAndedConditionsType] = field(
        default=None,
        metadata={
            "name": "ANDedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    ored_conditions: Optional[ArgumentOredConditionsType] = field(
        default=None,
        metadata={
            "name": "ORedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentInputAlgorithmType(SimpleAlgorithmType):
    """
    Identical to InputAlgorithmType but supports argument instance references.

    :ivar input_set: The InputSet describes the list of arguments and/or
        parameters that should be made available as input arguments to
        the algorithm.
    """

    input_set: Optional[ArgumentInputSetType] = field(
        default=None,
        metadata={
            "name": "InputSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentListType:
    """
    Defines a list of Arguments for a command definition.

    :ivar argument: Defines an Argument for a command definition.
        Arguments are local to the MetaCommand, BlockMetaCommand, and
        those that inherit from the definition.
    """

    argument: List[ArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "Argument",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class BooleanExpressionType:
    """
    Holds an arbitrarily complex boolean expression.

    :ivar condition: Condition elements describe a test similar to the
        Comparison element except that the parameters used have
        additional flexibility.
    :ivar anded_conditions: This element describes tests similar to the
        ComparisonList element except that the parameters used are more
        flexible.
    :ivar ored_conditions: This element describes tests similar to the
        ComparisonList element except that the parameters used are more
        flexible.
    """

    condition: Optional[ComparisonCheckType] = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    anded_conditions: Optional[AndedConditionsType] = field(
        default=None,
        metadata={
            "name": "ANDedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    ored_conditions: Optional[OredConditionsType] = field(
        default=None,
        metadata={
            "name": "ORedConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class FrameStreamType(PcmstreamType):
    """
    The top level type definition for all data streams that are frame based.

    :ivar container_ref: This Container (usually abstract) is the
        container that is in the fixed frame stream.  Normally, this is
        a general container type from which many specific containers are
        inherited.
    :ivar service_ref:
    :ivar stream_ref: This is a reference to a connecting stream - say a
        custom stream.
    """

    container_ref: Optional[ContainerRefType] = field(
        default=None,
        metadata={
            "name": "ContainerRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    service_ref: Optional[ServiceRefType] = field(
        default=None,
        metadata={
            "name": "ServiceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    stream_ref: Optional[StreamRefType] = field(
        default=None,
        metadata={
            "name": "StreamRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class InputAlgorithmType(SimpleAlgorithmType):
    """
    A set of labeled inputs is added to the SimpleAlgorithmType.

    :ivar input_set: The InputSet describes the list of parameters that
        should be made available as input arguments to the algorithm.
    """

    input_set: Optional[InputSetType] = field(
        default=None,
        metadata={
            "name": "InputSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class MemberListType:
    """Order is important only if the name of the AggregateParameter or
    Aggregate Argument is directly referenced in SequenceContainers.

    In this case the members are assued to be added sequentially (in the
    order listed here) into the Container.
    """

    member: List[MemberType] = field(
        default_factory=list,
        metadata={
            "name": "Member",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ParameterToSetType(ParameterRefType):
    """
    Sets a Parameter to a new value (either from a derivation or explicitly)
    after the command has been verified (all verifications have passed).

    :ivar derivation: Specify a MathOperation to use to set the
        Parameter value.  See MathOperationType.
    :ivar new_value: Specify value as a string compliant with the XML
        schema (xs) type specified for each XTCE type:
        integer=xs:integer; float=xs:double; string=xs:string;
        boolean=xs:boolean; binary=xs:hexBinary; enum=xs:string from
        EnumerationList; relative time= xs:duration; absolute
        time=xs:dateTime.  Supplied value must be within the ValidRange
        specified for the Parameter and appropriate for the type.
    :ivar set_on_verification: This attribute provides more specific
        control over when the Parameter value is set.  By default, it is
        when the command have all verifications complete.  See
        VerifierEnumerationType.
    """

    derivation: Optional[MathOperationType] = field(
        default=None,
        metadata={
            "name": "Derivation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    new_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    set_on_verification: VerifierEnumerationType = field(
        default=VerifierEnumerationType.COMPLETE,
        metadata={
            "name": "setOnVerification",
            "type": "Attribute",
        },
    )


@dataclass
class ServiceSetType:
    """
    A service is a logical grouping of container and/or messages.
    """

    service: List[ServiceType] = field(
        default_factory=list,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class TriggeredMathOperationType(MathOperationType):
    trigger_set: Optional[TriggerSetType] = field(
        default=None,
        metadata={
            "name": "TriggerSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    output_parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputParameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class AggregateDataType(NameDescriptionType):
    """A base schema type for describing a complex data type analogous to a
    C-struct.

    Each field of the data type is called a Member.  Each Member is part
    of the MemberList which forms the list of items to be placed under
    this data type’s name.  The MemberList defines a data block and
    block’s size is defined by the DataEncodings of each Member’s type
    reference. The data members are ordered and contiguous in the
    MemberList element (packed).  Each member may be addressed by the
    dot syntax similar to C such as P.voltage if P is the referring
    parameter and voltage is of a member of P’s aggregate type.  See
    MemberType, MemberListType, DataEncodingType, NameReferenceType,
    AggregateParameterType and AggregateArgumentType.

    :ivar member_list: Ordered list of the members of the
        aggregate/structure.  Members are contiguous.
    """

    member_list: Optional[MemberListType] = field(
        default=None,
        metadata={
            "name": "MemberList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ArgumentMatchCriteriaType:
    """
    Identical to MatchCriteriaType but supports argument instance references.

    :ivar comparison: A simple comparison check involving a single test
        of an argument or parameter value.
    :ivar comparison_list: A series of simple comparison checks with an
        implicit 'and' in that they all must be true for the overall
        condition to be true.
    :ivar boolean_expression: An arbitrarily complex boolean expression
        that has additional flexibility on the terms beyond the
        Comparison and ComparisonList elements.
    :ivar custom_algorithm: An escape to an externally defined
        algorithm.
    """

    comparison: Optional[ArgumentComparisonType] = field(
        default=None,
        metadata={
            "name": "Comparison",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    comparison_list: Optional[ArgumentComparisonListType] = field(
        default=None,
        metadata={
            "name": "ComparisonList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    boolean_expression: Optional[ArgumentBooleanExpressionType] = field(
        default=None,
        metadata={
            "name": "BooleanExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    custom_algorithm: Optional[ArgumentInputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "CustomAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class AutoInvertType:
    """After searching for the frame sync marker for some number of bits, it
    may be desirable to invert the incoming data, and then look for frame sync.

    In some cases this will require an external algorithm
    """

    invert_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "InvertAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    bad_frames_to_auto_invert: int = field(
        default=1024,
        metadata={
            "name": "badFramesToAutoInvert",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )


@dataclass
class CheckWindowAlgorithmsType:
    """Used by CommandVerifiers to limit the time allocated to check for the
    verification.

    See CommandVerifierType.
    """

    start_check: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "StartCheck",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    stop_time: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "StopTime",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ChecksumType:
    """
    Describe checksum information.

    :ivar input_algorithm: Assumed to return the computed checksum.
    :ivar bits_from_reference:
    :ivar reference:
    :ivar name: Qualified list of name checksum algorithms. If custom is
        chosen, InputAlgorithm must be set.
    :ivar hash_size_in_bits:
    """

    input_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "InputAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    bits_from_reference: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitsFromReference",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    reference: ReferencePointType = field(
        default=ReferencePointType.START,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[ChecksumTypeName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash_size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "hashSizeInBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )


@dataclass
class CustomAlarmType(BaseAlarmType):
    """Describe a custom, algorithmic alarm condition.

    The algorithm is assumed to return a boolean value: true or false.
    See AlarmType.

    :ivar input_algorithm: Algorithm returns a boolean.
    """

    input_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "InputAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class InputOutputAlgorithmType(InputAlgorithmType):
    """
    A set of labeled outputs are added to the SimpleInputAlgorithmType.
    """

    output_set: Optional[OutputSetType] = field(
        default=None,
        metadata={
            "name": "OutputSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    thread: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MatchCriteriaType:
    """
    Contains either a simple Comparison, a ComparisonList, an arbitrarily
    complex BooleanExpression or an escape to an externally defined algorithm.

    :ivar comparison: A simple comparison check involving a single test
        of a parameter value.
    :ivar comparison_list: A series of simple comparison checks with an
        implicit 'and' in that they all must be true for the overall
        condition to be true.
    :ivar boolean_expression: An arbitrarily complex boolean expression
        that has additional flexibility on the terms beyond the
        Comparison and ComparisonList elements.
    :ivar custom_algorithm: An escape to an externally defined
        algorithm.
    """

    comparison: Optional[ComparisonType] = field(
        default=None,
        metadata={
            "name": "Comparison",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    comparison_list: Optional[ComparisonListType] = field(
        default=None,
        metadata={
            "name": "ComparisonList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    boolean_expression: Optional[BooleanExpressionType] = field(
        default=None,
        metadata={
            "name": "BooleanExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    custom_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "CustomAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class MathAlgorithmType(NameDescriptionType):
    """Describe a postfix (Reverse Polish Notation (RPN)) notation based
    mathmatical equations.

    See MathOperationType.

    :ivar math_operation: The contents of the Math Operation as an
        algorithm definition in RPN.  See TriggeredMathOperationType.
    """

    math_operation: Optional[TriggeredMathOperationType] = field(
        default=None,
        metadata={
            "name": "MathOperation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ParameterToSetListType:
    """Parameters that are set with a new value after the command has been
    sent.

    Appended to the Base Command list
    """

    parameter_to_set: List[ParameterToSetType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterToSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class AggregateArgumentType(AggregateDataType):
    """Describe a complex data type analogous to a C-struct.

    Each field of the data type is called a Member.  Each Member is part
    of the MemberList which forms the list of items to be placed under
    this data type’s name.  The MemberList defines a data block and
    block’s size is defined by the DataEncodings of each Member’s type
    reference. The data members are ordered and contiguous in the
    MemberList element (packed).  Each member may be addressed by the
    dot syntax similar to C such as P.voltage if P is the referring
    parameter and voltage is of a member of P’s aggregate type.  See
    MemberType, MemberListType, DataEncodingType, NameReferenceType, and
    AggregateDataType.
    """


@dataclass
class AggregateParameterType(AggregateDataType):
    """Describe a complex data type analogous to a C-struct.

    Each field of the data type is called a Member.  Each Member is part
    of the MemberList which forms the list of items to be placed under
    this data type’s name.  The MemberList defines a data block and
    block’s size is defined by the DataEncodings of each Member’s type
    reference. The data members are ordered and contiguous in the
    MemberList element (packed).  Each member may be addressed by the
    dot syntax similar to C such as P.voltage if P is the referring
    parameter and voltage is of a member of P’s aggregate type.  See
    MemberType, MemberListType, DataEncodingType, NameReferenceType, and
    AggregateDataType.
    """


@dataclass
class AlarmConditionsType:
    """Describe up to six levels: Normal, Watch, Warning, Distress, Critical,
    and Severe of conditions the alarm will trigger when true.

    The types are conditions available are a single comparison, a
    comparison list, a discrete lookup list, and custom algorithm.   See
    MatchCriteriaType.

    :ivar watch_alarm: An alarm state of least concern.  Considered to
        be below the most commonly used Warning level.
    :ivar warning_alarm: An alarm state of concern that represents the
        most commonly used minimum concern level for many software
        applications.
    :ivar distress_alarm: An alarm state of concern in between the most
        commonly used Warning and Critical levels.
    :ivar critical_alarm: An alarm state of concern that represents the
        most commonly used maximum concern level for many software
        applications.
    :ivar severe_alarm: An alarm state of highest concern.  Considered
        to be above the most commonly used Critical level.
    """

    watch_alarm: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "WatchAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    warning_alarm: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "WarningAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    distress_alarm: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "DistressAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    critical_alarm: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "CriticalAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    severe_alarm: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "SevereAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentDiscreteLookupType(ArgumentMatchCriteriaType):
    """
    Identical to ArgumentDiscreteLookupType but supports argument instance
    references.

    :ivar value: Value to use when the lookup conditions are true.
    """

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CommandVerifierType(OptionalNameDescriptionType):
    """A command verifier is used to check that the command has been
    successfully executed.

    Command Verifiers may be either a Custom Algorithm or a Boolean
    Check or the presence of a Container for a relative change in the
    value of a Parameter.  The CheckWindow is a time period where the
    verification must test true to pass.

    :ivar comparison_list: Verification is a list of comparisons.
    :ivar container_ref: Verification is a new instance of the
        referenced container. For example, sending a command to download
        memory then receiving a packet with the memory download would be
        verified upon receipt of the packet.
    :ivar parameter_value_change: Verification is a telemetry parameter
        value change on the ground.  For example, a command counter.
    :ivar custom_algorithm: Verification is outside the scope of regular
        command and telemetry processing.
    :ivar boolean_expression: Verification is a boolean expression of
        conditions.
    :ivar comparison: Verification is a single comparison.
    :ivar check_window: Define a time window for checking for
        verification.
    :ivar check_window_algorithms: Define a time window algorithmically
        for verification.
    """

    comparison_list: Optional[ComparisonListType] = field(
        default=None,
        metadata={
            "name": "ComparisonList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_ref: Optional[ContainerRefType] = field(
        default=None,
        metadata={
            "name": "ContainerRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_value_change: Optional[ParameterValueChangeType] = field(
        default=None,
        metadata={
            "name": "ParameterValueChange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    custom_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "CustomAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    boolean_expression: Optional[BooleanExpressionType] = field(
        default=None,
        metadata={
            "name": "BooleanExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    comparison: Optional[ComparisonType] = field(
        default=None,
        metadata={
            "name": "Comparison",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    check_window: Optional[CheckWindowType] = field(
        default=None,
        metadata={
            "name": "CheckWindow",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    check_window_algorithms: Optional[CheckWindowAlgorithmsType] = field(
        default=None,
        metadata={
            "name": "CheckWindowAlgorithms",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ContextMatchType(MatchCriteriaType):
    """
    A MatchCriteriaType used for Context selection.
    """


@dataclass
class CustomStreamType(PcmstreamType):
    """A stream type where some level of custom processing (e.g. convolutional,
    encryption, compression) is performed.

    Has a reference to external algorithms for encoding and decoding
    algorithms.

    :ivar encoding_algorithm:
    :ivar decoding_algorithm: Algorithm outputs may be used to set
        decoding quality parameters.
    :ivar encoded_stream_ref:
    :ivar decoded_stream_ref:
    """

    encoding_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "EncodingAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    decoding_algorithm: Optional[InputOutputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "DecodingAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    encoded_stream_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "encodedStreamRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    decoded_stream_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "decodedStreamRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class DiscreteLookupType(MatchCriteriaType):
    """
    Describe a discrete value lookup and the value associated when the lookup
    evaluates to true.

    :ivar value: Value to use when the lookup conditions are true.
    """

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ErrorDetectCorrectType:
    """
    Describe error detection/correction algorithm.
    """

    checksum: Optional[ChecksumType] = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    crc: Optional[Crctype] = field(
        default=None,
        metadata={
            "name": "CRC",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parity: Optional[ParityType] = field(
        default=None,
        metadata={
            "name": "Parity",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class InputOutputTriggerAlgorithmType(InputOutputAlgorithmType):
    """Input output algorithm is extended with a set of labeled triggers.

    See InputOutputAlgorithmType.

    :ivar trigger_set:
    :ivar trigger_container: First telemetry container from which the
        output parameter should be calculated.
    :ivar priority: Algorithm processing priority. If more than one
        algorithm is triggered by the same container, the lowest
        priority algorithm should be calculated first.
    """

    trigger_set: Optional[TriggerSetType] = field(
        default=None,
        metadata={
            "name": "TriggerSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    trigger_container: Optional[str] = field(
        default=None,
        metadata={
            "name": "triggerContainer",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MessageType(NameDescriptionType):
    """
    :ivar match_criteria:
    :ivar container_ref: The ContainerRef should point to ROOT container
        that will describe an entire packet/minor frame or chunk of
        telemetry.
    """

    match_criteria: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "MatchCriteria",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    container_ref: Optional[ContainerRefType] = field(
        default=None,
        metadata={
            "name": "ContainerRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ParameterPropertiesType:
    """
    Describes extended properties/attributes of Parameter definitions.

    :ivar system_name: Optional.  Normally used when the database is
        built in a flat, non-hierarchical format.
    :ivar validity_condition: Optional condition that must be true for
        this Parameter to be valid.
    :ivar physical_address_set: When present, this set of elements
        describes physical address location(s) of the parameter where it
        is stored.  Typically this is on the data source, although that
        is not constrained by this schema.
    :ivar time_association: This time will override any Default value
        for TimeAssociation.
    :ivar data_source: This attribute describes the nature of the source
        entity for which this parameter receives a value.
        Implementations assign different attributes/properties
        internally to a parameter based on the anticipated data source.
    :ivar read_only: A Parameter marked as 'readOnly' true is non-
        settable by users and applications/services that do not
        represent the data source itself.  Note that a slight conceptual
        overlap exists here between the 'dataSource' attribute and this
        attribute when the data source is 'constant'.  For a constant
        data source, then 'readOnly' should be 'true'.  Application
        implementations may choose to implicitly enforce this.  Some
        implementations have both concepts of a Parameter that is
        settable or non-settable and a Constant in different parts of
        their internal data model.
    :ivar persistence: A Parameter marked to persist should retain the
        latest value through resets/restarts to the extent that is
        possible or defined in the implementation.  The net effect is
        that the initial/default value on a Parameter is only seen once
        or when the system has a reset to revert to initial/default
        values.
    """

    system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemName",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    validity_condition: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    physical_address_set: Optional[PhysicalAddressSetType] = field(
        default=None,
        metadata={
            "name": "PhysicalAddressSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    time_association: Optional[TimeAssociationType] = field(
        default=None,
        metadata={
            "name": "TimeAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    data_source: Optional[TelemetryDataSourceType] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Attribute",
        },
    )
    read_only: bool = field(
        default=False,
        metadata={
            "name": "readOnly",
            "type": "Attribute",
        },
    )
    persistence: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RestrictionCriteriaType(MatchCriteriaType):
    """Define one or more conditions (constraints) for container inheritance.

    A container is instantiable if its constraints are true.  Constraint
    conditions may be a comparison, a list of comparisons, a boolean
    expression, or a graph of containers that are instantiable (if all
    containers are instantiable the condition is true).  See
    BaseContainerType, ComparisonType, ComparisonListType,
    BooleanExpressionType and NextContainerType.

    :ivar next_container: Reference to the named container that must
        follow this container in the stream sequence.
    """

    next_container: Optional[ContainerRefType] = field(
        default=None,
        metadata={
            "name": "NextContainer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class SyncStrategyType:
    """A Sync Strategy specifies the strategy on how to find frames within a
    stream of PCM data.

    The sync strategy is based upon a state machine that begins in the
    'Search' state until the first sync marker is found.  Then it goes
    into the 'Verify' state until a specified number of successive good
    sync markers are found.  Then, the state machine goes into the
    'Lock' state, in the 'Lock' state frames are considered good.
    Should a sync marker be missed in the 'Lock' state, the state
    machine will transition into the 'Check' state, if the next sync
    marker is where it's expected within a specified number of frames,
    then the state machine will transition back to the 'Lock' state, it
    not it will transition back to 'Search'.

    :ivar auto_invert:
    :ivar verify_to_lock_good_frames:
    :ivar check_to_lock_good_frames:
    :ivar max_bit_errors_in_sync_pattern: Maximum number of bit errors
        in the sync pattern (marker).
    """

    auto_invert: Optional[AutoInvertType] = field(
        default=None,
        metadata={
            "name": "AutoInvert",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    verify_to_lock_good_frames: int = field(
        default=4,
        metadata={
            "name": "verifyToLockGoodFrames",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    check_to_lock_good_frames: int = field(
        default=1,
        metadata={
            "name": "checkToLockGoodFrames",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    max_bit_errors_in_sync_pattern: int = field(
        default=0,
        metadata={
            "name": "maxBitErrorsInSyncPattern",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )


@dataclass
class TransmissionConstraintType(MatchCriteriaType):
    """
    A CommandTransmission constraint is used to check that the command can be
    run in the current operating mode and may block the transmission of the
    command if the constraint condition is true.

    :ivar time_out: Pause during timeOut, fail when the timeout passes
    :ivar suspendable: Indicates whether the constraints for a Command
        may be suspended.
    """

    time_out: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "timeOut",
            "type": "Attribute",
        },
    )
    suspendable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AcceptedVerifierType(CommandVerifierType):
    """
    A verifier that means the SpaceSystem has accepted the command.
    """


@dataclass
class AlarmType(BaseAlarmType):
    """Defines a base schema type used to build up the other data type specific
    alarm types.

    The definition includes a count to go into alarm (minViolations –
    the counts to go out of alarm is the same), a condition style alarm
    and a custom alarm. See AlarmConditionType, CustomAlgorithmType,
    BinaryAlarmConditionType, BooleanAlarmType, BinaryContextAlarmType,
    EnumerationAlarmType, NumericAlarmType, StringAlarmType,
    TimeAlarmType, TimeAlarmConditionType.

    :ivar alarm_conditions: A MatchCriteria may be specified for each of
        the 5 alarm levels. Each level is optional and the alarm should
        be the highest level to test true.
    :ivar custom_alarm: An escape for ridiculously complex alarm
        conditions. Will trigger on changes to the containing Parameter.
    :ivar min_violations: The number of successive instances that meet
        the alarm conditions for the alarm to trigger. The default is 1.
    :ivar min_conformance: Optionally specify the number of successive
        instances that do not meet the alarm conditions to leave the
        alarm state. If this attribute is not specified, it is treated
        as being equal to minViolations (symmetric).
    """

    alarm_conditions: Optional[AlarmConditionsType] = field(
        default=None,
        metadata={
            "name": "AlarmConditions",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    custom_alarm: Optional[CustomAlarmType] = field(
        default=None,
        metadata={
            "name": "CustomAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    min_violations: int = field(
        default=1,
        metadata={
            "name": "minViolations",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    min_conformance: Optional[int] = field(
        default=None,
        metadata={
            "name": "minConformance",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )


@dataclass
class AlgorithmSetType:
    """
    An unordered collection of algorithms.
    """

    custom_algorithm: List[InputOutputTriggerAlgorithmType] = field(
        default_factory=list,
        metadata={
            "name": "CustomAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    math_algorithm: List[MathAlgorithmType] = field(
        default_factory=list,
        metadata={
            "name": "MathAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentDiscreteLookupListType:
    """
    Identical to DiscreteLookupListType but supports argument instance
    references.

    :ivar discrete_lookup: Describe a lookup condition set using
        discrete values from arguments and/or parameters.
    """

    discrete_lookup: List[ArgumentDiscreteLookupType] = field(
        default_factory=list,
        metadata={
            "name": "DiscreteLookup",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class BaseContainerType:
    """Describe a child/parent container inheritance relationship.

    Describe constraints with RestrictionCriteria, conditions that must
    be true for this container to be an extension of the parent
    container.  A constraint can be used to convey the identifying
    features of the telemetry format such as the CCSDS application id or
    minor-frame id.  See RestrictionCriteriaType and
    SequenceContainerType.

    :ivar restriction_criteria: Contains the conditions that must
        evaluate to true in order for this container to be an extension
        of the parent container.
    :ivar container_ref: Reference to the container that this container
        extends.
    """

    restriction_criteria: Optional[RestrictionCriteriaType] = field(
        default=None,
        metadata={
            "name": "RestrictionCriteria",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class CompleteVerifierType(CommandVerifierType):
    """
    A possible set of verifiers that all must be true for the command be
    considered completed.
    """

    return_parm_ref: Optional[ParameterRefType] = field(
        default=None,
        metadata={
            "name": "ReturnParmRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ContextCalibratorType:
    """Context calibrations are applied when the ContextMatch is true.

    Context calibrators overide Default calibrators
    """

    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    calibrator: Optional[CalibratorType] = field(
        default=None,
        metadata={
            "name": "Calibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ContextSignificanceType:
    """Describe a significance level for a MetaCommand definition where the
    significance level depends on matching a context value.

    See ContextMatchType and SignificanceType.

    :ivar context_match: Describe the context matching value and source
        that will enable the Significance listed in the Significance
        element.
    :ivar significance: Describe the signficance of this MetaCommand
        definition.  See SignificanceType.
    """

    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    significance: Optional[SignificanceType] = field(
        default=None,
        metadata={
            "name": "Significance",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class DataEncodingType:
    """Describes how a particular piece of data is sent or received from some
    non-native, off-platform device.

    (e.g. a spacecraft)
    """

    error_detect_correct: Optional[ErrorDetectCorrectType] = field(
        default=None,
        metadata={
            "name": "ErrorDetectCorrect",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    bit_order: BitOrderType = field(
        default=BitOrderType.MOST_SIGNIFICANT_BIT_FIRST,
        metadata={
            "name": "bitOrder",
            "type": "Attribute",
        },
    )
    byte_order: Union[ByteOrderCommonType, str] = field(
        default=ByteOrderCommonType.MOST_SIGNIFICANT_BYTE_FIRST,
        metadata={
            "name": "byteOrder",
            "type": "Attribute",
            "pattern": r"(0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15)(,(0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15))*",
        },
    )


@dataclass
class DiscreteLookupListType:
    """Describe an ordered table of integer values and associated conditions,
    forming a lookup table.

    The list may have duplicates.  The table is evaluated from first to
    last, the first condition to be true returns the value associated
    with it.  See DiscreteLookupType.

    :ivar discrete_lookup: Describe a lookup condition set using
        discrete values from parameters.
    """

    discrete_lookup: List[DiscreteLookupType] = field(
        default_factory=list,
        metadata={
            "name": "DiscreteLookup",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ExecutionVerifierType(CommandVerifierType):
    """A verifier that indicates that the command is being executed.

    An optional Element indicates how far along the command has
    progressed either as a fixed value or an (possibly scaled)
    ParameterInstance value.
    """

    percent_complete: Optional[PercentCompleteType] = field(
        default=None,
        metadata={
            "name": "PercentComplete",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class FailedVerifierType(CommandVerifierType):
    """When true, indicates that the command failed.

    timeToWait is how long to wait for the FailedVerifier to test true.
    """

    return_parm_ref: Optional[ParameterRefType] = field(
        default=None,
        metadata={
            "name": "ReturnParmRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class FixedFrameSyncStrategyType(SyncStrategyType):
    """Describe a sync pattern and an optional reference to an algorithm used
    to invert the stream if the frame sync pattern is not found.

    See FixedFrameStreamType.

    :ivar sync_pattern: The pattern of bits used to look for frame
        synchronization.  See SyncPatternType.
    """

    sync_pattern: Optional[SyncPatternType] = field(
        default=None,
        metadata={
            "name": "SyncPattern",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class MessageSetType(OptionalNameDescriptionType):
    message: List[MessageType] = field(
        default_factory=list,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ParameterType(NameDescriptionType):
    """Describe the properties of a telemetry parameter, including its data
    type (parameter type).

    The bulk of properties associated with a telemetry parameter are in
    its parameter type. The initial value specified here, overrides the
    initial value in the parameter type. A parameter may be local, in
    which case its parameter type would have no data encodings. Ideally
    such a definition would also set data source in parameter properties
    to ‘local’ but the syntax does not enforce this. See BaseDataType,
    BaseTimeDataType, and NameReferenceType.

    :ivar parameter_properties: Specify additional properties for this
        Parameter used by the implementation of tailor the behavior and
        attributes of the Parameter.  When not specified, the defaults
        on the ParameterProperties element attributes are assumed.
    :ivar parameter_type_ref: Specify the reference to the parameter
        type from the ParameterTypeSet area using the path reference
        rules, either local to this SpaceSystem, relative, or absolute.
    :ivar initial_value: Specify as: integer data type using xs:integer,
        float data type using xs:double, string data type using
        xs:string, boolean data type using xs:boolean, binary data type
        using xs:hexBinary, enum data type using label name, relative
        time data type using xs:duration, absolute time data type using
        xs:dateTime.  Values must not exceed the characteristics for the
        data type or this is a validation error. Takes precedence over
        an initial value given in the data type. Values are calibrated
        unless there is an option to override it.
    """

    parameter_properties: Optional[ParameterPropertiesType] = field(
        default=None,
        metadata={
            "name": "ParameterProperties",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterTypeRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class QueuedVerifierType(CommandVerifierType):
    """
    A verifer that means the command is scheduled for execution by the
    SpaceSystem.
    """


@dataclass
class ReceivedVerifierType(CommandVerifierType):
    """
    A verifier that simply means the SpaceSystem has received the command.
    """


@dataclass
class SentFromRangeVerifierType(CommandVerifierType):
    """Sent from range means the command has been transmitted to the spacecraft
    by the network that connects the ground system to the spacecraft.

    Obviously, this verifier must come from something other than the
    spacecraft.
    """


@dataclass
class TransferredToRangeVerifierType(CommandVerifierType):
    """Transferred to range means the command has been received to the network
    that connects the ground system to the spacecraft.

    Obviously, this verifier must come from something other than the
    spacecraft.
    """


@dataclass
class TransmissionConstraintListType:
    """Appended to the TramsmissionConstraint List of the base command.

    Constraints are checked in order.
    """

    transmission_constraint: List[TransmissionConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "TransmissionConstraint",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class VariableFrameSyncStrategyType(SyncStrategyType):
    flag: Optional[FlagType] = field(
        default=None,
        metadata={
            "name": "Flag",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ArgumentIntegerValueType:
    """
    Identical to IntegerValueType but supports argument instance references.

    :ivar fixed_value: Use a fixed integer value.
    :ivar dynamic_value: Determine the value by interrogating an
        instance of an argument or parameter.
    :ivar discrete_lookup_list: Determine the value by interrogating an
        instance of an argument or parameter and selecting a specified
        value based on tests of the value of that argument or parameter.
    """

    fixed_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "FixedValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    dynamic_value: Optional[ArgumentDynamicValueType] = field(
        default=None,
        metadata={
            "name": "DynamicValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    discrete_lookup_list: Optional[ArgumentDiscreteLookupListType] = field(
        default=None,
        metadata={
            "name": "DiscreteLookupList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentVariableStringType:
    """
    Identical to VariableStringType but supports argument instance references.

    :ivar dynamic_value: Determine the container size in bits by
        interrogating an instance of a parameter or argument.
    :ivar discrete_lookup_list: Determine the container size in bits by
        interrogating an instance of a parameter or argument and
        selecting a specified value based on tests of the value of that
        parameter or argument.
    :ivar leading_size: In some string implementations, the size of the
        string contents (not the memory allocation size) is determined
        by a leading numeric value.  This is sometimes referred to as
        Pascal strings.  If a LeadingSize is specified, then the
        TerminationChar element does not have a functional meaning.
    :ivar termination_char: The termination character that represents
        the end of the string contents.  For C and most strings, this is
        null (00), which is the default.
    :ivar max_size_in_bits: The upper bound of the size of this string
        data type so that the implementation can reserve/allocate enough
        memory to capture all reported instances of the string.
    """

    dynamic_value: Optional[ArgumentDynamicValueType] = field(
        default=None,
        metadata={
            "name": "DynamicValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    discrete_lookup_list: Optional[ArgumentDiscreteLookupListType] = field(
        default=None,
        metadata={
            "name": "DiscreteLookupList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    leading_size: Optional[LeadingSizeType] = field(
        default=None,
        metadata={
            "name": "LeadingSize",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    termination_char: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TerminationChar",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "format": "base16",
        },
    )
    max_size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxSizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class BinaryAlarmType(AlarmType):
    """
    Describe alarm conditions specific to the binary data type, extends the
    basic AlarmType.
    """


@dataclass
class BinaryContextAlarmType(AlarmType):
    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class BooleanAlarmType(AlarmType):
    """
    Alarm conditions for Boolean types.
    """


@dataclass
class ContextCalibratorListType:
    """Describe an ordered list of calibrators with a context match.

    Useful when different calibrations must be used depending on a
    matching value.  The first context that matches determines which
    calibrator to use. See IntegerDataEncodingType and
    FloatDataEncodingType.

    :ivar context_calibrator: Describe a calibrator that depends on a
        matching value using a ContextMatch.  When the context matches
        for the calibrator, the default calibrator is overridden, if it
        exists.
    """

    context_calibrator: List[ContextCalibratorType] = field(
        default_factory=list,
        metadata={
            "name": "ContextCalibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ContextSignificanceListType:
    """Describe an ordered list of ContextSignificance elements where the
    significance on the first context match to test true is used as the
    significance of the MetaCommand.

    If there is a DefaultSignificance, it is overrideen by the matching
    context.  See ContextSignificantType and MetaCommandType.

    :ivar context_significance: Describe a significance level for a
        MetaCommand definition where the significance level depends on
        matching a context value.  See ContextMatchType and
        SignificanceType.
    """

    context_significance: List[ContextSignificanceType] = field(
        default_factory=list,
        metadata={
            "name": "ContextSignificance",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class EnumerationAlarmType(AlarmType):
    """Describe alarm conditions specific to the enumeration data type, extends
    the basic AlarmType with an EnumerationAlarmList.

    The alarms are described using the label (engineering/calibrated
    value) of the enumerated parameter. Enumeration labels may represent
    several raw/uncalibrated values, so as a result, a single alarm
    definition here may represent multiple raw values in the enumerated
    parameter. It is not necessary to define an alarm for
    raw/uncalibrated values that do not map to an enumeration.
    Implementations should implicitly define this as an alarm case, of
    which the manifestation of that is program/implementation specific.
    See EnumeratedParameterType.

    :ivar enumeration_alarm_list: List of alarm state definitions for
        this enumerated type.
    :ivar default_alarm_level: Alarm state name for when no enumeration
        alarms evaluate to true. This defaults to "normal", which is
        almost always the case. Setting it to another alarm state
        permits a form of "inverted logic" where the alarm list can
        specify the normal states instead of the alarm states.
    """

    enumeration_alarm_list: Optional[EnumerationAlarmListType] = field(
        default=None,
        metadata={
            "name": "EnumerationAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    default_alarm_level: ConcernLevelsType = field(
        default=ConcernLevelsType.NORMAL,
        metadata={
            "name": "defaultAlarmLevel",
            "type": "Attribute",
        },
    )


@dataclass
class FixedFrameStreamType(FrameStreamType):
    """For streams that contain a series of frames with a fixed frame length
    where the frames are found by looking for a marker in the data.

    This marker is sometimes called the frame sync pattern and sometimes
    the Asynchronous Sync Marker (ASM).  This marker need not be
    contiguous although it usually is.

    :ivar sync_strategy:
    :ivar sync_aperture_in_bits: Allowed slip (in bits) in either
        direction for the sync pattern
    :ivar frame_length_in_bits:
    """

    sync_strategy: Optional[FixedFrameSyncStrategyType] = field(
        default=None,
        metadata={
            "name": "SyncStrategy",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    sync_aperture_in_bits: int = field(
        default=0,
        metadata={
            "name": "syncApertureInBits",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    frame_length_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "frameLengthInBits",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class IntegerValueType:
    """
    Contains an Integer value; value may be provided directly or via the value
    in a parameter.

    :ivar fixed_value: Use a fixed integer value.
    :ivar dynamic_value: Determine the value by interrogating an
        instance of a parameter.
    :ivar discrete_lookup_list: Determine the value by interrogating an
        instance of a parameter and selecting a specified value based on
        tests of the value of that parameter.
    """

    fixed_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "FixedValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    dynamic_value: Optional[DynamicValueType] = field(
        default=None,
        metadata={
            "name": "DynamicValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    discrete_lookup_list: Optional[DiscreteLookupListType] = field(
        default=None,
        metadata={
            "name": "DiscreteLookupList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class NumericAlarmType(AlarmType):
    """Describe alarm conditions specific to the numeric data types, extends
    the basic AlarmType with StaticAlarmRanges and ChangeAlarmRanges.

    See FloatParameterType and IntegerParameterType.

    :ivar static_alarm_ranges: StaticAlarmRanges are used to trigger
        alarms when the parameter value passes some threshold value.
    :ivar change_alarm_ranges: ChangeAlarmRanges are used to trigger
        alarms when the parameter value changes by a rate or quantity
        from a reference.
    :ivar alarm_multi_ranges: Similar to but more lenient form of
        StaticAlarmRanges.
    """

    static_alarm_ranges: Optional[AlarmRangesType] = field(
        default=None,
        metadata={
            "name": "StaticAlarmRanges",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    change_alarm_ranges: Optional[ChangeAlarmRangesType] = field(
        default=None,
        metadata={
            "name": "ChangeAlarmRanges",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    alarm_multi_ranges: Optional[AlarmMultiRangesType] = field(
        default=None,
        metadata={
            "name": "AlarmMultiRanges",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ParameterSetType:
    """Describe an unordered collection of parameters where duplicates defined
    by the Parameter name attribute are invalid.

    The ParameterSet exists in both the TelemetryMetaData and the
    CommandMetaData element so that each may be built independently but
    from a single namespace.  See TelemetryMetaDataType and
    CommandMetaDataType.

    :ivar parameter: Defines a named and typed Parameter.
    :ivar parameter_ref: Used to include a Parameter defined in another
        sub-system in this sub-system.
    """

    parameter: List[ParameterType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_ref: List[ParameterRefType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class StringAlarmType(AlarmType):
    """Describe alarms specific to the string data type, extends the basic
    AlarmType, while adding a StringAlarmList and defaultAlarmLevel attribute.

    The string alarm list is evaluated in list order. See
    ConcernsLevelsType and StringAlarmListType.
    """

    string_alarm_list: Optional[StringAlarmListType] = field(
        default=None,
        metadata={
            "name": "StringAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    default_alarm_level: ConcernLevelsType = field(
        default=ConcernLevelsType.NORMAL,
        metadata={
            "name": "defaultAlarmLevel",
            "type": "Attribute",
        },
    )


@dataclass
class TimeAlarmType(AlarmType):
    """
    Alarms associated with time data types.

    :ivar static_alarm_ranges: StaticAlarmRanges are used to trigger
        alarms when the parameter value passes some threshold value
    :ivar change_per_second_alarm_ranges: ChangePerSecondAlarmRanges are
        used to trigger alarms when the parameter value's rate-of-change
        passes some threshold value.  An alarm condition that triggers
        when the value changes too fast (or too slow)
    """

    static_alarm_ranges: Optional[TimeAlarmRangesType] = field(
        default=None,
        metadata={
            "name": "StaticAlarmRanges",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    change_per_second_alarm_ranges: Optional[TimeAlarmRangesType] = field(
        default=None,
        metadata={
            "name": "ChangePerSecondAlarmRanges",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class VariableFrameStreamType(FrameStreamType):
    """For streams that contain a series of frames with a variable frame length
    where the frames are found by looking for a series of one's or zero's
    (usually one's).

    The series is called the flag.   in the PCM stream that are usually
    made to be illegal in the PCM stream by zero or one bit insertion.
    """

    sync_strategy: Optional[VariableFrameSyncStrategyType] = field(
        default=None,
        metadata={
            "name": "SyncStrategy",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class VariableStringType:
    """
    Describe a variable string whose length may change between samples.

    :ivar dynamic_value: Determine the container size in bits by
        interrogating an instance of a parameter.
    :ivar discrete_lookup_list: Determine the container size in bits by
        interrogating an instance of a parameter and selecting a
        specified value based on tests of the value of that parameter.
    :ivar leading_size: In some string implementations, the size of the
        string contents (not the memory allocation size) is determined
        by a leading numeric value.  This is sometimes referred to as
        Pascal strings.  If a LeadingSize is specified, then the
        TerminationChar element does not have a functional meaning.
    :ivar termination_char: The termination character that represents
        the end of the string contents.  For C and most strings, this is
        null (00), which is the default.
    :ivar max_size_in_bits: The upper bound of the size of this string
        data type so that the implementation can reserve/allocate enough
        memory to capture all reported instances of the string.
    """

    dynamic_value: Optional[DynamicValueType] = field(
        default=None,
        metadata={
            "name": "DynamicValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    discrete_lookup_list: Optional[DiscreteLookupListType] = field(
        default=None,
        metadata={
            "name": "DiscreteLookupList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    leading_size: Optional[LeadingSizeType] = field(
        default=None,
        metadata={
            "name": "LeadingSize",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    termination_char: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TerminationChar",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "format": "base16",
        },
    )
    max_size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxSizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class VerifierSetType:
    """Describe a collection of unordered verifiers.

    A command verifier is a conditional check on the telemetry from a
    SpaceSystem that that provides positive indication on the processing
    state of a command.  There are eight different verifiers each
    associated with difference states in command processing:
    TransferredToRange, TransferredFromRange, Received, Accepted,
    Queued, Execution, Complete, and Failed.  There may be multiple
    ‘complete’ and 'execution' verifiers. If the MetaCommand is part of
    an inheritance relation (BaseMetaCommand), the 'complete' and
    'execution' verifier sets are appended to any defined in the parent
    MetaCommand. All others will override a verifier defined in a
    BaseMetaCommand.  Duplicate verifiers in the list of
    CompleteVerifiers and ExecutionVerifiers before and after appending
    to the verifiers in BaseMetaCommand should be avoided. See
    MetaCommandType and BaseMetaCommandType for additional information.
    """

    transferred_to_range_verifier: Optional[TransferredToRangeVerifierType] = field(
        default=None,
        metadata={
            "name": "TransferredToRangeVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    sent_from_range_verifier: Optional[SentFromRangeVerifierType] = field(
        default=None,
        metadata={
            "name": "SentFromRangeVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    received_verifier: Optional[ReceivedVerifierType] = field(
        default=None,
        metadata={
            "name": "ReceivedVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    accepted_verifier: Optional[AcceptedVerifierType] = field(
        default=None,
        metadata={
            "name": "AcceptedVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    queued_verifier: Optional[QueuedVerifierType] = field(
        default=None,
        metadata={
            "name": "QueuedVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    execution_verifier: List[ExecutionVerifierType] = field(
        default_factory=list,
        metadata={
            "name": "ExecutionVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    complete_verifier: List[CompleteVerifierType] = field(
        default_factory=list,
        metadata={
            "name": "CompleteVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    failed_verifier: Optional[FailedVerifierType] = field(
        default=None,
        metadata={
            "name": "FailedVerifier",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentBinaryDataEncodingType(DataEncodingType):
    """
    Identical to BinaryDataEncodingType but supports argument instance
    references.

    :ivar size_in_bits: Number of bits this value occupies on the stream
        being encoded/decoded.
    :ivar from_binary_transform_algorithm: Used to convert binary data
        to an application data type
    :ivar to_binary_transform_algorithm: Used to convert binary data
        from an application data type to binary data
    """

    size_in_bits: Optional[ArgumentIntegerValueType] = field(
        default=None,
        metadata={
            "name": "SizeInBits",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    from_binary_transform_algorithm: Optional[ArgumentInputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "FromBinaryTransformAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    to_binary_transform_algorithm: Optional[ArgumentInputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "ToBinaryTransformAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentDimensionType:
    """
    Identical to DimensionType but supports argument instance references.

    :ivar starting_index: zero based index
    :ivar ending_index:
    """

    starting_index: Optional[ArgumentIntegerValueType] = field(
        default=None,
        metadata={
            "name": "StartingIndex",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    ending_index: Optional[ArgumentIntegerValueType] = field(
        default=None,
        metadata={
            "name": "EndingIndex",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ArgumentLocationInContainerInBitsType(ArgumentIntegerValueType):
    """
    Identical to LocationInContainerInBitsType but supports argument instance
    references.
    """

    reference_location: ReferenceLocationType = field(
        default=ReferenceLocationType.PREVIOUS_ENTRY,
        metadata={
            "name": "referenceLocation",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentRepeatType:
    """
    Identical to RepeatType but supports argument instance references.

    :ivar count: Value (either fixed or dynamic) that contains the count
        of repeated structures.
    :ivar offset:
    """

    count: Optional[ArgumentIntegerValueType] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    offset: Optional[ArgumentIntegerValueType] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class ArgumentStringDataEncodingType(DataEncodingType):
    """
    Identical to StringDataEncodingType but supports argument instance
    references.

    :ivar size_in_bits: Static length strings do not change in overall
        length between samples.   They may terminate before the end of
        their buffer using a terminating character, or by various
        lookups, or calculations.  But they have a maximum fixed size,
        and the data itself is always within that maximum size.
    :ivar variable: Variable length strings are those where the space
        occupied in a container can vary.  If the string has variable
        content but occupies the same amount of space when encoded
        should use the SizeInBits element.  Specification of a variable
        length string needs to consider that the implementation needs to
        allocate space to store the string.  Specify the maximum
        possible length of the string data type for memory purposes and
        also specify the bit size of the string to use in containers
        with the dynamic elements.
    :ivar encoding: The character set encoding of this string data type.
    """

    size_in_bits: Optional[SizeInBitsType] = field(
        default=None,
        metadata={
            "name": "SizeInBits",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    variable: Optional[ArgumentVariableStringType] = field(
        default=None,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    encoding: StringEncodingType = field(
        default=StringEncodingType.UTF_8,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BinaryContextAlarmListType:
    """Describe an ordered collection of context binary alarms, duplicates are
    valid.

    Process the contexts in list order.  See BinaryContextAlarmType.
    """

    context_alarm: List[BinaryContextAlarmType] = field(
        default_factory=list,
        metadata={
            "name": "ContextAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class BinaryDataEncodingType(DataEncodingType):
    """Describe binary data that is unmolested in the decoding/encoding or
    cannot be represented in any of the other data encoding formats.

    Optionally use the FromBinaryTransformAlgorithm and
    ToBinaryTransformAlgorithm element to describe the transformation
    process.  See InputAlgorithmType for the transformation structure.

    :ivar size_in_bits: Number of bits this value occupies on the stream
        being encoded/decoded.
    :ivar from_binary_transform_algorithm: Used to convert binary data
        to an application data type
    :ivar to_binary_transform_algorithm: Used to convert binary data
        from an application data type to binary data
    """

    size_in_bits: Optional[IntegerValueType] = field(
        default=None,
        metadata={
            "name": "SizeInBits",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    from_binary_transform_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "FromBinaryTransformAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    to_binary_transform_algorithm: Optional[InputAlgorithmType] = field(
        default=None,
        metadata={
            "name": "ToBinaryTransformAlgorithm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class BooleanContextAlarmType(BooleanAlarmType):
    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class DimensionType:
    """For partial entries of an array, the starting and ending index for each
    dimension, OR the Size must be specified.

    Indexes are zero based.

    :ivar starting_index: zero based index
    :ivar ending_index:
    """

    starting_index: Optional[IntegerValueType] = field(
        default=None,
        metadata={
            "name": "StartingIndex",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    ending_index: Optional[IntegerValueType] = field(
        default=None,
        metadata={
            "name": "EndingIndex",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class EnumerationContextAlarmType(EnumerationAlarmType):
    """Describe a context that when true the alarm condition may be evaluated.

    See ContextMatchType and EnumerationAlarmType.

    :ivar context_match: Describe a context in terms of a parameter and
        value that when true enables the context alarm definition.
    """

    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class FloatDataEncodingType(DataEncodingType):
    """
    For common encodings of floating point data.

    :ivar default_calibrator: Calibrator to be applied to the raw
        uncalibrated value to arrive at the engineering/calibrated value
        when no Context Calibrators are provided or evaluate to true,
        based on their MatchCriteria.
    :ivar context_calibrator_list: Calibrator to be applied to the raw
        uncalibrated value to arrive at the engineering/calibrated value
        when a MatchCriteria evaluates to true.
    :ivar encoding: Specifies real/decimal numeric value to raw encoding
        method, with the default being "IEEE754_1985".
    :ivar size_in_bits: Number of bits to use for the float raw encoding
        method, with 32 being the default.  Not every number of bits is
        valid for each encoding method.
    :ivar change_threshold: A changeThreshold may optionally be
        specified to inform systems of the minimum change in value that
        is significant.  This is used by some systems to limit the
        telemetry processing and/or recording requirements. If the value
        is unspecified or zero, any change is significant.
    """

    default_calibrator: Optional[CalibratorType] = field(
        default=None,
        metadata={
            "name": "DefaultCalibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_calibrator_list: Optional[ContextCalibratorListType] = field(
        default=None,
        metadata={
            "name": "ContextCalibratorList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    encoding: FloatEncodingType = field(
        default=FloatEncodingType.IEEE754_1985,
        metadata={
            "type": "Attribute",
        },
    )
    size_in_bits: FloatEncodingSizeInBitsType = field(
        default=FloatEncodingSizeInBitsType.VALUE_32,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
        },
    )
    change_threshold: Optional[float] = field(
        default=None,
        metadata={
            "name": "changeThreshold",
            "type": "Attribute",
        },
    )


@dataclass
class IntegerDataEncodingType(DataEncodingType):
    """
    For all major encodings of integer data.

    :ivar default_calibrator: Calibrator to be applied to the raw
        uncalibrated value to arrive at the engineering/calibrated value
        when no Context Calibrators are provided or evaluate to true,
        based on their MatchCriteria.
    :ivar context_calibrator_list: Calibrator to be applied to the raw
        uncalibrated value to arrive at the engineering/calibrated value
        when a MatchCriteria evaluates to true.
    :ivar encoding: Specifies integer numeric value to raw encoding
        method, with the default being "unsigned".
    :ivar size_in_bits: Number of bits to use for the raw encoding, with
        8 being the default.
    :ivar change_threshold: A changeThreshold may optionally be
        specified to inform systems of the minimum change in value that
        is significant.  This is used by some systems to limit the
        telemetry processing and/or recording requirements, such as for
        an analog-to-digital converter that dithers in the least
        significant bit. If the value    is unspecified or zero, any
        change is significant.
    """

    default_calibrator: Optional[CalibratorType] = field(
        default=None,
        metadata={
            "name": "DefaultCalibrator",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_calibrator_list: Optional[ContextCalibratorListType] = field(
        default=None,
        metadata={
            "name": "ContextCalibratorList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    encoding: IntegerEncodingType = field(
        default=IntegerEncodingType.UNSIGNED,
        metadata={
            "type": "Attribute",
        },
    )
    size_in_bits: int = field(
        default=8,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    change_threshold: Optional[int] = field(
        default=None,
        metadata={
            "name": "changeThreshold",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )


@dataclass
class LocationInContainerInBitsType(IntegerValueType):
    """Describe the absolute or relative bit location of an entry in a
    container.

    The "referenceLocation" attribute specifies the starting bit anchor.
    If no referenceLocation value is given, the entry is assumed to
    begin at the first bit position after the previous entry.  Each
    container starts at bit 0, thus "containerStart" is an offset from
    0.  Negative container start bits are before the container and are
    implementation dependent – these should be flagged as likely errors.
    "containerEnd" is given as a positive offset from the end of the
    container, thus a container end of 0 is exactly at the end of the
    container.  Negative container end addresses are after the container
    and are implementation dependent – these should be flagged as likely
    errors.  Positive "previouEntry" values are offsets from the
    previous entry – zero (0) is the default which means it follows
    contiguously from the last occupied bit of the previous entry.  A
    value of one means it is offset 1-bit from the previous entry, and a
    value of negative 1 (-1) means it overlaps the previous entry by one
    bit, and so forth. The "nextEntry" attribute value is proposed for
    deprecation and should be avoided.  See SequenceEntryType.

    :ivar reference_location: Defines the relative reference used to
        interpret the start bit position.  The default is 0 bits from
        the end of the previousEntry, which makes the entry contiguous.
    """

    reference_location: ReferenceLocationType = field(
        default=ReferenceLocationType.PREVIOUS_ENTRY,
        metadata={
            "name": "referenceLocation",
            "type": "Attribute",
        },
    )


@dataclass
class NumericContextAlarmType(NumericAlarmType):
    """Describe a parameter dependent context, that when evaluates to true,
    enables the use of this alarm definition.

    See ContextMatchType and NumericAlarmType.

    :ivar context_match: Contains the evaluation criteria for a
        parameter dependent test, that when evaluates to true, enables
        this alarm definition.
    """

    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class RepeatType:
    """
    Hold a structure that can be repeated X times, where X is the Count.

    :ivar count: Value (either fixed or dynamic) that contains the count
        of repeated structures.
    :ivar offset:
    """

    count: Optional[IntegerValueType] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    offset: Optional[IntegerValueType] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class StreamSetType:
    """
    Contains an unordered set of Streams.
    """

    fixed_frame_stream: List[FixedFrameStreamType] = field(
        default_factory=list,
        metadata={
            "name": "FixedFrameStream",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    variable_frame_stream: List[VariableFrameStreamType] = field(
        default_factory=list,
        metadata={
            "name": "VariableFrameStream",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    custom_stream: List[CustomStreamType] = field(
        default_factory=list,
        metadata={
            "name": "CustomStream",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class StringContextAlarmType(StringAlarmType):
    """Describe a context that when true the alarm may be evaluated.

    See ContextMatchType and StringAlarmType.
    """

    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class StringDataEncodingType(DataEncodingType):
    """Describe common encodings of string data: UTF-8 and UTF-16.

    See StringDataType.

    :ivar size_in_bits: Static length strings do not change in overall
        length between samples.   They may terminate before the end of
        their buffer using a terminating character, or by various
        lookups, or calculations.  But they have a maximum fixed size,
        and the data itself is always within that maximum size.
    :ivar variable: Variable length strings are those where the space
        occupied in a container can vary.  If the string has variable
        content but occupies the same amount of space when encoded
        should use the SizeInBits element.  Specification of a variable
        length string needs to consider that the implementation needs to
        allocate space to store the string.  Specify the maximum
        possible length of the string data type for memory purposes and
        also specify the bit size of the string to use in containers
        with the dynamic elements.
    :ivar encoding: The character set encoding of this string data type.
    """

    size_in_bits: Optional[SizeInBitsType] = field(
        default=None,
        metadata={
            "name": "SizeInBits",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    variable: Optional[VariableStringType] = field(
        default=None,
        metadata={
            "name": "Variable",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    encoding: StringEncodingType = field(
        default=StringEncodingType.UTF_8,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TimeContextAlarmType(TimeAlarmType):
    """Context alarms are applied when the ContextMatch is true.

    Context alarms override Default alarms
    """

    context_match: Optional[ContextMatchType] = field(
        default=None,
        metadata={
            "name": "ContextMatch",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ArgumentBaseDataType(NameDescriptionType):
    """
    Identical to BaseDataType but supports argument instance references.

    :ivar unit_set: When appropriate, describe the units of measure that
        are represented by this argument value.
    :ivar binary_data_encoding: Binary encoding is typically a "pass
        through" raw encoding form where one of the more common
        encodings is not required for the argument.  A custom
        transformation capability is available if needed.
    :ivar float_data_encoding: Float encoding is a common encoding where
        the raw binary is in a form that gets interpreted as a decimal
        numeric value.
    :ivar integer_data_encoding: Integer encoding is a common encoding
        where the raw binary is in a form that gets interpreted as an
        integral value, either signed or unsigned.
    :ivar string_data_encoding: String encoding is a common encoding
        where the raw binary is in a form that gets interpreted as a
        character sequence.
    :ivar base_type: Used to derive one Data Type from another - will
        inherit all the attributes from the baseType any of which may be
        redefined in this type definition.
    """

    unit_set: Optional[UnitSetType] = field(
        default=None,
        metadata={
            "name": "UnitSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    binary_data_encoding: Optional[ArgumentBinaryDataEncodingType] = field(
        default=None,
        metadata={
            "name": "BinaryDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    float_data_encoding: Optional[FloatDataEncodingType] = field(
        default=None,
        metadata={
            "name": "FloatDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    integer_data_encoding: Optional[IntegerDataEncodingType] = field(
        default=None,
        metadata={
            "name": "IntegerDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    string_data_encoding: Optional[ArgumentStringDataEncodingType] = field(
        default=None,
        metadata={
            "name": "StringDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ArgumentDimensionListType:
    """
    Identical to DimensionListType but supports argument instance references.
    """

    dimension: List[ArgumentDimensionType] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ArgumentSequenceEntryType:
    """
    Identical to a SequenceEntryType but supports argument instance references.

    :ivar location_in_container_in_bits: The start bit 0 position for
        each container is local to the container, but does include space
        occupied by inherited containers.  When a container is
        "included", as opposed to inherited, then the interpreting
        implementation takes into account the start bit position of the
        referring container when finally assembling the start bits for
        the post-processed entry content.  The default start bit for any
        entry is 0 bits from the previous entry, making the content
        contiguous when this element is not used.
    :ivar repeat_entry: May be used when this entry repeats itself in
        the sequence container.  When an entry repeats, it effectively
        specifies that the same entry is reported more than once in the
        container and has the same physical meaning.  This should not be
        construed to be equivalent to arrays.
    :ivar include_condition: This entry will only be included in the
        sequence when this condition is true, otherwise it is always
        included.  When the include condition evaluates to false, it is
        as if the entry does not exist such that any start bit
        interpretations cannot take into account the space that would
        have been occupied if this included condition were true.
    :ivar ancillary_data_set: Ancillary data associated with this entry.
    :ivar short_description: Optional short description for this entry
        element.
    """

    location_in_container_in_bits: Optional[ArgumentLocationInContainerInBitsType] = field(
        default=None,
        metadata={
            "name": "LocationInContainerInBits",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    repeat_entry: Optional[ArgumentRepeatType] = field(
        default=None,
        metadata={
            "name": "RepeatEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    include_condition: Optional[ArgumentMatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "IncludeCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    ancillary_data_set: Optional[AncillaryDataSetType] = field(
        default=None,
        metadata={
            "name": "AncillaryDataSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Attribute",
        },
    )


@dataclass
class BaseDataType(NameDescriptionType):
    """An abstract schema type used by within the schema to derive the other
    simple/primitive engineering form data types:  BooleanDataType,
    BinaryDataType, StringDataType, EnumeratedDataType, FloatDataType and
    IntegerDataType.

    The encoding elements are optional because they describe the raw
    wire encoded form of the data type.  Encoding is only necessary when
    the type is telemetered in some form.  Local variables and derived
    typically do not require encoding.

    :ivar unit_set: When appropriate, describe the units of measure that
        are represented by this parameter value.
    :ivar binary_data_encoding: Binary encoding is typically a "pass
        through" raw encoding form where one of the more common
        encodings is not required for the parameter.  A custom
        transformation capability is available if needed.
    :ivar float_data_encoding: Float encoding is a common encoding where
        the raw binary is in a form that gets interpreted as a decimal
        numeric value.
    :ivar integer_data_encoding: Integer encoding is a common encoding
        where the raw binary is in a form that gets interpreted as an
        integral value, either signed or unsigned.
    :ivar string_data_encoding: String encoding is a common encoding
        where the raw binary is in a form that gets interpreted as a
        character sequence.
    :ivar base_type: Used to derive one Data Type from another - will
        inherit all the attributes from the baseType any of which may be
        redefined in this type definition.
    """

    unit_set: Optional[UnitSetType] = field(
        default=None,
        metadata={
            "name": "UnitSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    binary_data_encoding: Optional[BinaryDataEncodingType] = field(
        default=None,
        metadata={
            "name": "BinaryDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    float_data_encoding: Optional[FloatDataEncodingType] = field(
        default=None,
        metadata={
            "name": "FloatDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    integer_data_encoding: Optional[IntegerDataEncodingType] = field(
        default=None,
        metadata={
            "name": "IntegerDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    string_data_encoding: Optional[StringDataEncodingType] = field(
        default=None,
        metadata={
            "name": "StringDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class BooleanContextAlarmListType:
    context_alarm: List[BooleanContextAlarmType] = field(
        default_factory=list,
        metadata={
            "name": "ContextAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ContainerType(NameDescriptionType):
    """
    An abstract block of data; used as the base type for more specific
    container types.

    :ivar default_rate_in_stream:
    :ivar rate_in_stream_set:
    :ivar binary_encoding: May be used to indicate error detection and
        correction, change byte order,  provide the size (when it can't
        be derived), or perform some custom processing.
    """

    default_rate_in_stream: Optional[RateInStreamType] = field(
        default=None,
        metadata={
            "name": "DefaultRateInStream",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    rate_in_stream_set: Optional[RateInStreamSetType] = field(
        default=None,
        metadata={
            "name": "RateInStreamSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    binary_encoding: Optional[BinaryDataEncodingType] = field(
        default=None,
        metadata={
            "name": "BinaryEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class DimensionListType:
    """Where the Dimension list is in this form:
    Array[1stDim][2ndDim][lastDim].

    The last dimension is assumed to be the least significant - that is this dimension will cycle through its combination before the next to last dimension changes.  The order MUST ascend or the array will need to be broken out entry by entry.
    """

    dimension: List[DimensionType] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class EncodingType:
    """Describe the data encoding for a time data type.

    It includes the units and other attributes scale and offset.  Use
    scale and offset to describe a y=mx+b relationship (where m is the
    slope/scale and b is the intercept/offset) to make adjustments to
    the encoded time value so that it matches the time units.  For
    binary encoded time use transform algorithms to convert time data
    formats that are too difficult to describe in XTCE. See
    AbsoluteTimeDataType and RelativeTimeDataType.

    :ivar binary_data_encoding: Binary encoding is typically a "pass
        through" raw encoding form where one of the more common
        encodings is not required for the parameter.  A custom
        transformation capability is available if needed.
    :ivar float_data_encoding: Float encoding is a common encoding where
        the raw binary is in a form that gets interpreted as a decimal
        numeric value.
    :ivar integer_data_encoding: Integer encoding is a common encoding
        where the raw binary is in a form that gets interpreted as an
        integral value, either signed or unsigned.
    :ivar string_data_encoding: String encoding is a common encoding
        where the raw binary is in a form that gets interpreted as a
        character sequence.
    :ivar units: Time units, with the default being in seconds.
    :ivar scale: Linear slope used as a shorter form of specifying a
        calibrator to convert between the raw value and the engineering
        units.
    :ivar offset: Linear intercept used as a shorter form of specifying
        a calibrator to convert between the raw value and the
        engineering units.
    """

    binary_data_encoding: Optional[BinaryDataEncodingType] = field(
        default=None,
        metadata={
            "name": "BinaryDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    float_data_encoding: Optional[FloatDataEncodingType] = field(
        default=None,
        metadata={
            "name": "FloatDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    integer_data_encoding: Optional[IntegerDataEncodingType] = field(
        default=None,
        metadata={
            "name": "IntegerDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    string_data_encoding: Optional[StringDataEncodingType] = field(
        default=None,
        metadata={
            "name": "StringDataEncoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    units: TimeUnitsType = field(
        default=TimeUnitsType.SECONDS,
        metadata={
            "type": "Attribute",
        },
    )
    scale: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
        },
    )
    offset: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EnumerationContextAlarmListType:
    """Describe an ordered collection of context enumeration alarms, duplicates
    are valid.

    Process the contexts in list order. See EnumerationContextAlarmType.

    :ivar context_alarm: Describe the alarm matching context criteria
        and the alarm definition itself.
    """

    context_alarm: List[EnumerationContextAlarmType] = field(
        default_factory=list,
        metadata={
            "name": "ContextAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class NumericContextAlarmListType:
    """An ordered collection of numeric alarms associated with a context.

    A context is an alarm definition on a parameter which is valid only
    in the case of a test on the value of other parameters. Process the
    contexts in list order. Used by both FloatParameterType and
    IntegerParameterType. See NumericContextAlarmType.

    :ivar context_alarm: A contextual alarm definition for the parameter
        that uses this type that is valid when a test against the value
        of one or more other parameters evaluates to true.
    """

    context_alarm: List[NumericContextAlarmType] = field(
        default_factory=list,
        metadata={
            "name": "ContextAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class SequenceEntryType:
    """Defines an abstract schema type used to create other entry types.

    Describe an entry’s location in the container (See
    LocationInContainerInBitsType). The location may be fixed or
    dynamic, absolute or relative. Entries may be included depending on
    the value of a condition (See IncludeConditionType), and entries may
    also repeat (see RepeatEntryType). The entry’s IncludeCondition
    resolves to true, it is fully-resolved when its size is computable
    after RepeatEntry has been accounted for and then offset by
    LocationInContainer. See EntryListType, IncludeConditionType,
    RepeatEntryType and LocationInContainerInBitsType.

    :ivar location_in_container_in_bits: The start bit 0 position for
        each container is local to the container, but does include space
        occupied by inherited containers.  When a container is
        "included", as opposed to inherited, then the interpreting
        implementation takes into account the start bit position of the
        referring container when finally assembling the start bits for
        the post-processed entry content.  The default start bit for any
        entry is 0 bits from the previous entry, making the content
        contiguous when this element is not used.
    :ivar repeat_entry: May be used when this entry repeats itself in
        the sequence container.  When an entry repeats, it effectively
        specifies that the same entry is reported more than once in the
        container and has the same physical meaning.  This should not be
        construed to be equivalent to arrays.
    :ivar include_condition: This entry will only be included in the
        sequence when this condition is true, otherwise it is always
        included.  When the include condition evaluates to false, it is
        as if the entry does not exist such that any start bit
        interpretations cannot take into account the space that would
        have been occupied if this included condition were true.
    :ivar time_association: Optional timing information associated with
        this entry.
    :ivar ancillary_data_set: Optional ancillary data associated with
        this element.
    :ivar short_description: Optional short description for this entry
        element.
    """

    location_in_container_in_bits: Optional[LocationInContainerInBitsType] = field(
        default=None,
        metadata={
            "name": "LocationInContainerInBits",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    repeat_entry: Optional[RepeatType] = field(
        default=None,
        metadata={
            "name": "RepeatEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    include_condition: Optional[MatchCriteriaType] = field(
        default=None,
        metadata={
            "name": "IncludeCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    time_association: Optional[TimeAssociationType] = field(
        default=None,
        metadata={
            "name": "TimeAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    ancillary_data_set: Optional[AncillaryDataSetType] = field(
        default=None,
        metadata={
            "name": "AncillaryDataSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Attribute",
        },
    )


@dataclass
class StringContextAlarmListType:
    """An ordered collection of numeric alarms associated with a context.

    Process the contexts in list order. See StringContextAlarmType.
    """

    context_alarm: List[StringContextAlarmType] = field(
        default_factory=list,
        metadata={
            "name": "ContextAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class TimeContextAlarmListType:
    context_alarm: List[TimeContextAlarmType] = field(
        default_factory=list,
        metadata={
            "name": "ContextAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ArgumentArgumentRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ArgumentRefEntryType but supports argument instance
    references.
    """

    argument_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "argumentRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ArgumentArrayArgumentRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ArrayParameterRefEntryType but supports argument instance
    references.

    :ivar dimension_list: The dimension here if used for subsetting must
        be less than the ones in the type.  It's not a subset if its the
        same size.
    :ivar argument_ref:
    :ivar last_entry_for_this_array_instance:
    """

    dimension_list: Optional[ArgumentDimensionListType] = field(
        default=None,
        metadata={
            "name": "DimensionList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    argument_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "argumentRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    last_entry_for_this_array_instance: bool = field(
        default=False,
        metadata={
            "name": "lastEntryForThisArrayInstance",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentArrayParameterRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ArrayParameterRefEntryType but supports argument instance
    references.

    :ivar dimension_list: The dimension here if used for subsetting must
        be less than the ones in the type.  It's not a subset if its the
        same size.
    :ivar parameter_ref:
    :ivar last_entry_for_this_array_instance:
    """

    dimension_list: Optional[DimensionListType] = field(
        default=None,
        metadata={
            "name": "DimensionList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    last_entry_for_this_array_instance: bool = field(
        default=False,
        metadata={
            "name": "lastEntryForThisArrayInstance",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentBaseTimeDataType(NameDescriptionType):
    """
    Identical to BaseTimeDataType but supports argument instance references.

    :ivar encoding: Describes how the raw base counts of the time type
        are encoded/decoded.
    :ivar reference_time: Describes origin (epoch or reference) of this
        time type.
    :ivar base_type: Extend another absolute or relative time type.
    """

    encoding: Optional[EncodingType] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    reference_time: Optional[ReferenceTimeType] = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ArgumentBinaryDataType(ArgumentBaseDataType):
    """
    Identical to BinaryDataType but supports argument instance references.

    :ivar initial_value: Default/Initial value is always given in
        calibrated form.  Extra bits are truncated from the MSB
        (leftmost).
    """

    initial_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "format": "base16",
        },
    )


@dataclass
class ArgumentBooleanDataType(ArgumentBaseDataType):
    """
    Identical to BooleanDataType but supports argument instance references.

    :ivar initial_value: Default/Initial value is always given in
        calibrated form.
    :ivar one_string_value: Enumeration string representing the 1 value,
        with the default being 'True'.
    :ivar zero_string_value: Enumeration string representing the 0
        value, with the default being 'False'.
    """

    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    one_string_value: str = field(
        default="True",
        metadata={
            "name": "oneStringValue",
            "type": "Attribute",
        },
    )
    zero_string_value: str = field(
        default="False",
        metadata={
            "name": "zeroStringValue",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentContainerRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ContainerRefEntryType but supports argument instance
    references.
    """

    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ArgumentContainerSegmentRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ContainerSegmentRefEntryType but supports argument instance
    references.
    """

    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class ArgumentEnumeratedDataType(ArgumentBaseDataType):
    """
    Identical to EnumeratedDataType but supports argument instance references.

    :ivar enumeration_list: Unordered list of label/value pairs where
        values cannot be duplicated.
    :ivar initial_value: Default/Initial value is always given in
        calibrated form.  Use the label, it must be in the enumeration
        list to be valid.
    """

    enumeration_list: Optional[EnumerationListType] = field(
        default=None,
        metadata={
            "name": "EnumerationList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentFixedValueEntryType(ArgumentSequenceEntryType):
    """
    Identical to FixedValueEntryType but supports argument instance references.

    :ivar name: An optional name for the fixed/constant field in the
        sequence.
    :ivar binary_value: The fixed/constant value that should be encoded
        into the sequence.  This value provided should have sufficient
        bit length to accomodate the size in bits.  If the value is
        larger, the most significant unnecessary bits are dropped.  The
        value provided should be in network byte order for encoding.
    :ivar size_in_bits: The number of bits that this fixed/constant
        value should occupy in the sequence.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    binary_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "binaryValue",
            "type": "Attribute",
            "required": True,
            "format": "base16",
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class ArgumentFloatDataType(ArgumentBaseDataType):
    """
    Identical to FloatDataType but supports argument instance references.

    :ivar to_string: This element provides the implementation with
        assistance rendering the value as a string for users.
    :ivar initial_value: Default/Initial value is always given in
        calibrated form.
    :ivar size_in_bits: Optional hint to the implementation about the
        size of the engineering/calibrated data type to use internally.
        Generally this can be determined by examination of the space
        required to capture the full range of the encoding, but it is
        not always clear when calibrators are in use.  A tolerant
        implementation will endeavor to always make sufficient size
        engineering data types to capture the entire range of possible
        values.
    """

    to_string: Optional[ToStringType] = field(
        default=None,
        metadata={
            "name": "ToString",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    initial_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    size_in_bits: FloatSizeInBitsType = field(
        default=FloatSizeInBitsType.VALUE_32,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentIndirectParameterRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to IndirectParameterRefEntryType but supports argument instance
    references.
    """

    parameter_instance: Optional[ParameterInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ParameterInstance",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    alias_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "aliasNameSpace",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentIntegerDataType(ArgumentBaseDataType):
    """
    Identical to IntegerDataType but supports argument instance references.

    :ivar to_string: This element provides the implementation with
        assistance rendering the value as a string for users.
    :ivar initial_value: Default/Initial value is always given in
        calibrated form.  Default is base 10 form; binary, octal, or
        hexadecimal values may be given by preceding value with 0[b|B],
        0[o|O|, 0[x|X] respectively.
    :ivar size_in_bits: Optional hint to the implementation about the
        size of the engineering/calibrated data type to use internally.
        Generally this can be determined by examination of the space
        required to capture the full range of the encoding, but it is
        not always clear when calibrators are in use.  A tolerant
        implementation will endeavor to always make sufficient size
        engineering data types to capture the entire range of possible
        values.
    :ivar signed: Flag indicating if the engineering/calibrated data
        type used should support signed representation.  This should not
        be confused with the encoding type for the raw value.  The
        default is true.
    """

    to_string: Optional[ToStringType] = field(
        default=None,
        metadata={
            "name": "ToString",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    initial_value: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "pattern": r"0[xX][0-9a-fA-F]+",
        },
    )
    size_in_bits: int = field(
        default=32,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    signed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentParameterRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ParameterRefEntryType but supports argument instance
    references.
    """

    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ArgumentParameterSegmentRefEntryType(ArgumentSequenceEntryType):
    """
    Identical to ParameterSegmentRefEntryType but supports argument instance
    references.
    """

    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class ArgumentStreamSegmentEntryType(ArgumentSequenceEntryType):
    """
    Identical to StreamRefEntryType but supports argument instance references.
    """

    stream_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "streamRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class ArgumentStringDataType(ArgumentBaseDataType):
    """
    Identical to StringDataType but supports argument instance references.

    :ivar size_range_in_characters:
    :ivar initial_value: Initial values for string types, may include C
        language style (\\n, \\t, \\", \\\\, etc.) escape sequences.
    :ivar restriction_pattern: restriction pattern is a regular
        expression
    :ivar character_width:
    """

    size_range_in_characters: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "SizeRangeInCharacters",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    restriction_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "restrictionPattern",
            "type": "Attribute",
        },
    )
    character_width: Optional[CharacterWidthType] = field(
        default=None,
        metadata={
            "name": "characterWidth",
            "type": "Attribute",
        },
    )


@dataclass
class ArrayArgumentType(ArrayDataTypeType):
    """Describe an array argument type.

    The size and number of dimension are described here. See
    ArrayParameterRefEntryType, NameReferenceType and ArrayDataType.

    :ivar dimension_list: Describe the dimensions of this array.
    """

    dimension_list: Optional[ArgumentDimensionListType] = field(
        default=None,
        metadata={
            "name": "DimensionList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class ArrayParameterRefEntryType(SequenceEntryType):
    """Describe an entry that is an array parameter.

    Specify the dimension sizes if you subsetting the array (the number
    of dimensions shall match the number defined in the parameter’s type
    definition), otherwise the ones in the ParameterType are assumed.
    See SequenceEntryType.

    :ivar dimension_list: The dimension here if used for subsetting must
        be less than the ones in the type.  It's not a subset if its the
        same size.
    :ivar parameter_ref:
    """

    dimension_list: Optional[DimensionListType] = field(
        default=None,
        metadata={
            "name": "DimensionList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ArrayParameterType(ArrayDataTypeType):
    """Describe an array parameter type.

    The size and number of dimensions are described here. See
    ArrayParameterRefEntryType, NameReferenceType and ArrayDataType.

    :ivar dimension_list: Describe the dimensions of this array.
    """

    dimension_list: Optional[DimensionListType] = field(
        default=None,
        metadata={
            "name": "DimensionList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )


@dataclass
class BaseTimeDataType(NameDescriptionType):
    """An abstract schema type used within the schema to derive other time
    based data types: RelativeTimeDataType and AbsoluteTimeDataType.

    An absolute time data type is a telemetered source/destination data
    type.  A data encoding must be set.  An optional epoch may be set.
    Time types are an exception to other primitives because, if the time
    data type is not telemetered, it still must have a data encoding
    set.  See DataEncodingType, AbsoluteTimeDataType and
    RelativeTimeDataType.

    :ivar encoding: Describes how the raw base counts of the time type
        are encoded/decoded.
    :ivar reference_time: Describes origin (epoch or reference) of this
        time type.
    :ivar base_type: Extend another absolute or relative time type.
    """

    encoding: Optional[EncodingType] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    reference_time: Optional[ReferenceTimeType] = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class BinaryDataType(BaseDataType):
    """A base schema type for describing a binary data engineering/calibrated
    type (often called “blob type”).

    The binary data may be of fixed or variable length, and has an
    optional encoding and decoding algorithm that may be defined to
    transform the data between space and ground.  See BaseDataType,
    BinaryParameterType and BinaryArgumentType.

    :ivar initial_value: Default/Initial value is always given in
        calibrated form.  Extra bits are truncated from the MSB
        (leftmost).
    """

    initial_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
            "format": "base16",
        },
    )


@dataclass
class BooleanDataType(BaseDataType):
    """A base schema type for describing a boolean data type which has two
    values only: ‘True’ (1) or ‘False’ (0).

    The values one and zero may be mapped to a specific string using the
    attributes oneStringValue and zeroStringValue.  This type is a
    simplified form of the EnumeratedDataType.  See BaseDataType,
    BooleanParameterType and BooleanArgumentType.

    :ivar initial_value: Default/Initial value is always given in
        calibrated form.
    :ivar one_string_value: Enumeration string representing the 1 value,
        with the default being 'True'.
    :ivar zero_string_value: Enumeration string representing the 0
        value, with the default being 'False'.
    """

    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    one_string_value: str = field(
        default="True",
        metadata={
            "name": "oneStringValue",
            "type": "Attribute",
        },
    )
    zero_string_value: str = field(
        default="False",
        metadata={
            "name": "zeroStringValue",
            "type": "Attribute",
        },
    )


@dataclass
class ContainerRefEntryType(SequenceEntryType):
    """
    An entry that is simply a reference to another container.
    """

    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ContainerSegmentRefEntryType(SequenceEntryType):
    """An entry that is only a portion of a container indicating that the
    entire container must be assembled from other container segments.

    It is assumed that container segments happen sequentially in time,
    that is the first part of a container is first, however (and there's
    always a however), if this is not the case the order of this
    container segment may be supplied with the order attribute where the
    first segment order="0".  Each instance of a container cannot
    overlap in the overall sequence with another instance
    """

    container_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "containerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class EnumeratedDataType(BaseDataType):
    """Describes an enumerated parameter type.

    The enumeration list consists of label/value pairs. See
    EnumerationListType, EnumeratedParameterType and
    EnumeratedArgumentType.

    :ivar enumeration_list: Unordered list of label/value pairs where
        values cannot be duplicated.
    :ivar initial_value: Default/Initial value is always given in
        calibrated form.  Use the label, it must be in the enumeration
        list to be valid.
    """

    enumeration_list: Optional[EnumerationListType] = field(
        default=None,
        metadata={
            "name": "EnumerationList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class FloatDataType(BaseDataType):
    """A base schema type for describing a floating point
    engineering/calibrated data type.

    Several encodings are supported.  Calibrated integer to float
    relationships should be described with this data type. Use the data
    encoding to define calibrators.  Joins integer as one of the
    numerics. See BaseDataType, FloatParameterType and
    FloatArgumentType.

    :ivar to_string: This element provides the implementation with
        assistance rendering the value as a string for users.
    :ivar valid_range: The Valid Range provides additional
        boundary/constraint information beyond that of the data encoding
        in the range of possible values that are meaningful to this
        parameter.  Not to be construed as an alarm definition,
        violations of the valid range make a parameter value
        "unreasonable", as opposed to reasonable to be reported, but in
        a state which should be of concern.
    :ivar initial_value: Initial value is always given in calibrated
        form
    :ivar size_in_bits: Optional hint to the implementation about the
        size of the engineering/calibrated data type to use internally.
        Generally this can be determined by examination of the space
        required to capture the full range of the encoding, but it is
        not always clear when calibrators are in use.  A tolerant
        implementation will endeavor to always make sufficient size
        engineering data types to capture the entire range of possible
        values.
    """

    to_string: Optional[ToStringType] = field(
        default=None,
        metadata={
            "name": "ToString",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    valid_range: Optional["FloatDataType.ValidRange"] = field(
        default=None,
        metadata={
            "name": "ValidRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    initial_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    size_in_bits: FloatSizeInBitsType = field(
        default=FloatSizeInBitsType.VALUE_32,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
        },
    )

    @dataclass
    class ValidRange(FloatRangeType):
        """
        :ivar valid_range_applies_to_calibrated: By default and general
            recommendation, the valid range is specified in
            engineering/calibrated values, although this can be
            adjusted.
        """

        valid_range_applies_to_calibrated: bool = field(
            default=True,
            metadata={
                "name": "validRangeAppliesToCalibrated",
                "type": "Attribute",
            },
        )


@dataclass
class IndirectParameterRefEntryType(SequenceEntryType):
    """An entry whose name is given by the value of a ParamameterInstance.

    This entry may be used to implement dwell telemetry streams.  The
    value of the parameter in ParameterInstance must use either the name
    of the Parameter or its alias.  If it's an alias name, the alias
    namespace is supplied as an attribute.
    """

    parameter_instance: Optional[ParameterInstanceRefType] = field(
        default=None,
        metadata={
            "name": "ParameterInstance",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    alias_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "aliasNameSpace",
            "type": "Attribute",
        },
    )


@dataclass
class IntegerDataType(BaseDataType):
    """Describe an integer engineering/calibrated data type.

    Several encodings are supported.  See BaseDataType,
    IntegerParameterType and IntegerArgumentType.

    :ivar to_string: This element provides the implementation with
        assistance rendering the value as a string for users.
    :ivar valid_range: The Valid Range provides additional
        boundary/constraint information beyond that of the data encoding
        in the range of possible values that are meaningful to this
        parameter.  Not to be construed as an alarm definition,
        violations of the valid range make a parameter value
        "unreasonable", as opposed to reasonable to be reported, but in
        a state which should be of concern.
    :ivar initial_value: Default/Initial value is always given in
        calibrated form.  Default is base 10 form; binary, octal, or
        hexadecimal values may be given by preceding value with 0[b|B],
        0[o|O|, 0[x|X] respectively.
    :ivar size_in_bits: Optional hint to the implementation about the
        size of the engineering/calibrated data type to use internally.
        Generally this can be determined by examination of the space
        required to capture the full range of the encoding, but it is
        not always clear when calibrators are in use.  A tolerant
        implementation will endeavor to always make sufficient size
        engineering data types to capture the entire range of possible
        values.
    :ivar signed: Flag indicating if the engineering/calibrated data
        type used should support signed representation.  This should not
        be confused with the encoding type for the raw value.  The
        default is true.
    """

    to_string: Optional[ToStringType] = field(
        default=None,
        metadata={
            "name": "ToString",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    valid_range: Optional["IntegerDataType.ValidRange"] = field(
        default=None,
        metadata={
            "name": "ValidRange",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    initial_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    size_in_bits: int = field(
        default=32,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    signed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class ValidRange(IntegerRangeType):
        """
        :ivar valid_range_applies_to_calibrated: By default and general
            recommendation, the valid range is specified in
            engineering/calibrated values, although this can be
            adjusted.
        """

        valid_range_applies_to_calibrated: bool = field(
            default=True,
            metadata={
                "name": "validRangeAppliesToCalibrated",
                "type": "Attribute",
            },
        )


@dataclass
class ParameterRefEntryType(SequenceEntryType):
    """
    An entry that is a single Parameter.
    """

    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )


@dataclass
class ParameterSegmentRefEntryType(SequenceEntryType):
    """An entry that is only a portion of a parameter value indicating that the
    entire parameter value must be assembled from other parameter segments.

    It is assumed that parameter segments happen sequentially in time,
    that is the first part if a telemetry parameter first, however (and
    there's always a however), if this is not the case the order of this
    parameter segment may be supplied with the order attribute where the
    first segment order="0".
    """

    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class StreamSegmentEntryType(SequenceEntryType):
    """
    An entry that is a portion of a stream (streams are by definition, assumed
    continuous)   It is assumed that stream segments happen sequentially in
    time, that is the first part if a steam first, however, if this is not the
    case the order of the stream segments may be supplied with the order
    attribute where the first segment order="0".
    """

    stream_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "streamRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    size_in_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "sizeInBits",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class StringDataType(BaseDataType):
    """Defines a base schema type for StringParameterType and
    StringArgumentType, adding initial value, restriction pattern, character
    width, and size range in characters.

    The initial value if set is the initial value of all instances of
    the child types.  The restriction pattern is a regular expression
    enforcing the string value to this pattern.  The character width is
    on the local data type side.  And the size range in character
    restricts the character set.  For telemetered values, if the
    restriction pattern of size range in character is not met, the item
    is invalid. See BaseDataType, StringParameterType,
    StringArgumentType, CharacterWidthType and IntegerRangeType.

    :ivar size_range_in_characters: The size in bits may be greater than
        or equal to minInclusive.  It may be less than or equal to
        maxInclusive.  They both may be set indicating a closed range.
    :ivar initial_value: Initial values for string types, may include C
        language style (\\n, \\t, \\", \\\\, etc.) escape sequences.
    :ivar restriction_pattern: restriction pattern is a regular
        expression
    :ivar character_width:
    """

    size_range_in_characters: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "SizeRangeInCharacters",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    initial_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )
    restriction_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "restrictionPattern",
            "type": "Attribute",
        },
    )
    character_width: Optional[CharacterWidthType] = field(
        default=None,
        metadata={
            "name": "characterWidth",
            "type": "Attribute",
        },
    )


@dataclass
class AbsoluteTimeDataType(BaseTimeDataType):
    """A base schema type for describing an absolute time data type.

    Contains an absolute (to a known epoch) time.  Use the [ISO 8601]
    extended format CCYY-MM-DDThh:mm:ss where "CC" represents the
    century, "YY" the year, "MM" the month and "DD" the day, preceded by
    an optional leading "-" sign to indicate a negative number. If the
    sign is omitted, "+" is assumed. The letter "T" is the date/time
    separator and "hh", "mm", "ss" represent hour, minute and second
    respectively. Additional digits can be used to increase the
    precision of fractional seconds if desired i.e. the format ss.ss...
    with any number of digits after the decimal point is supported. See
    AbsoluteTimeParameterType and AbsoluteTimeArgumentType.  See
    AbsouteTimeParameterType, AbsoluteTimeArgumentType and
    BaseTimeDataType.

    :ivar initial_value: Default/Initial value is always given in
        calibrated form.
    """

    initial_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentAbsoluteTimeDataType(ArgumentBaseTimeDataType):
    """A base schema type for describing an absolute time data type.

    Contains an absolute (to a known epoch) time.  Use the [ISO 8601]
    extended format CCYY-MM-DDThh:mm:ss where "CC" represents the
    century, "YY" the year, "MM" the month and "DD" the day, preceded by
    an optional leading "-" sign to indicate a negative number. If the
    sign is omitted, "+" is assumed. The letter "T" is the date/time
    separator and "hh", "mm", "ss" represent hour, minute and second
    respectively. Additional digits can be used to increase the
    precision of fractional seconds if desired i.e. the format ss.ss...
    with any number of digits after the decimal point is supported. See
    AbsoluteTimeParameterType and AbsoluteTimeArgumentType.  See
    AbsouteTimeParameterType, AbsoluteTimeArgumentType and
    BaseTimeDataType.

    :ivar initial_value: Default/Initial value is always given in
        calibrated form.
    """

    initial_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class ArgumentRelativeTimeDataType(ArgumentBaseTimeDataType):
    """Used to contain a relative time value.

    Used to describe a relative time.  Normally used for time offsets.
    A Relative time is expressed as PnYn MnDTnH nMnS, where nY
    represents the number of years, nM the number of months, nD the
    number of days, 'T' is the date/time separator, nH the number of
    hours, nM the number of minutes and nS the number of seconds. The
    number of seconds can include decimal digits to arbitrary precision.
    For example, to indicate a duration of 1 year, 2 months, 3 days, 10
    hours, and 30 minutes, one would write: P1Y2M3DT10H30M. One could
    also indicate a duration of minus 120 days as: -P120D.  An extension
    of Schema duration type.
    """

    initial_value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class BinaryArgumentType(ArgumentBinaryDataType):
    """Defines a binary engineering/calibrated argument type (often called
    “blob type”).

    The binary data may be of fixed or variable length, and has an
    optional encoding and decoding algorithm that may be defined to
    transform the data between space and ground.  See
    BinaryDataEncodingType, IntegerValueType, InputAlgorithmType, and
    BinaryDataType.
    """


@dataclass
class BinaryParameterType(BinaryDataType):
    """Describe a binary engineering/calibrated parameter type (sometimes
    called a “blob type”).

    It may be of fixed or variable length, and has an optional encoding
    and decoding algorithm that may be defined to transform the data
    between space and ground.  See BinaryDataEncodingType,
    IntegerValueType, InputAlgorithmType and BinaryDataType.

    :ivar default_alarm: Optionally describe an alarm monitoring
        specification that is effective whenever a contextual alarm
        definition does not take precedence.
    :ivar binary_context_alarm_list: Optionally describe one or more
        alarm monitoring specifications that are effective whenever a
        contextual match definition evaluates to true.  The first match
        that evaluates to true takes precedence.
    """

    default_alarm: Optional[BinaryAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    binary_context_alarm_list: Optional[BinaryContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "BinaryContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class BooleanArgumentType(ArgumentBooleanDataType):
    """Defines a boolean argument type which has two values only: ‘True’ (1) or
    ‘False’ (0).

    The values one and zero may be mapped to a specific string using the
    attributes oneStringValue and zeroStringValue.  This type is a
    simplified form of the EnumeratedDataType.  See IntegerDataEncoding
    and BooleanDataType.
    """


@dataclass
class BooleanParameterType(BooleanDataType):
    """Describe a boolean parameter type which has two values only: ‘True’ (1)
    or ‘False’ (0).

    The values one and zero may be mapped to a specific string using the
    attributes oneStringValue and zeroStringValue.  This type is a
    simplified form of the EnumeratedDataType.  See IntegerDataEncoding
    and BooleanDataType.

    :ivar default_alarm: Optionally describe an alarm monitoring
        specification that is effective whenever a contextual alarm
        definition does not take precedence.
    :ivar context_alarm_list: Optionally describe one or more alarm
        monitoring specifications that are effective whenever a
        contextual match definition evaluates to true.  The first match
        that evaluates to true takes precedence.
    """

    default_alarm: Optional[BooleanAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_alarm_list: Optional[BooleanContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "ContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class CommandContainerEntryListType:
    """Describe an entry list for a CommandContainer which is associated with a
    MetaCommand.

    The entry list for a MetaCommand CommandContainer element operates
    in a similar fashion as the entry list element for a
    SequenceContainer element.  It adds fixed value and argument entries
    to the entry list not present in sequence containers.  See
    MetaCommandType, CommandContainerType and EntryListType.

    :ivar parameter_ref_entry: Specify a Parameter to be a part of this
        container layout definition.
    :ivar parameter_segment_ref_entry: Specify a portion of a Parameter
        to be a part of this container layout definition.  This is used
        when the Parameter is reported in fractional parts in the
        container before being fully updated.
    :ivar container_ref_entry: Specify the content of another Container
        to be a part of this container layout definition.
    :ivar container_segment_ref_entry: Specify a portion of another
        Container to be a part of this container layout definition.
    :ivar stream_segment_entry: Specify a portion of a Stream to be a
        part of this container layout definition.
    :ivar indirect_parameter_ref_entry: Specify a previous (not last
        reported) value of a Parmeter to be a part of this container
        layout definition.
    :ivar array_parameter_ref_entry: Specify an Array Type Parameter to
        be a part of this container layout definition when the Container
        does not populate the entire space of the Array contents.  If
        the entire space of the Array is populated, a tolerant
        implementation will accept ParameterRefEntry also.
    :ivar argument_ref_entry: Specify an Argument to be a part of this
        container layout definition.
    :ivar array_argument_ref_entry: Specify an Array Type Argument to be
        a part of this container layout definition when the Container
        does not populate the entire space of the Array contents.  If
        the entire space of the Array is populated, a tolerant
        implementation will accept ArgumentRefEntry also.
    :ivar fixed_value_entry: Specify an immutable value to be a part of
        this container layout definition.
    """

    parameter_ref_entry: List[ArgumentParameterRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_segment_ref_entry: List[ArgumentParameterSegmentRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterSegmentRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_ref_entry: List[ArgumentContainerRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ContainerRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_segment_ref_entry: List[ArgumentContainerSegmentRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ContainerSegmentRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    stream_segment_entry: List[ArgumentStreamSegmentEntryType] = field(
        default_factory=list,
        metadata={
            "name": "StreamSegmentEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    indirect_parameter_ref_entry: List[ArgumentIndirectParameterRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "IndirectParameterRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    array_parameter_ref_entry: List[ArgumentArrayParameterRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ArrayParameterRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    argument_ref_entry: List[ArgumentArgumentRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ArgumentRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    array_argument_ref_entry: List[ArgumentArrayArgumentRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ArrayArgumentRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    fixed_value_entry: List[ArgumentFixedValueEntryType] = field(
        default_factory=list,
        metadata={
            "name": "FixedValueEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class EntryListType:
    """Contains an ordered list of Entries.

    Used in Sequence Container

    :ivar parameter_ref_entry: Specify a Parameter to be a part of this
        container layout definition.
    :ivar parameter_segment_ref_entry: Specify a portion of a Parameter
        to be a part of this container layout definition.  This is used
        when the Parameter is reported in fractional parts in the
        container before being fully updated.
    :ivar container_ref_entry: Specify the content of another Container
        to be a part of this container layout definition.
    :ivar container_segment_ref_entry: Specify a portion of another
        Container to be a part of this container layout definition.
    :ivar stream_segment_entry: Specify a portion of a Stream to be a
        part of this container layout definition.
    :ivar indirect_parameter_ref_entry: Specify a previous (not last
        reported) value of a Parmeter to be a part of this container
        layout definition.
    :ivar array_parameter_ref_entry: Specify an Array Type Parameter to
        be a part of this container layout definition when the Container
        does not populate the entire space of the Array contents.  If
        the entire space of the Array is populated, a tolerant
        implementation will accept ParameterRefEntry also.
    """

    parameter_ref_entry: List[ParameterRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_segment_ref_entry: List[ParameterSegmentRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ParameterSegmentRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_ref_entry: List[ContainerRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ContainerRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_segment_ref_entry: List[ContainerSegmentRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ContainerSegmentRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    stream_segment_entry: List[StreamSegmentEntryType] = field(
        default_factory=list,
        metadata={
            "name": "StreamSegmentEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    indirect_parameter_ref_entry: List[IndirectParameterRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "IndirectParameterRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    array_parameter_ref_entry: List[ArrayParameterRefEntryType] = field(
        default_factory=list,
        metadata={
            "name": "ArrayParameterRefEntry",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class EnumeratedArgumentType(ArgumentEnumeratedDataType):
    """Describes an enumerated argument type.

    The enumeration list consists of label/value pairs. See
    EnumerationListType, IntegerDataEncodingType and EnumeratedDataType.
    """


@dataclass
class EnumeratedParameterType(EnumeratedDataType):
    """Describe an enumerated parameter type.

    The enumeration list consists of label/value pairs. See
    EnumerationListType, IntegerDataEncodingType and EnumeratedDataType.

    :ivar default_alarm: Describe labels for this parameter that should
        be in an alarm state.  The default definition applies when there
        are no context alarm definitions or all the context alarm
        definitions evaluate to false in their matching criteria.
    :ivar context_alarm_list: Describe labels for this parameter that
        should be in an alarm state when another parameter and value
        combination evaluates to true using the described matching
        criteria.
    """

    default_alarm: Optional[EnumerationAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_alarm_list: Optional[EnumerationContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "ContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class FloatArgumentType(ArgumentFloatDataType):
    """Describe a floating point argument type.

    Several encodings are supported.  Calibrated integer to float
    relationships should be described with this data type. Use the data
    encoding to define calibrators.  Joins integer as one of the
    numerics. See FloatDataEncodingType, IntegerDataEncodingType and
    FloatDataType.

    :ivar valid_range_set: Provides additional platform/program specific
        ranging information.
    """

    valid_range_set: Optional[ValidFloatRangeSetType] = field(
        default=None,
        metadata={
            "name": "ValidRangeSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class FloatParameterType(FloatDataType):
    """Describe a floating point parameter type.

    Several encodings are supported.  Calibrated integer to float
    relationships should be described with this data type. Use the data
    encoding to define calibrators.  Joins integer as one of the
    numerics. See FloatDataEncodingType, IntegerDataEncodingType and
    FloatDataType.

    :ivar default_alarm: Default alarm definitions are those which do
        not adjust definition logic based on the value of other
        parameters.  Other parameters may participate in the
        determination of an alarm condition for this parameter, but the
        definition logic of the alarm on this parameter is constant.  If
        the alarming logic on this parameter changes based on the value
        of other parameters, then it is a ContextAlarm and belongs in
        the ContextAlarmList element.
    :ivar context_alarm_list: Context alarm definitions are those which
        adjust the definition logic for this parameter based on the
        value of other parameters.  A context which evaluates to being
        in effect, based on the testing of another parameter, takes
        precedence over the default alarms in the DefaultAlarm element.
        If the no context alarm evaluates to being in effect, based on
        the testing of another parameter, then the default alarm
        definitions from the DefaultAlarm element will remain in effect.
        If multiple contexts evaluate to being in effect, then the first
        one that appears will take precedence.
    """

    default_alarm: Optional[NumericAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_alarm_list: Optional[NumericContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "ContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class IntegerArgumentType(ArgumentIntegerDataType):
    """Describes an integer argument type.

    Several encodings supported.  Calibrated integer to integer
    relationships should be described with this data type. Use the
    integer data encoding to define calibrators. Joins float as one of
    the numerics. See IntegerDataEncoding and IntegerDataType.

    :ivar valid_range_set: Provides additional platform/program specific
        ranging information.
    """

    valid_range_set: Optional[ValidIntegerRangeSetType] = field(
        default=None,
        metadata={
            "name": "ValidRangeSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class IntegerParameterType(IntegerDataType):
    """Describe an integer parameter type.

    Several are supported. Calibrated integer to integer relationships
    should be described with this data type. Use the integer data
    encoding to define calibrators. Joins float as one of the numerics.
    See IntegerDataEncoding and IntegerDataType.

    :ivar default_alarm: Default alarm definitions are those which do
        not adjust definition logic based on the value of other
        parameters. Other parameters may participate in the
        determination of an alarm condition for this parameter, but the
        definition logic of the alarm on this parameter is constant. If
        the alarming logic on this parameter changes based on the value
        of other parameters, then it is a ContextAlarm and belongs in
        the ContextAlarmList element.
    :ivar context_alarm_list: Context alarm definitions are those which
        adjust the definition logic for this parameter based on the
        value of other parameters. A context which evaluates to being in
        effect, based on the testing of another parameter, takes
        precedence over the default alarms in the DefaultAlarm element.
        If the no context alarm evaluates to being in effect, based on
        the testing of another parameter, then the default alarm
        definitions from the DefaultAlarm element will remain in effect.
        If multiple contexts evaluate to being in effect, then the first
        one that appears will take precedence.
    """

    default_alarm: Optional[NumericAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_alarm_list: Optional[NumericContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "ContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class RelativeTimeDataType(BaseTimeDataType):
    """Used to contain a relative time value.

    Used to describe a relative time.  Normally used for time offsets.
    A Relative time is expressed as PnYn MnDTnH nMnS, where nY
    represents the number of years, nM the number of months, nD the
    number of days, 'T' is the date/time separator, nH the number of
    hours, nM the number of minutes and nS the number of seconds. The
    number of seconds can include decimal digits to arbitrary precision.
    For example, to indicate a duration of 1 year, 2 months, 3 days, 10
    hours, and 30 minutes, one would write: P1Y2M3DT10H30M. One could
    also indicate a duration of minus 120 days as: -P120D.  An extension
    of Schema duration type.
    """

    initial_value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "initialValue",
            "type": "Attribute",
        },
    )


@dataclass
class StringArgumentType(ArgumentStringDataType):
    """Describes a string parameter type.

    Three forms are supported: fixed length, variable length and
    variable length using a prefix. See StringDataEncodingType and
    StringDataType.
    """


@dataclass
class StringParameterType(StringDataType):
    """Describes a string parameter type.

    Three forms are supported: fixed length, variable length and
    variable length using a prefix. See StringDataEncodingType and
    StringDataType.

    :ivar default_alarm: Default alarm definitions are those which do
        not adjust definition logic based on the value of other
        parameters.  Other parameters may participate in the
        determination of an alarm condition for this parameter, but the
        definition logic of the alarm on this parameter is constant.  If
        the alarming logic on this parameter changes based on the value
        of other parameters, then it is a ContextAlarm and belongs in
        the ContextAlarmList element.
    :ivar context_alarm_list: Context alarm definitions are those which
        adjust the definition logic for this parameter based on the
        value of other parameters.  A context which evaluates to being
        in effect, based on the testing of another parameter, takes
        precedence over the default alarms in the DefaultAlarm element.
        If the no context alarm evaluates to being in effect, based on
        the testing of another parameter, then the default alarm
        definitions from the DefaultAlarm element will remain in effect.
        If multiple contexts evaluate to being in effect, then the first
        one that appears will take precedence.
    """

    default_alarm: Optional[StringAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_alarm_list: Optional[StringContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "ContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class AbsoluteTimeArgumentType(ArgumentAbsoluteTimeDataType):
    """Describe an absolute time argument type relative to a known epoch (such
    as TAI).

    The string representation of this time should use the [ISO 8601]
    extended format CCYY-MM-DDThh:mm:ss where "CC" represents the
    century, "YY" the year, "MM" the month and "DD" the day, preceded by
    an optional leading "-" sign to indicate a negative number. If the
    sign is omitted, "+" is assumed. The letter "T" is the date/time
    separator and "hh", "mm", "ss" represent hour, minute and second
    respectively. Additional digits can be used to increase the
    precision of fractional seconds if desired i.e. the format ss.ss...
    with any number of digits after the decimal point is supported.  See
    TAIType, IntegerDataEncoding and AbsoluteTimeDataType.
    """


@dataclass
class AbsoluteTimeParameterType(AbsoluteTimeDataType):
    """Describe an absolute time parameter type relative to a known epoch (such
    as TAI).

    The string representation of this time should use the [ISO 8601]
    extended format CCYY-MM-DDThh:mm:ss where "CC" represents the
    century, "YY" the year, "MM" the month and "DD" the day, preceded by
    an optional leading "-" sign to indicate a negative number. If the
    sign is omitted, "+" is assumed. The letter "T" is the date/time
    separator and "hh", "mm", "ss" represent hour, minute and second
    respectively. Additional digits can be used to increase the
    precision of fractional seconds if desired i.e. the format ss.ss...
    with any number of digits after the decimal point is supported.  See
    TAIType, IntegerDataEncoding and AbsoluteTimeDataType.
    """


@dataclass
class CommandContainerType(ContainerType):
    """Describe a MetaCommand command container.

    The command container may contain arguments, parameters, other basic
    containers, and fixed values.  Arguments are supplied by the user of
    a commanding application; parameters are supplied by the controlling
    system.  Parameters and arguments map source data types to
    encodings.   See MetaCommandType.

    :ivar entry_list: List of item entries to pack/encode into this
        container definition.
    :ivar base_container: When a MetaCommand inherits/extends another
        MetaCommand, this references the CommandContainer from the
        BaseMetaCommand.
    """

    entry_list: Optional[CommandContainerEntryListType] = field(
        default=None,
        metadata={
            "name": "EntryList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    base_container: Optional[BaseContainerType] = field(
        default=None,
        metadata={
            "name": "BaseContainer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class RelativeTimeArgumentType(ArgumentRelativeTimeDataType):
    """Describes a relative time argument type.

    Relative time parameters are time offsets (e.g. 10 second, 1.24
    milliseconds, etc.) See IntegerDataEncodingType, FloatDataEncoding
    and RelativeTimeDataType.
    """


@dataclass
class RelativeTimeParameterType(RelativeTimeDataType):
    """Describes a relative time parameter type.

    Relative time parameters are time offsets (e.g. 10 second, 1.24
    milliseconds, etc.) See IntegerDataEncodingType, FloatDataEncoding
    and RelativeTimeDataType.

    :ivar default_alarm: Default alarm definitions are those which do
        not adjust definition logic based on the value of other
        parameters.  Other parameters may participate in the
        determination of an alarm condition for this parameter, but the
        definition logic of the alarm on this parameter is constant.  If
        the alarming logic on this parameter changes based on the value
        of other parameters, then it is a ContextAlarm and belongs in
        the ContextAlarmList element.
    :ivar context_alarm_list: Context alarm definitions are those which
        adjust the definition logic for this parameter based on the
        value of other parameters.  A context which evaluates to being
        in effect, based on the testing of another parameter, takes
        precedence over the default alarms in the DefaultAlarm element.
        If the no context alarm evaluates to being in effect, based on
        the testing of another parameter, then the default alarm
        definitions from the DefaultAlarm element will remain in effect.
        If multiple contexts evaluate to being in effect, then the first
        one that appears will take precedence.
    """

    default_alarm: Optional[TimeAlarmType] = field(
        default=None,
        metadata={
            "name": "DefaultAlarm",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_alarm_list: Optional[TimeContextAlarmListType] = field(
        default=None,
        metadata={
            "name": "ContextAlarmList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class SequenceContainerType(ContainerType):
    """Describes the binary layout/packing of data and also related properties,
    including an entry list of parameters, parameter segments, array
    parameters, stream segments, containers, and container segments.

    Sequence containers may extend other sequence containers (see
    BaseContainerType).   The parent container’s entries are placed
    before the entries in the child container forming one entry list.
    An inheritance chain may be formed using this mechanism, but only
    one entry list is being created.  Sequence containers may be marked
    as "abstract", when this occurs an instance of it cannot itself be
    created.  The idle pattern is part of any unallocated space in the
    container.  See EntryListType.

    :ivar entry_list: List of item entries to pack/encode into this
        container definition.
    :ivar base_container: Optional inheritance for this container from
        another named container.
    :ivar abstract: Abstract container definitions that are not
        instantiated, rather only used as bases to inherit from to
        create specialized container definitions.
    :ivar idle_pattern: The idle pattern is part of any unallocated
        space in the container.  This is uncommon.
    """

    entry_list: Optional[EntryListType] = field(
        default=None,
        metadata={
            "name": "EntryList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "required": True,
        },
    )
    base_container: Optional[BaseContainerType] = field(
        default=None,
        metadata={
            "name": "BaseContainer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    idle_pattern: Union[int, str] = field(
        default="0x0",
        metadata={
            "name": "idlePattern",
            "type": "Attribute",
            "pattern": r"0[xX][0-9a-fA-F]+",
        },
    )


@dataclass
class ArgumentTypeSetType:
    """Describe an unordered collection of argument type definitions.

    These types named for the engineering/calibrated type of the
    argument.  See BaseDataType and BaseTimeDataType.

    :ivar string_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of a character string.
    :ivar enumerated_argument_type: Describe an argument type that has
        an engineering/calibrated value in the form of an enumeration.
    :ivar integer_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of an integer.
    :ivar binary_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of a binary (usually
        hex represented).
    :ivar float_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of a decimal.
    :ivar boolean_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of a boolean
        enumeration.
    :ivar relative_time_agument_type: Describe an argument type that has
        an engineering/calibrated value in the form of a duration in
        time.
    :ivar absolute_time_argument_type: Describe an argument type that
        has an engineering/calibrated value in the form of an instant in
        time.
    :ivar array_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of an array of a
        primitive type.
    :ivar aggregate_argument_type: Describe an argument type that has an
        engineering/calibrated value in the form of a structure of
        arguments of other types.
    """

    string_argument_type: List[StringArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "StringArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    enumerated_argument_type: List[EnumeratedArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "EnumeratedArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    integer_argument_type: List[IntegerArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "IntegerArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    binary_argument_type: List[BinaryArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "BinaryArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    float_argument_type: List[FloatArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "FloatArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    boolean_argument_type: List[BooleanArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "BooleanArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    relative_time_agument_type: List[RelativeTimeArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "RelativeTimeAgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    absolute_time_argument_type: List[AbsoluteTimeArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "AbsoluteTimeArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    array_argument_type: List[ArrayArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "ArrayArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    aggregate_argument_type: List[AggregateArgumentType] = field(
        default_factory=list,
        metadata={
            "name": "AggregateArgumentType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class CommandContainerSetType:
    """
    Contains an unordered Set of Command Containers.
    """

    command_container: List[SequenceContainerType] = field(
        default_factory=list,
        metadata={
            "name": "CommandContainer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "min_occurs": 1,
        },
    )


@dataclass
class ContainerSetType:
    """
    Unordered Set of Containers.

    :ivar sequence_container: SequenceContainers define sequences of
        parameters or other containers.
    """

    sequence_container: List[SequenceContainerType] = field(
        default_factory=list,
        metadata={
            "name": "SequenceContainer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class MetaCommandType(NameDescriptionType):
    """Describe a command which consists of an abstract portion (MetaCommand)
    and an optional packaging portion (MetaCommand CommandContainer).

    An argument list is provided. MetaCommand may extend other
    MetaCommands and their CommandContainer may extend other
    CommandContainer or SequenceContainers.  A MetaCommand’s
    CommandContainer is private except as referred to in BaseMetaCommand
    (they are not visible to other containers and cannot be used in an
    entry list). MetaCommands may also define various other behavioral
    aspects of a command such as command verifiers.  See
    CommandContainerType, ArgumentListType, BaseMetaCommandType and
    BaseContainerType.

    :ivar base_meta_command: Optional inheritance for this MetaCommand
        from another named MetaCommand.
    :ivar system_name: Optional.  Normally used when the database is
        built in a flat, non-hierarchical format.  May be used by
        implementations to group MetaCommands together.
    :ivar argument_list: Many commands have one or more options.  These
        are called command arguments.  Command arguments may be of any
        of the standard data types.  MetaCommand arguments are local to
        the MetaCommand, but may be referenced in inherited MetaCommand
        definitions, generally to apply Argument Assignments to the
        values.
    :ivar command_container: Tells how to package/encode this command
        definition in binary form.
    :ivar transmission_constraint_list: List of constraints to check
        when sending this command.
    :ivar default_significance: Some Command and Control Systems may
        require special user access or confirmations before transmitting
        commands with certain levels.  The level is inherited from the
        Base MetaCommand.
    :ivar context_significance_list: Some Command and Control Systems
        may require special user access or confirmations before
        transmitting commands with certain levels.  In addition to the
        default, Significance can be defined in contexts where it
        changes based on the values of parameters.
    :ivar interlock: An Interlock is a type of Constraint, but not on
        Command instances of this MetaCommand; Interlocks apply instead
        to the next command.  An Interlock will block successive
        commands until this command has reached a certain stage (through
        verifications).  Interlocks are scoped to a SpaceSystem basis.
    :ivar verifier_set: Functional list of conditions/changes to check
        after sending this command to determine success or failure.
    :ivar parameter_to_set_list: List of parameters to set new values
        upon completion of sending this command.
    :ivar parameters_to_suspend_alarms_on_set: List of parameters to
        suspend alarm processing/detection upon completion of sending
        this command.
    :ivar abstract: Abstract MetaCommand definitions that are not
        instantiated, rather only used as bases to inherit from to
        create specialized command definitions.
    """

    base_meta_command: Optional[BaseMetaCommandType] = field(
        default=None,
        metadata={
            "name": "BaseMetaCommand",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemName",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    argument_list: Optional[ArgumentListType] = field(
        default=None,
        metadata={
            "name": "ArgumentList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    command_container: Optional[CommandContainerType] = field(
        default=None,
        metadata={
            "name": "CommandContainer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    transmission_constraint_list: Optional[TransmissionConstraintListType] = field(
        default=None,
        metadata={
            "name": "TransmissionConstraintList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    default_significance: Optional[SignificanceType] = field(
        default=None,
        metadata={
            "name": "DefaultSignificance",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    context_significance_list: Optional[ContextSignificanceListType] = field(
        default=None,
        metadata={
            "name": "ContextSignificanceList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    interlock: Optional[InterlockType] = field(
        default=None,
        metadata={
            "name": "Interlock",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    verifier_set: Optional[VerifierSetType] = field(
        default=None,
        metadata={
            "name": "VerifierSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_to_set_list: Optional[ParameterToSetListType] = field(
        default=None,
        metadata={
            "name": "ParameterToSetList",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameters_to_suspend_alarms_on_set: Optional[ParametersToSuspendAlarmsOnSetType] = field(
        default=None,
        metadata={
            "name": "ParametersToSuspendAlarmsOnSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ParameterTypeSetType:
    """Describe an unordered collection of parameter type definitions.

    These types named for the engineering/calibrated type of the
    parameter.  See BaseDataType and BaseTimeDataType.

    :ivar string_parameter_type: Describe a parameter type that has an
        engineering/calibrated value in the form of a character string.
    :ivar enumerated_parameter_type: Describe a parameter type that has
        an engineering/calibrated value in the form of an enumeration.
    :ivar integer_parameter_type: Describe a parameter type that has an
        engineering/calibrated value in the form of an integer.
    :ivar binary_parameter_type: Describe a parameter type that has an
        engineering/calibrated value in the form of a binary (usually
        hex represented).
    :ivar float_parameter_type: Describe a parameter type that has an
        engineering/calibrated value in the form of a decimal.
    :ivar boolean_parameter_type: Describe a parameter type that has an
        engineering/calibrated value in the form of a boolean
        enumeration.
    :ivar relative_time_parameter_type: Describe a parameter type that
        has an engineering/calibrated value in the form of a duration in
        time.
    :ivar absolute_time_parameter_type: Describe a parameter type that
        has an engineering/calibrated value in the form of an instant in
        time.
    :ivar array_parameter_type: Describe a parameter type that has an
        engineering/calibrated value in the form of an array of a
        primitive type.
    :ivar aggregate_parameter_type: Describe a parameter type that has
        an engineering/calibrated value in the form of a structure of
        parameters of other types.
    """

    string_parameter_type: List[StringParameterType] = field(
        default_factory=list,
        metadata={
            "name": "StringParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    enumerated_parameter_type: List[EnumeratedParameterType] = field(
        default_factory=list,
        metadata={
            "name": "EnumeratedParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    integer_parameter_type: List[IntegerParameterType] = field(
        default_factory=list,
        metadata={
            "name": "IntegerParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    binary_parameter_type: List[BinaryParameterType] = field(
        default_factory=list,
        metadata={
            "name": "BinaryParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    float_parameter_type: List[FloatParameterType] = field(
        default_factory=list,
        metadata={
            "name": "FloatParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    boolean_parameter_type: List[BooleanParameterType] = field(
        default_factory=list,
        metadata={
            "name": "BooleanParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    relative_time_parameter_type: List[RelativeTimeParameterType] = field(
        default_factory=list,
        metadata={
            "name": "RelativeTimeParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    absolute_time_parameter_type: List[AbsoluteTimeParameterType] = field(
        default_factory=list,
        metadata={
            "name": "AbsoluteTimeParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    array_parameter_type: List[ArrayParameterType] = field(
        default_factory=list,
        metadata={
            "name": "ArrayParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    aggregate_parameter_type: List[AggregateParameterType] = field(
        default_factory=list,
        metadata={
            "name": "AggregateParameterType",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class MetaCommandSetType:
    """Describes an unordered collection of command definitions.

    Duplicates are invalid based on the name attribute of MetaCommand
    and BlockMetaCommand.  See MetaCommandType and BlockMetaCommandType.

    :ivar meta_command: All atomic commands to be sent on this mission
        are listed here.  In addition this area has verification and
        validation information.
    :ivar meta_command_ref: Used to include a MetaCommand defined in
        another sub-system in this sub-system.
    :ivar block_meta_command: Used to define a command that includes
        more than one atomic MetaCommand definition.
    """

    meta_command: List[MetaCommandType] = field(
        default_factory=list,
        metadata={
            "name": "MetaCommand",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    meta_command_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MetaCommandRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "pattern": r"/?(([^./:\[\]]+|\.|\.\.)/)*([^./:\[\]]+)+",
        },
    )
    block_meta_command: List[BlockMetaCommandType] = field(
        default_factory=list,
        metadata={
            "name": "BlockMetaCommand",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class TelemetryMetaDataType:
    """
    All the data about telemetry is contained in TelemetryMetaData.

    :ivar parameter_type_set: A list of parameter types
    :ivar parameter_set: A list of Parameters for this Space System.
    :ivar container_set: Holds the list of all potential container
        definitions for telemetry. Containers may parts of packets or
        TDM, and then groups of the containers, and then an entire
        entity -- such as a packet.  In order to maximize re-used for
        duplication, the pieces may defined once here, and then
        assembled as needed into larger structures, also here.
    :ivar message_set: Messages are an alternative method of uniquely
        identifying containers within a Service.  A message provides a
        test in the form of MatchCriteria to match to a container.  A
        simple example might be: [When minorframeID=21, the message is
        the 21st minorframe container.  The collection of messages to
        search thru will be bound by a Service.
    :ivar stream_set:
    :ivar algorithm_set:
    """

    parameter_type_set: Optional[ParameterTypeSetType] = field(
        default=None,
        metadata={
            "name": "ParameterTypeSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_set: Optional[ParameterSetType] = field(
        default=None,
        metadata={
            "name": "ParameterSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    container_set: Optional[ContainerSetType] = field(
        default=None,
        metadata={
            "name": "ContainerSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    message_set: Optional[MessageSetType] = field(
        default=None,
        metadata={
            "name": "MessageSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    stream_set: Optional[StreamSetType] = field(
        default=None,
        metadata={
            "name": "StreamSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    algorithm_set: Optional[AlgorithmSetType] = field(
        default=None,
        metadata={
            "name": "AlgorithmSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class CommandMetaDataType:
    """Describe command related metadata.

    Items defined in this area may refer to items defined in
    TelemetryMetaData.  See TelemetryMetaDataType.

    :ivar parameter_type_set: A list of parameter types.
    :ivar parameter_set: Parameters referenced by MetaCommands.  This
        Parameter Set is located here so that MetaCommand data can be
        built independently of TelemetryMetaData.
    :ivar argument_type_set: A list of argument types.  MetaCommand
        definitions can contain arguments and parameters.  Arguments are
        user provided to the specific command definition.  Parameters
        are provided/calculated/determined by the software creating the
        command instance.  As a result, arguments contain separate type
        information.  In some cases, arguments have different
        descriptive characteristics.
    :ivar meta_command_set: A list of command definitions with their
        arguments, parameters, and container encoding descriptions.
    :ivar command_container_set: Similar to the ContainerSet for
        telemetry, the CommandContainerSet contains containers that can
        be referenced/shared by MetaCommand definitions.
    :ivar stream_set: Contains an unordered set of Streams.
    :ivar algorithm_set: Contains an unordered set of Algorithms.
    """

    parameter_type_set: Optional[ParameterTypeSetType] = field(
        default=None,
        metadata={
            "name": "ParameterTypeSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    parameter_set: Optional[ParameterSetType] = field(
        default=None,
        metadata={
            "name": "ParameterSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    argument_type_set: Optional[ArgumentTypeSetType] = field(
        default=None,
        metadata={
            "name": "ArgumentTypeSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    meta_command_set: Optional[MetaCommandSetType] = field(
        default=None,
        metadata={
            "name": "MetaCommandSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    command_container_set: Optional[CommandContainerSetType] = field(
        default=None,
        metadata={
            "name": "CommandContainerSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    stream_set: Optional[StreamSetType] = field(
        default=None,
        metadata={
            "name": "StreamSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    algorithm_set: Optional[AlgorithmSetType] = field(
        default=None,
        metadata={
            "name": "AlgorithmSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )


@dataclass
class SpaceSystemType(NameDescriptionType):
    """SpaceSystem is a collection of SpaceSystem(s) including space assets,
    ground assets, multi-satellite systems and sub-systems.

    A SpaceSystem is the root element for the set of data necessary to monitor and command an arbitrary space device - this includes the binary decomposition the data streams going into and out of a device.

    :ivar header: The Header element contains optional descriptive
        information about this SpaceSystem or the document as a whole
        when specified at the root SpaceSystem.
    :ivar telemetry_meta_data: This element contains descriptions of the
        telemetry created on the space asset/device and sent to other
        data consumers.
    :ivar command_meta_data: This element contains descriptions of the
        commands and their associated constraints and verifications that
        can be sent to the space asset/device.
    :ivar service_set:
    :ivar space_system: Additional SpaceSystem elements may be used like
        namespaces to segregate portions of the space asset/device into
        convenient groupings or may be used to specialize a product line
        generic SpaceSystem to a specific asset instance.
    :ivar operational_status: Optional descriptive attribute for
        document owner convenience.
    :ivar base:
    """

    header: Optional[HeaderType] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    telemetry_meta_data: Optional[TelemetryMetaDataType] = field(
        default=None,
        metadata={
            "name": "TelemetryMetaData",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    command_meta_data: Optional[CommandMetaDataType] = field(
        default=None,
        metadata={
            "name": "CommandMetaData",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    service_set: Optional[ServiceSetType] = field(
        default=None,
        metadata={
            "name": "ServiceSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
        },
    )
    space_system: List["SpaceSystem"] = field(
        default_factory=list,
        metadata={
            "name": "SpaceSystem",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/XTCE/20180204",
            "nillable": True,
        },
    )
    operational_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class SpaceSystem(SpaceSystemType):
    """The top-level SpaceSystem is the root element for the set of metadata
    necessary to monitor and command a space device, such as a satellite.

    A SpaceSystem defines a namespace.  Metadata areas include:
    packets/minor frames layout, telemetry, calibration, alarm,
    algorithms, streams and commands.  A SpaceSystem may have child
    SpaceSystems, forming a SpaceSystem tree. See SpaceSystemType.
    """

    class Meta:
        nillable = True
        namespace = "http://www.omg.org/spec/XTCE/20180204"
