def format_coord_field(coord_value):
    """
    Correctly formats a coordinate field based on its value

    """
    size = 8
    coord = ""
    #Add the minus signal if the number is negative
    #if coord_value == 0:
    #    coord += '.' + ' '*(size-1)
    #    return coord
    
    if coord_value < 0:
        coord += "-"
        size  -= 1
        coord_value = coord_value * -1  ## Modulus of the number
    

    # Guarantee that the integer isn't already bigger than what is needed
    char = str(coord_value)

    # check if we are speaking about a decimal number not bigger than 1.
    if (coord_value ** 2) < 1:
        coord += "."
        size -= 1
        splitted = char.split(".")
        if len(splitted[1]) > size:
            splitted[1] = splitted[1][:(size - 1)]

        size = size - len(splitted[1])
        coord += str(splitted[1]).ljust(size + len(splitted[1]), '0')
    else:
        if len(char) > size:
            char = char[:(size - 1)]
        size = size - len(char)
        coord += char.ljust(size + len(char), '0')
    return coord


def write_GRID(point,f):
    line = ''
    #{point.id}       0
    ## FORMATAÇÃO NECESSÁRIA É A SEGUINTE:
    ## GRID           1       0.0270903.1655057.0791552       0
    ## GRID  (11WS)|NODE ID|(7WS)|0|8 CHAR X .|8 CHAR Y.|8 CHAR Z.|(7WS)|0
    ##FORMATAÇÃO DE COORDENADA
    
    blank2 = ' ' * (8 - len(str(point.ID)))
    
    field1   = "GRID    "
    field2   = blank2 + str(point.ID)
    field3   = "       0" #coordinate_system_ID
    field4   = format_coord_field(point.x)
    field5   = format_coord_field(point.y)
    field6   = format_coord_field(point.z)
    field7   = "       0"
    line_end = "\n"
    
    line = field1 + field2 + field3 + field4 + field5 + field6 + field7 + line_end

    f.write(line)

def write_CQUAD4(element,f):

    node_1 = element.nodes[0]
    node_2 = element.nodes[1]
    node_3 = element.nodes[2]
    node_4 = element.nodes[3]

    blank_1 = ' ' * (8 - len(element.type))
    blank_2 = ' ' * (8 - len(str(element.ID)))
    blank_3 = ' ' * (8 - len(str(element.property_ID)))
    blank_4 = ' ' * (8 - len(str(node_1)))
    blank_5 = ' ' * (8 - len(str(node_2)))
    blank_6 = ' ' * (8 - len(str(node_3)))
    blank_7 = ' ' * (8 - len(str(node_4)))
    blank_8 = ' ' * (8 - len(str(element.material_direction_angle)))

    field1 = element.type + blank_1
    field2 = blank_2 + str(element.ID)
    field3 = blank_3 + str(element.property_ID)
    field4 = blank_4 + str(node_1)
    field5 = blank_5 + str(node_2)
    field6 = blank_6 + str(node_3)
    field7 = blank_7 + str(node_4)
    field8 = blank_8 + str(element.material_direction_angle)

    line = field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + '\n'

    f.write(line)
    
def write_RBE2(element, f):
    #RBE2(self,ID, independent_node, coupled_DOFs, dependent_nodes
    # EID - Element identification number.(Integer > 0)
    # GN  - Identification number of grid point to which all six independent degrees - of - freedom for the element are assigned.(Integer > 0)
    # CM  - Component numbers of the dependent degrees - of - freedom in the global coordinate system at grid points GMi.(Integers 1 through 6 with no embedded blanks.)
    # GMi - Grid point identification numbers at which dependent degrees - of - freedom are assigned .(Integer > 0)
    # ALPHA -Thermal expansion coefficient (Real; Default = 0.0)
    # RBE2    |    8218|    8301|  123456|       1|       2|       3       4       5+
    # +              6       7       8       9      10      11      12      13+
    # +             14      15      16      17      18      19      20      21+
    # +             22      23      24      25      26      27      28      29+
    # +             30      31      32      33      34      35      36      37+
    # +             38      39      40      41      42      43      44      45+
    # +             46      47      48      49      50      51      52      53+
    # +             54      55      56      57      58      59      60      61+
    # +             62      63      64      65      66      67      68      69+
    # +             70      71      72      73      74      75      76      77+
    # +             78      79      80      81      82      83

    EID = element.ID
    GN  = element.independent_node
    CM  = element.coupled_DOFs
    dependent_nodes = element.dependent_nodes
    
    blank2 = ' ' * (8 - len(str(EID)))
    blank3 = ' ' * (8 - len(str(GN)))
    blank4 = ' ' * (8 - len(str(CM)))

    field1 = 'RBE2    '  # 8 SPACES
    field2 = blank2 + str(EID)
    field3 = blank3 + str(GN)
    field4 = blank4 + str(CM)

    line = field1 + field2 + field3 + field4

    first_line = True
    nodes_added = 0 # Count of the number of the elements added to the RBE

    nodes_inserted = 0 # Local count of the elements added to a line.
    max_nodes = 5

    for node_ID in dependent_nodes:
        if nodes_added == 5:
            first_line = False

        if nodes_inserted != max_nodes:
            blank = ' ' * (8 - len(str(node_ID)))
            field = blank + str(node_ID)
            line += field
            nodes_inserted += 1
            nodes_added += 1

        else:
            nodes_inserted = 0
            field = '+\n' + '+       '
            line += field
            blank = ' ' * (8 - len(str(node_ID)))
            field = blank + str(node_ID)
            line += field
            nodes_inserted += 1
            nodes_added += 1

            if first_line:
                max_nodes = 5
            else:
                max_nodes = 8

    f.write(line + '\n')
