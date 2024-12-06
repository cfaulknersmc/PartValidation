import re as __re
from collections import defaultdict as __defaultdict
from numpy import interp as __interp

itv1000_2000_3000 = __re.compile("""^ITV([1-3]0[135][01]-([0-3][1-4]|40|52|53|60|CC|DE|PR|RC|IL)[NTF]?[1-4][BC]?[SLN][2-5]?(-X(102|224|25|256|26))?|[12]0[135][01]-[0-3][1-4][NTF]?[1-3][BC]?[SLN][2-5]?-X88|[1-3]0[135][01]-[0-3][1-4][NTF]?[1-4][BC]?[SLN][2-5]?-X410|[1-3]0[135][01]-[0-3][23][NTF]?[1-4][BC]?[SLN][2-5]?-X420|10[135][01]-([0-3][1-4]|40)[NTF]?[12][BC]?[SLN][2-5]?-X10|20[135][01]-([0-3][1-4]|40)[NTF]?[23][BC]?[SLN][2-5]?-X10)""")
itv1100_2100_3100 = __re.compile("^ITV[1-3]1[135][01]-([0-3][1-5]|40)[NF]?[1-4][BC]?[SLN][2-5]?")
itv209 = __re.compile("^ITV209(0-(([0-3][1-4]|40|52|53|IL)[NTF]?2[BC]?[SLN]5|(CC|DE|PR|RC)[NTF]?2[BC]?[SLN]|50[NTF]?2[BC]?[SN]5)|1-([0-3][1-4]|40)[NTF]?2[BC]?[SLN]5)")
itv0000 = __re.compile("^ITV00[135][01]-[0-3]U?M?[BC]?[NSL]")
iitv0000 = __re.compile("^IITV00-(0[2-9]|10)U?-?") #Needs work itv 39/36/5
itv009 = __re.compile("^ITV009[01]-[0-3]U?M?[BC]?[NSL]")
itve_p = __re.compile("""^ITV(10[135]0-(SEN|SPN)-N?[12]-DUX02357|20[135]0-(SEN|SPN)-(N?[23]-DUX02357|2-DUX02357-X26)|2090-(SEN|SPN)-N?2-DUX02357|20[35]0-(SEN|SPN)-3-DUX02357-X400|30[135]0-(SEN|SPN)-N?[34]-DUX02357)""")

itvx2000 = __re.compile("^ITVX2030-[0-3][1-4][NF]?3[BC]?[SLN][2-4]?")

itvh2000 = __re.compile("^ITVH2020-([0-3][1-4]|40)[NF]?[23][BC]?[SLN][2-4]?")

izs = __re.compile("""^IZS4(0-(340|400|460|580|640|820|1120|1300|1600|1900|2320|2500)[CJKVS]?[ZN]?-(0[4-9]|1[01])B?(-X14)?|[12]-(340|400|460|580|640|820|1120|1300|1600|1900|2320|2500)[CJKVS]?P?[ZN]?-(0[4-9]|1[01])B?[FG]?(-X14)?|0-(520|700|760|880|940|1000|1060|1180|1240|1360|1420|1480|1540|1660|1720|1780|1840|1960|2020|2080|2140|2200|2260|2380|2440)[CJKVS]?[ZN]?-(0[4-9]|1[01])B?-X1[04]|[12]-(520|700|760|880|940|1000|1060|1180|1240|1360|1420|1480|1540|1660|1720|1780|1840|1960|2020|2080|2140|2200|2260|2380|2440)[CJKVS]?P?[ZN]?-(0[4-9]|1[01])B?[FG]?-X1[04])""")

izs_acc = __re.compile("^IZ(S(3(1-D[FG]|0-M2)|4([01]-CP(Z|([01][1-9]|[12]0)-X13)?|0-(N[TCJKVS]|B[EM]|E[3-5])|1(RC|C(G[12]|F((0[134679]|1[1-9]|[12]0)-X13|0[258])))))|F10-CG[12])")

