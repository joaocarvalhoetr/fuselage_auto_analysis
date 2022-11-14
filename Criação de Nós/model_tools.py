# SPC1 Creator
# constraint_node = [id1, id2, id3, id4]

def SPC1(spc1_ID, constrained_DOFs, constraint_node, f):
    blank2 = ' ' * (8 - len(str(spc1_ID)))
    blank3 = ' ' * (8 - len(str(constrained_DOFs)))
    blank4 = ' ' * (8 - len(str(constraint_node)))

    field1 = "SPC1    "
    field2 = blank2 + str(spc1_ID)
    field3 = blank3 + str(constrained_DOFs)
    field4 = blank4 + str(constraint_node)
    line_end = "\n"

    line = field1 + field2 + field3 + field4 + line_end

    f.write(line)

    "SPC1           1  123456    8301"

def FORCE(force_ID, node, cid, scale_factor, force_x, force_y, force_z, f):
    blank2 = ' ' * (8 - len(str(force_ID)))
    blank3 = ' ' * (8 - len(str(node)))
    blank4 = ' ' * (8 - len(str(cid)))
    blank5 = ' ' * (8 - len(str(scale_factor)))
    blank6 = ' ' * (8 - len(str(force_x)))
    blank7 = ' ' * (8 - len(str(force_y)))
    blank8 = ' ' * (8 - len(str(force_z)))

    field1 = "FORCE   "
    field2 = blank2 + str(force_ID)
    field3 = blank3 + str(node)
    field4 = blank4 + str(cid)
    field5 = blank5 + str(scale_factor)
    field6 = blank6 + str(force_x)
    field7 = blank7 + str(force_y)
    field8 = blank8 + str(force_z)
    line_end = "\n"

    line = field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + line_end

    f.write(line)

def format_constant_field(value):
    scientific_notation = "{:e}".format(value)
    splitted = scientific_notation.split("e")
    rounded = round(float(splitted[0]), 3)
    string = str(rounded) + f"{splitted[1]}"
    return string

def write_MAT8(material, f):
    blank2 = ' ' * (8 - len(str(material.MID)))
    blank3 = ' ' * (8 - len(str(format_constant_field(material.E1))))
    blank4 = ' ' * (8 - len(str(format_constant_field(material.E2))))
    blank5 = ' ' * (8 - len(str(material.NU12)))
    blank6 = ' ' * (8 - len(str(format_constant_field(material.G12))))
    blank7 = ' ' * (8 - len(str(format_constant_field(material.G1Z))))
    blank8 = ' ' * (8 - len(str(format_constant_field(material.G2Z))))
    blank9 = ' ' * (8 - len(str(material.RHO)))
    blank10 = ' ' * (8 - len(str(material.A1)))
    blank11 = ' ' * (8 - len(str(material.A2)))
    blank12 = ' ' * (8 - len(str(material.TREF)))
    blank13 = ' ' * (8 - len(str(format_constant_field(material.Xt))))
    blank14 = ' ' * (8 - len(str(format_constant_field(material.Xc))))
    blank15 = ' ' * (8 - len(str(format_constant_field(material.Yt))))
    blank16 = ' ' * (8 - len(str(format_constant_field(material.Yc))))
    blank17 = ' ' * (8 - len(str(format_constant_field(material.S))))
    blank18 = ' ' * (8 - len(str(material.GE)))
    blank19 = ' ' * (8 - len(str(material.F12)))
    blank20 = ' ' * (8 - len(str(material.STRN)))

    field1  = "MAT8    "
    field2  = blank2 + str(material.MID)
    field3  = blank3 + str(format_constant_field(material.E1))
    field4  = blank4 + str(format_constant_field(material.E2))
    field5  = blank5 + str(material.NU12)
    field6  = blank6 + str(format_constant_field(material.G12))
    field7  = blank7 + str(format_constant_field(material.G1Z))
    field8  = blank8 + str(format_constant_field(material.G2Z))
    field9  = blank9 + str(material.RHO)
    field10 = blank10 + str(material.A1)
    field11 = blank11 + str(material.A2)
    field12 = blank12 + str(material.TREF)
    field13 = blank13 + str(format_constant_field(material.Xt))
    field14 = blank14 + str(format_constant_field(material.Xc))
    field15 = blank15 + str(format_constant_field(material.Yt))
    field16 = blank16 + str(format_constant_field(material.Yc))
    field17 = blank17 + str(format_constant_field(material.S))
    field18 = blank18 + str(material.GE)
    field19 = blank19 + str(material.F12)
    field20 = blank20 + str(material.STRN)

    line_cont_start='+       '
    line_cont_end = '+\n'
    line_end = "\n"

    line0 = f"$ Femap with NX Nastran Material 1 : {material.name}" + line_end
    line1 = field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + field9 + line_cont_end
    line2 = line_cont_start + field10 + field11 + field12 + field13 + field14 + field15 + field16 + field17 + line_cont_end
    line3 = line_cont_start + field18 + field19 + field20 + line_end

    f.write(line0 + line1 + line2 + line3)

