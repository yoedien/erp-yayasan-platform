from enum import Enum


class PartnerType(str, Enum):

    SUPPLIER = "SUPPLIER"

    VENDOR = "VENDOR"

    BANK = "BANK"

    DONATUR = "DONATUR"

    LAINNYA = "LAINNYA"