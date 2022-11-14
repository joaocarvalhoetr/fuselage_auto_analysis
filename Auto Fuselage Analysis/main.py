import math
import write
import os
from node_creator import fuselage_CQUAD4_creator
from elements import node, CQUAD4, RBE2, PCOMP, PSHELL
from materials import orthotropic2d, isotropic
from model_tools import SPC1, FORCE, write_MAT8, write_PCOMP, write_PSHELL, write_MAT1
        
# INPUTS --------------------------------------------------------------------------
# Parametros de dados de fuselagem
diameter = 0.133
height = 0.5
output_name = input("File output name: ")

# Constraint Degrees
constrained_DOFs_RBE2_bottom=123456

# Loads Applied

f_x = 10.
f_y = 20.
f_z = -5.


# User selection of what material will be used
selected = False
while not selected:
    choice = (input("I for isotropic, O for orthotropic\n")).lower()
    if choice == 'i':
        material_mode = 'isotropic'
        selected = True
    elif choice == 'o':
        material_mode = 'orthotropic2d'
        selected = True
    else:
        print("Unknown input.")

#Material
#Isotropic

if material_mode == 'isotropic':
    NAME = "PLATE - ISOTROPIC"
    E   = 70e9 #Pa
    G   = 7e10
    NU  = 0.3  #[-]
    RHO = 2700 #kg/m^3
    ID    = 1
    MID   = 1
    T     = 0.0005

#Composite

if material_mode == 'orthotropic2d':
    NAME = "LAMINATE - ANALYSIS"
    E1   =  1.2785e11 #Pa
    E2   =  9.86e9 #Pa
    NU12 =  0.28 #[-]
    G12  =  4.65e9 #Pa
    G1Z  =  4.65e9 #Pa
    G2Z  =  3.44e9 #Pa
    RHO  =  2700. #kg/m^3
    Xt   =  2.86e10 #Pa
    Xc   =  1.45e9 #Pa
    Yt   =  2.86e10 #Pa
    Yc   =  1.45e9 #Pa
    S    =  136e6 #Pa




    fiber_angles = [0, 45, 90, -90, -45]
    ID    = 1
    Z0    = 0.0005
    NSM   = 0
    SB    = 1
    FT    = "TSAI"
    TREF  = 0
    GE    = 0
    LAM   = 0
    MID   = 1
    T     = 0.5
    SOUT  = "YES"



#-----------------------------------------------------------------------------

# Initialize mesh data
nodes_list         = []
elements_list      = []
materials_list     = []
properties_list    = []
layup_list    = []
current_node_ID    = 0
current_element_ID = 0
current_material_ID = 0


#Create materials
if material_mode=='isotropic':
    name = 'Isotropic'
    current_material_ID += 1
    materials_list.append(isotropic(name, E, G, NU, RHO, MID))

elif material_mode=='orthotropic2d':
    name='ply_material'
    current_material_ID += 1
    materials_list.append(orthotropic2d(name, current_material_ID, E1, E2, NU12, G12, G1Z, G2Z, RHO, Xt, Xc, Yt, Yc, S))


# Create the fuselage using CQUAD4 elements -----------------------------------
radius = diameter / 2
perimeter = 2 * 3.14 * radius


# mesh sizes
node_size_base = 0.005
node_size_height = 0.005

# get correct sizes
num_nodes_layer = int(perimeter / node_size_base)  # Numero de pontos em cada camada
num_nodes_height = int(height / node_size_height)  # Numero de pontos em cada camada
node_size_base_correct = perimeter / num_nodes_layer
node_size_height_correct = height / (num_nodes_height - 1)
angle = node_size_base_correct * 2 * 3.14 / perimeter


# Numero de "camadas" que a malha vai ter
n_floors = num_nodes_height
n_positions = num_nodes_layer


# Criar os nós por andar e dar append à lista de node_base - Uso de objetos para calcular as coordenadas
node_base = []  # Lista onde serão guardadas novas listas com os diversos "andares da malha"
for i_floors in range(n_floors):
    node_floor = []
    theta = 0
    pos   = 0
    for i_positions in range(int(n_positions)):
        pos += 1
        current_node_ID += 1
        coord_x        = radius * math.cos(theta)
        coord_y        = radius * math.sin(theta)
        coord_z        = float(i_floors * node_size_height_correct)
        #z + 1, i + 1,
        node_floor.append(current_node_ID)
        nodes_list.append(node(current_node_ID, coord_x, coord_y, coord_z))
        theta += angle
    node_base.append(node_floor)

elements_list,current_element_ID = fuselage_CQUAD4_creator(node_base,elements_list,current_element_ID)
#------------------------------------------------------------------------------

