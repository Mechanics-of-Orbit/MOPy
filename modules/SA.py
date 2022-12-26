R1 = 149.6e6
R2 = 227.9e6
Vdv = 32.7279
Major_Body = 'Sun'
R1_bod = 'Earth'

Vi = 2.94346
Rp = 6678

class SA(Major_Body,R1_bod):
    def __init__(self):
        G = 6.67e-20
        mu_Major_Body = G * self.R1_bod * 1
        mu_R1 = G * self.R2_bod * 1

    def SA(self, R1, R2):
        a = 2/(1-(R1*Vdv**2)/(2*self.mu_Major_Body))
        coeff_del_Rp_Rp = a * (self.mu_R1/(Vdv*Vi*Rp))
        coeff_del_Vp_Vp = a * ((Vi+(2*self.mu_R1/(Rp*Vi)))/Vdv)
        del_R2_R2 = coeff_del_Rp_Rp*(del_Rp_Rp) + coeff_del_Vp_Vp * (del_Vp_Vp)
        return [del_R2_R2]




del_Rp_Rp = 0#0.01
del_Vp_Vp = 1