def write_MAT1(material, f):

    blank2 = ' ' * (8 - len(str(material.MID)))
    blank3 = ' ' * (8 - len(str(format_constant_field(material.E))))
    blank4 = ' ' * (8 - len(str(format_constant_field(material.G))))
    blank5 = ' ' * (8 - len(str(format_constant_field(material.NU))))
    blank6 = ' ' * (8 - len(str(format_constant_field(material.RHO))))
    blank7 = ' ' * 8
    blank8 = ' ' * 8
    blank9 = ' ' * 8


    field1 = "MAT1    "
    field2 = blank2 + str(material.MID)
    field3 = blank3 + str(format_constant_field(material.E))
    field4 = blank4 + str(format_constant_field(material.G))
    field5 = blank5 + str(format_constant_field(material.NU))
    field6 = blank6 + str(format_constant_field(material.RHO))
    field7 = blank7
    field8 = blank8
    field9 = blank9

    line_cont_start = '+       '
    line_cont_end = '+\n'
    line_end = "\n"

    line0 = f"$ Femap with NX Nastran Material 1 : {material.name}" + line_end
    line1 = field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + field9 + line_end

    f.write(line0 + line1)

def write_PCOMP(PCOMP, f):
    fiber_angles = PCOMP.fibers

    f.write(f"$ Femap with NX Nastran Property 1 : {PCOMP.NAME}\n")

    line = ""

    blank2 = ' ' * (8 - len(str(PCOMP.ID)))
    blank3 = ' ' * (8 - len(str(PCOMP.Z0)))
    blank4 = ' ' * (8 - len(str(PCOMP.NSM)))
    blank5 = ' ' * (8 - len(str(PCOMP.SB)))
    blank6 = ' ' * (8 - len(str(PCOMP.FT)))
    blank7 = ' ' * (8 - len(str(PCOMP.TREF)))
    blank8 = ' ' * (8 - len(str(PCOMP.GE)))
    blank9 = ' ' * (8 - len(str(PCOMP.LAM)))

    blankmid = ' ' * (8 - len(str(PCOMP.MID)))
    blankt = ' ' * (8 - len(str(PCOMP.T)))
    blanksout = ' ' * (8 - len(str(PCOMP.SOUT)))
    fieldmid = blankmid + str(PCOMP.MID)
    fieldt = blankt + str(PCOMP.T)
    fieldsout = blanksout + str(PCOMP.SOUT)

    field1 = "PCOMP   "
    field2 = blank2 + str(PCOMP.ID)
    field3 = blank3 + str(PCOMP.Z0)
    field4 = blank4 + str(PCOMP.NSM)
    field5 = blank5 + str(PCOMP.SB)
    field6 = blank6 + str(PCOMP.FT)
    field7 = blank7 + str(PCOMP.TREF)
    field8 = blank8 + str(PCOMP.GE)
    field9 = blank9 + str(PCOMP.LAM)

    line_cont_start = '+       '
    line_cont_end = '+\n'
    line_end = "\n"


    line += field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + field9 + line_cont_end + line_cont_start

    line_count = 0

    for theta in fiber_angles:

        if line_count % 2 == 0 and line_count != 0:
            line_count = 0
            line += line_cont_end + line_cont_start
        line_count += 1
        blank_theta = ' ' * (8 - len(str(theta)))
        fieldtheta = blank_theta + str(theta)


        line += fieldmid + fieldt + fieldtheta + fieldsout

    f.write(line + line_end)

def write_PSHELL(PSHELL, f):
    NSM = '0.'

    blank2 = ' ' * (8 - len(str(PSHELL.ID)))
    blank3 = ' ' * (8 - len(str(PSHELL.MID)))
    blank4 = ' ' * (8 - len(str(format_constant_field(PSHELL.T))))
    blank5 = ' ' * (8 - len(str(PSHELL.MID)))
    blank6 = ' ' * 8
    blank7 = ' ' * (8 - len(str(PSHELL.MID)))
    blank8 = ' ' * 8
    blank9 = ' ' * (8 - len(str(NSM)))


    field1 = "PSHELL  "
    field2 = blank2 + str(PSHELL.ID)
    field3 = blank3 + str(PSHELL.MID)
    field4 = blank4 + str(format_constant_field(PSHELL.T))
    field5 = blank5 + str(PSHELL.MID)
    field6 = blank6
    field7 = blank7 + str(PSHELL.MID)
    field8 = blank8
    field9 = blank9 + str(NSM)

    line_end = "\n"

    line1 = f"$ Femap with NX Nastran Property 1 : {PSHELL.NAME}\n"
    line2 = field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + field9 + line_end

    f.write(line1 + line2)