izt_res = (r"(16|22|34|40|46|58|64|82|112|130|160|190|232|250)", r"[DELMVS][1-3]([4-9]|[AB])[HL][QR]?", r"3|5|10|15|N", r"[BF]?[UWY]?", r"(-X14)?",
           r"(28|52|70|76|88|94|100|106|118|124|136|142|148|154|166|172|178|184|196|202|208|214|220|226|238|244)", r"L-[NJKMSTZ][NEGHJKMPQRSTZ]")
izt = __re.compile(fr"^IZT4(0-{''.join(izt_res[:2])}-{''.join(izt_res[2:5])}|[12]-{''.join(izt_res[:2])}(P?-{izt_res[2]}|{izt_res[6]}){''.join(izt_res[3:5])}|0-{izt_res[5]}{izt_res[1]}-{''.join(izt_res[2:4])}-X10|[12]-{izt_res[5]}{izt_res[1]}(P?-{izt_res[2]}|{izt_res[6]}){izt_res[3]}-X10|3-[DL][1-3][67][HL](P?-{izt_res[2]}|{izt_res[6]}){izt_res[3]})")

izt_bcpn = __re.compile(fr"^IZT(B4[02]-({''.join(izt_res[:2])}(-[BF])?(-X14)?|{izt_res[5]}{izt_res[1]}(-[BF])?-X1[04])|C4(0-(3|5|10|15|N)(-W)?|1-(P?(3|5|10|15|N)|L[NJKMSTZ][NEGHJKMPQRSTZ])(-W)?)|P4([0-3]|[1-3]-L)(-Y)?|N43-[DL][1-3][67][HL](-F)?)")

izt_acc = __re.compile("^IZ(T4(0-(N[DELM]|B([EM][12]|[1-3])|C(P(3|5|10|15)|G[12]|F[1-3])|E[12])|1-C(P[JKMSTZ]|E[EGHJKMPQRSTZ])|3-(N[DL]|BL[12]|A00(1-[DL][67][HL]|2-[1-3])|M2))|S(30-(M2|A020[12])|40-(N[VS]|E[2-5])))")

izs_lengths = (340, 400, 460, 580, 640, 820, 1120, 1300, 1600, 1900, 2320, 2500)
izs_weights = ((590, 640, 690, 790, 830, 980, 1220, 1360, 1600, 1840, 2170, 2320), 
               (740, 790, 840, 940, 980, 1130, 1370, 1510, 1750, 1990, 2320, 2470),
               (860, 910, 960, 1060, 1100, 1250, 1490, 1630, 1870, 2110, 2440, 2590)) #40, 41, 42

izs_fittings = {
    "04": 13,
    "06": 13,
    "08": 15,
    "10": 22,
    "05": 15,
    "07": 14,
    "09": 15,
    "11": 23
}

izt_fittings = {
    "4H": 13,
    "6H": 13,
    "8H": 15,
    "AH": 22,
    "4L": 25,
    "6L": 27,
    "8L": 29,
    "AL": 37,
    "5H": 15,
    "7H": 14,
    "9H": 15,
    "BH": 23,
    "5L": 26,
    "7L": 27,
    "9L": 29,
    "BL": 36,
}

izt_controller_weights = ((210, 230), (210, 230), (210, 230), (210, 230))
izt_power_weights = ((680, 690), (680, 690), (1350, 1360), (680, 690))

izt_bar_lengths = (160, 220, 340, 400, 460, 580, 640, 820, 1120, 1300, 1600, 1900, 2320, 2500)
izt_bar_weights = (((360, 420, 530, 590, 650, 760, 820, 990, 1270, 1440, 1720, 2010, 2410, 2580), 
                    (490, 550, 660, 720, 780, 890, 950, 1120, 1400, 1570, 1850, 2140, 2540, 2710),
                    (610, 670, 780, 840, 900, 1010, 1070, 1240, 1520, 1690, 1970, 2260, 2660, 2830)),
                   ((360, 420, 530, 590, 650, 760, 820, 990, 1270, 1440, 1720, 2010, 2410, 2580), 
                    (490, 550, 660, 720, 780, 890, 950, 1120, 1400, 1570, 1850, 2140, 2540, 2710),
                    (610, 670, 780, 840, 900, 1010, 1070, 1240, 1520, 1690, 1970, 2260, 2660, 2830)),
                   ((520, 580, 690, 750, 810, 920, 980, 1150, 1430, 1600, 1880, 2170, 2570, 2740),
                    (770, 830, 940, 1000, 1060, 1170, 1230, 1400, 1680, 1850, 2130, 2420, 2820, 2990),
                    (1010, 1070, 1180, 1240, 1300, 1410, 1470, 1640, 1920, 2090, 2370, 2660, 3060, 3230)),
                    (200, 310, 440)) #40, 41, 42, 43 per voltage cable

