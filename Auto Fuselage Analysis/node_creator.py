# CQUAD4         1       1       1       2      17      16.3862493
# CQUAD4        37       1      53      54      60      59    -90.
from elements import CQUAD4

def fuselage_CQUAD4_creator(node_base,elements_list,current_element_ID):
    for n_floor in range(len(node_base) - 1):
        for n_position in range(len(node_base[n_floor])):
    
            property_ID = 1
            material_direction_angle = 0.
            
            node_1 = node_base[n_floor][n_position - 1]
            node_2 = node_base[n_floor][n_position]
            node_3 = node_base[n_floor + 1][n_position]
            node_4 = node_base[n_floor + 1][n_position - 1]
            nodes  = [node_1,node_2,node_3,node_4]
            
            current_element_ID += 1
            elements_list.append(CQUAD4(current_element_ID, property_ID, nodes, material_direction_angle))

    return elements_list,current_element_ID