#Create RBE2 elements at both ends of the fuselage-----------------------------
# Creation of independent nodes for RBE2
# -Base
current_node_ID += 1
nodes_list.append(node(current_node_ID,0, 0, 0))
RBE2_center_node_ID_base=current_node_ID

# - Top
current_node_ID += 1
nodes_list.append(node(current_node_ID, 0, 0, height))
RBE2_center_node_ID_top=current_node_ID

current_element_ID += 1
coupled_DOFs = 123456
bottom_list = node_base[0]
elements_list.append(RBE2(current_element_ID, RBE2_center_node_ID_base, coupled_DOFs, bottom_list))

current_element_ID += 1
coupled_DOFs = 123456
top_list = node_base[n_floors-1]
elements_list.append(RBE2(current_element_ID, RBE2_center_node_ID_top, coupled_DOFs, top_list))
#------------------------------------------------------------------------------
# PCOMP CREATOR
if material_mode == "orthotropic2d":
    layup_list.append(PCOMP(ID, Z0, NSM, SB, FT, TREF, GE, LAM, MID, T, SOUT, NAME,fiber_angles))
# ------------------------------------------------------------------------------
# PSHELL CREATOR
if material_mode == "isotropic":
    layup_list.append(PSHELL(ID, MID, T, NAME))

#------------------------------------------------------------------------------
# Print data to individual files ----------------------------------------------
# Nodes
f = open("grid.txt", "w")
for node_obj in nodes_list:
    write.write_GRID(node_obj,f)
f.close()

# Elements
f = open("elements.txt", "w")
for element in elements_list:
    if element.type == 'CQUAD4':
        write.write_CQUAD4(element,f)
    elif element.type == 'RBE2':
        write.write_RBE2(element,f)
    else:
        raise ValueError('Unknown element')
f.write("ENDDATA 18d0fdda")
f.close()

#------------------------------------------------------------------------------
# Constrained SET


# $ Femap with NX Nastran Constraint Set 1 : constraintset
# SPC1           1  123456    8301
f = open("constraint.txt", "w")

constraint_set_name = "constraintset"

constrained_nodes = [[RBE2_center_node_ID_base,constrained_DOFs_RBE2_bottom]]

f.write(f"$ Femap with NX Nastran Constraint Set 1 : {constraint_set_name}\n")
for i in range(len(constrained_nodes)):
    constrained_node=constrained_nodes[i][0]
    constrained_DOFs=constrained_nodes[i][1]
    SPC1(i + 1, constrained_DOFs, constrained_node, f)

f.close()

#------------------------------------------------------------------------------
# Write Load SET

f = open("load.txt", "w")

load_set_name = "loadset"

loads = [[RBE2_center_node_ID_top, f_x, f_y, f_z]]

f.write(f"$ Femap with NX Nastran Load Set 1 : {load_set_name}\n")
for i in range(len(loads)):
    load_node = loads[i][0]
    load_f_x   = loads[i][1]
    load_f_y   = loads[i][2]
    load_f_z   = loads[i][3]
    CID = 0
    scale_factor = 1.

    FORCE(i + 1, load_node, CID, scale_factor, load_f_x, load_f_y, load_f_z, f)

f.close()
#------------------------------------------------------------------------------
# Write PCOMP
if material_mode == "orthotropic2d":
    f = open("properties.txt", "w")

    for layup in layup_list:
        write_PCOMP(layup, f)
    # ID, Z0, NSM, SB, FT, TREF, GE, LAM, MID, T, SOUT, NAME, fiber_angles

    f.close()
#------------------------------------------------------------------------------
# Write PSHELL
if material_mode == "isotropic":
    f = open("properties.txt", "w")

    for layup in layup_list:
        write_PSHELL(layup, f)

    f.close()


#------------------------------------------------------------------------------
# Create Materials

f = open("materials.txt", "w")
for mat_obj in materials_list:
    if mat_obj.type=='orthotropic2d':
        write_MAT8(mat_obj, f)
    if mat_obj.type=='isotropic':
        write_MAT1(mat_obj, f)
f.close()
#------------------------------------------------------------------------------

# Write from .txt files to .bdf file ------------------------------------------
with open("heading.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "w") as f1:
        f1.writelines(lines)

with open("load.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "a") as f1:
        f1.writelines(lines)

with open("constraint.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "a") as f1:
        f1.writelines(lines)

with open("properties.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "a") as f1:
        f1.writelines(lines)

with open("materials.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "a") as f1:
        f1.writelines(lines)

with open("grid.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "a") as f1:
        f1.writelines(lines)

with open("elements.txt") as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(f"{output_name}.bdf", "a") as f1:
        f1.writelines(lines)

#------------------------------------------------------------------------------
os.remove("constraint.txt")
os.remove("elements.txt")
os.remove("grid.txt")
os.remove("load.txt")
os.remove("materials.txt")
os.remove("properties.txt")