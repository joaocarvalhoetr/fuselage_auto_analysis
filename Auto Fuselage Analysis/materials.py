class orthotropic2d:
    def __init__(self, name, MID, E1, E2, NU12, G12, G1Z, G2Z, RHO, Xt, Xc, Yt, Yc,S,  A1=0.0, A2=0.0, TREF=0.0, GE='', F12='', STRN=''):
        self.name = name
        self.type = 'orthotropic2d'
        self.MID  = MID
        self.E1   = E1
        self.E2   = E2
        self.NU12 = NU12
        self.G12  = G12
        self.G1Z  = G1Z
        self.G2Z  = G2Z
        self.RHO  = RHO
        self.A1   = A1
        self.A2   = A2
        self.TREF = TREF
        self.Xt   = Xt
        self.Xc   = Xc
        self.Yt   = Yt
        self.Yc   = Yc
        self.S    = S
        self.GE   = GE
        self.F12  = F12
        self.STRN = STRN

class isotropic:
    def __init__(self, name, E, G, NU, RHO, MID):
        self.type = 'isotropic'
        self.E    = E
        self.G    = G
        self.NU   = NU
        self.RHO  = RHO
        self.MID  = MID
        self.name = name