izs_ys = (73, 94, 94)
izs_zs = (30, 44, 44)

itv0000_dimensions = (15, 59.7, 82)

itv1000_weights = (__defaultdict(lambda: 250, {"CC": 330, "DE": 320, "PR": 350, "RC": 320, "IL": 320}), 
                   __defaultdict(lambda: 350, {"CC": 430, "DE": 420, "PR": 450, "RC": 420, "IL": 420}), 
                   __defaultdict(lambda: 645, {"CC": 730, "DE": 720, "PR": 750, "RC": 720, "IL": 720}))

itv1000_dimensions = ((50, 50, __defaultdict(lambda: 82, {"52": 109, "53": 109, "60": 107, "CC": 119, "DE": 109, "PR": 119, "RC": 109, "IL": 109})), 
                      (50, 50, __defaultdict(lambda: 104, {"52": 131, "53": 131, "60": 129, "CC": 141, "DE": 131, "PR": 141, "RC": 131, "IL": 131})), 
                      (66, 66, __defaultdict(lambda: 125, {"52": 152, "53": 152, "60": 150, "CC": 162, "DE": 152, "PR": 162, "RC": 152, "IL": 152})))

itv1100_weights = (235, 285, 555)
itv1100_dimensions = ((50, 50, 82), (50, 50, 94), (66, 66, 115))

itvx2000_dimensions = (62, 52, 119)

itvh2000_dimensions = (62, 52, 122)

izt_ys = (99, 99, 153, 99)


descriptions = __defaultdict(lambda: "", {
    "IZS": "Bar Type Ionizer",
    "ITV1000": ("1000 Size Electro-Pneumatic Regulator", "2000 Size Electro-Pneumatic Regulator", "3000 Size Electro-Pneumatic Regulator"),
    "ITV1100": ("1100 Size High Flow Rate E/P Regulator", "2100 Size High Flow Rate E/P Regulator", "3100 Size High Flow Rate E/P Regulator"),
    "UPA": "Pressure Ctrl Unit",
    "ITVX2000": "High Pressure E/P Regulator",
    "ITVH2000": "3 MPa Max Supply Pressure High Pressure E/P Regulator",
    "IZT": ("Separate Controller Bar Type Ionizer", "Separate Controller Nozzle Type Ionizer") 
})

patterns_table = {
    "IZS": (__re.compile(r"4[0-2]"), __re.compile(r"\d{3,4}"), __re.compile(r"\d{2}")),
    "ITV1000": (__re.compile(r"[1-3]0[135]0"),),
    "ITV1100": (__re.compile(r"[1-3]1[135]0"),),
    "IZT": (__re.compile(r"4[0-3]"), __re.compile(izt_res[0][:-1] + r"|" + izt_res[5][1:]), __re.compile(r"([4-9]|[AB])[HL][QR]?"))
}

rohs = __defaultdict(lambda: None, {
    "ITV1000": (3,),
    "ITV1100": (3, 3, 3),
    "ITV209": 3,
    "ITVX2000": 3,
    "ITVH2000": 3,
    "IZS": 3,
    "IZT": 3
})

def izs_wframe(part_type, part_number_sections):
    patterns = patterns_table[part_type]
    model_type = __re.findall(patterns[0], part_number_sections[0])[0]
    L = float(__re.findall(patterns[1], part_number_sections[1])[0])
    diam = __re.findall(patterns[2], part_number_sections[2])[0]
    id = int(model_type[-1])
    x, y, z = L + 2*izs_fittings[diam], izs_ys[id], izs_zs[id]
    weight = __interp(L, izs_lengths, izs_weights[id])
    description = descriptions[part_type]
    return (x, y, z, weight, description)

