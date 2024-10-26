from enum import Enum

DOMAIN = "elkbledom"
CONF_RESET = "reset"
CONF_DELAY = "delay"

class EFFECTS (Enum):
    effect1 = 0x01
    effect2 = 0x02
    effect3 = 0x03
    effect4 = 0x04
    effect5 = 0x05
    effect6 = 0x06
    effect7 = 0x07
    effect8 = 0x08
    effect9 = 0x09
    effect10 = 0x0A
    effect11 = 0x0B
    effect12 = 0x0C
    effect13 = 0x0D
    effect14 = 0x0e
    effect15 = 0x0F
    effect16 = 0x10
    effect17 = 0x11
    effect18 = 0x12
    effect19 = 0x13
    effect20 = 0x14
    effect21 = 0x15
    effect22 = 0x16
    effect23 = 0x17
    effect24 = 0x18
    effect25 = 0x19
    effect26 = 0x1A
    effect27 = 0x1B
    effect28 = 0x1C
    effect29 = 0x1D
    effect30 = 0x1E
    effect31 = 0x1F
    effect32 = 0x20
    effect33 = 0x21
    effect34 = 0x22
    effect35 = 0x23
    effect36 = 0x24
    effect37 = 0x25
    effect38 = 0x26
    effect39 = 0x27
    effect40 = 0x28
    effect41 = 0x29
    effect42 = 0x2A
    effect43 = 0x2B
    effect44 = 0x2C
    effect45 = 0x2D
    effect46 = 0x2e
    effect47 = 0x2F
    effect48 = 0x30
    effect49 = 0x31
    effect50 = 0x32
    effect51 = 0x33
    effect52 = 0x34
    effect53 = 0x35
    effect54 = 0x36
    effect55 = 0x37
    effect56 = 0x38
    effect57 = 0x39
    effect58 = 0x3A
    effect59 = 0x3B
    effect60 = 0x3C
    effect61 = 0x3D
    effect62 = 0x3E
    effect63 = 0x3F
    effect64 = 0x40
    effect65 = 0x41
    effect66 = 0x42
    effect67 = 0x43
    effect68 = 0x44
    effect69 = 0x45
    effect70 = 0x46
    effect71 = 0x47
    effect72 = 0x48
    effect73 = 0x49
    effect74 = 0x4A
    effect75 = 0x4B
    effect76 = 0x4C
    effect77 = 0x4D
    effect78 = 0x4E
    effect79 = 0x4F
    effect80 = 0x50
    effect81 = 0x51
    effect82 = 0x52
    effect83 = 0x53
    effect84 = 0x54
    effect85 = 0x55
    effect86 = 0x56
    effect87 = 0x57
    effect88 = 0x58
    effect89 = 0x59
    effect90 = 0x5A
    effect91 = 0x5B
    effect92 = 0x5C
    effect93 = 0x5D
    effect94 = 0x5E
    effect95 = 0x5F
    effect96 = 0x60
    effect97 = 0x61
    effect98 = 0x62
    effect99 = 0x63
    effect100 = 0x64
    effect101 = 0x65
    effect102 = 0x66
    effect103 = 0x67
    effect104 = 0x68
    effect105 = 0x69
    effect106 = 0x6A
    effect107 = 0x6B
    effect108 = 0x6C
    effect109 = 0x6D
    effect110 = 0x6E
    effect111 = 0x6F
    effect112 = 0x70
    effect113 = 0x71
    effect114 = 0x72
    effect115 = 0x73
    effect116 = 0xFF

EFFECTS_list = ['effect1','effect2','effect3','effect4','effect5','effect6','effect7','effect8','effect9','effect10','effect11','effect12','effect13','effect14','effect15','effect16','effect17','effect18','effect19','effect20','effect21','effect22','effect23','effect24','effect25','effect26','effect27','effect28','effect29','effect30','effect31','effect32','effect33','effect34','effect35','effect36','effect37','effect38','effect39','effect40','effect41','effect42','effect43','effect44','effect45','effect46','effect47','effect48','effect49','effect50','effect51','effect52','effect53','effect54','effect55','effect56','effect57','effect58','effect59','effect60','effect61','effect62','effect63','effect64','effect65','effect66','effect67','effect68','effect69','effect70','effect71','effect72','effect73','effect74','effect75','effect76','effect77','effect78','effect79','effect80','effect81','effect82','effect83','effect84','effect85','effect86','effect87','effect88','effect89','effect90','effect91','effect92','effect93','effect94','effect95','effect96','effect97','effect98','effect99','effect100','effect101','effect102','effect103','effect104','effect105','effect106','effect107','effect108','effect109','effect110','effect111','effect112','effect113','effect114','effect115','effect116']

class WEEK_DAYS (Enum):
    monday = 0x01
    tuesday = 0x02
    wednesday = 0x04
    thursday = 0x08
    friday = 0x10
    saturday = 0x20
    sunday = 0x40
    all = (0x01 + 0x02 + 0x04 + 0x08 + 0x10 + 0x20 + 0x40)
    week_days = (0x01 + 0x02 + 0x04 + 0x08 + 0x10)
    weekend_days = (0x20 + 0x40)
    none = 0x00

#print(EFFECTS.blink_red.value)
