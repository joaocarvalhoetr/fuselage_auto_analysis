import math

class node:
    def __init__(self, ID, x, y, z):
        self.x        = float(x)
        self.y        = float(y)
        self.z        = float(z)
        self.ID       = ID

class CQUAD4:
    def __init__(self, ID, property_ID, nodes, material_direction_angle):
        self.type                     = 'CQUAD4'
        self.ID                       = ID
        self.property_ID              = property_ID
        self.nodes                    = nodes
        self.material_direction_angle = material_direction_angle
        
class RBE2:
    def __init__(self,ID, independent_node, coupled_DOFs, dependent_nodes):
        self.type             = 'RBE2'
        self.ID               = ID
        self.independent_node = independent_node
        self.coupled_DOFs     = coupled_DOFs
        self.dependent_nodes  = dependent_nodes

class PCOMP:
    def __init__(self, ID, Z0, NSM, SB, FT, TREF, GE, LAM, MID, T, SOUT, NAME, fiber_angles):
        self.ID   = ID
        self.Z0   = Z0
        self.NSM  = NSM
        self.SB   = SB
        self.FT   = FT
        self.TREF = TREF
        self.GE   = GE
        self.LAM  = LAM
        self.MID  = MID
        self.T    = T
        self.SOUT = SOUT
        self.NAME = NAME
        self.fibers = fiber_angles

class PSHELL:
    def __init__(self, ID, MID, T, NAME):
        self.ID  = ID
        self.MID = MID
        self.T   = T
        self.NAME = NAME