def itv0000_wframe(part_type, part_number_sections):
    x, y, z = itv0000_dimensions
    weight = 100
    # return (x, y, z, weight, description)

def itv1000_wframe(part_type, part_number_sections):
    patterns = patterns_table[part_type]
    model_type = __re.findall(patterns[0], part_number_sections[0])[0]
    id = int(model_type[0]) - 1
    communication_mode = part_number_sections[1][:2]
    x, y, z = itv1000_dimensions[id][0], itv1000_dimensions[id][1], itv1000_dimensions[id][2][communication_mode]
    weight = itv1000_weights[id][communication_mode]
    description = descriptions[part_type][id]
    return (x, y, z, weight, description)

def itv1100_wframe(part_type, part_number_sections):
    patterns = patterns_table[part_type]
    model_type = __re.findall(patterns[0], part_number_sections[0])[0]
    id = int(model_type[0]) - 1
    x, y, z = itv1100_dimensions[id][0], itv1100_dimensions[id][1], itv1100_dimensions[id][2]
    weight = itv1000_weights[id]
    description = descriptions[part_type][id]
    return (x, y, z, weight, description)

def itvx2000_wframe(part_type, part_number_sections):
    x, y, z = itvx2000_dimensions
    weight = 570
    description = descriptions[part_type]
    return (x, y, z, weight, description)

def itvh2000_wframe(part_type, part_number_sections):
    x, y, z = itvh2000_dimensions
    weight = 630
    description = descriptions[part_type]
    return (x, y, z, weight, description)

def izt_wframe(part_type, part_number_sections):
    patterns = patterns_table[part_type]
    model_type = __re.findall(patterns[0], part_number_sections[0])[0]
    id = int(model_type[-1])
    y, z = izt_ys[id], 75
    io_link_blint = 0
    if not str.isnumeric(part_number_sections[1][-2]) and part_number_sections[1][-1] == 'L' and not (part_number_sections[1][-2] == 'A' or part_number_sections[1][-2] == 'B'):
        io_link_blint = 1
    for voltage_cable_index, voltage_cable in enumerate(part_number_sections[1]):
        if not str.isnumeric(voltage_cable): 
            break
    voltage_cable = int(part_number_sections[1][voltage_cable_index + 1]) - 1
    if id == 3:
        x = 378 + 14 #14 is extra for nozzle right that's not specified, so I just went with the B length
        weight = izt_bar_weights[id][voltage_cable] + izt_controller_weights[id][io_link_blint] + izt_power_weights[id][io_link_blint]
    else:
        bar_length = int(__re.findall(patterns[1], part_number_sections[1])[0])*10
        fitting_plug_pos = __re.findall(patterns[2], part_number_sections[1])[0]    
        fitting, plug_pos = fitting_plug_pos[:2], fitting_plug_pos[-1]
        if plug_pos == "R":
            left_end = 4.4
        else:
            left_end = izt_fittings[fitting]
        x = bar_length + 36 + left_end + 325
        weight = __interp(bar_length, izt_bar_lengths, izt_bar_weights[id][voltage_cable]) + izt_controller_weights[id][io_link_blint] + izt_power_weights[id][io_link_blint]
    description = descriptions[part_type][int(id == 3)]
    return (x, y, z, weight, description)

re_patterns = (
    (itv0000, "ITV00", None), 
    (itv009, "ITV009", None), 
    (itv1000_2000_3000, "ITV1000", itv1000_wframe), 
    (itv1100_2100_3100, "ITV1100", itv1100_wframe), 
    (itv209, "ITV209", None),
    (iitv0000, "IITV00", None), 
    (itve_p, "ITVE_P", None), 
    (itvx2000, "ITVX2000", itvx2000_wframe), 
    (itvh2000, "ITVH2000", itvh2000_wframe), 
    (izs, "IZS", izs_wframe), 
    (izs_acc, "IZS_ACC", None), 
    (izt, "IZT", izt_wframe),
    (izt_bcpn, "IZT_BCPN", None),
    (izt_acc, "IZT_ACC", None))
