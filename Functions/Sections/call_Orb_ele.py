

from Functions.Sections.CoOE import Calculate

ty = Calculate.ACOE(pos_vec, vel_vec, e_vec, inc)
def all_orb_ele(self,ty): 
        if ty == 4:
            keys = list(ty.keys())
            values = list(ty.values()) 
            self.ui.RAAN_CoOE_lbl.setText(keys[0])
            self.ui.RAAN_coe_n_aoe.setText(str(round(values[0] * (180/pi), 4)))
            self.ui.arg_of_per_CoOE_lbl.setText(keys[1])
            self.ui.arg_of_per_coe_n_aoe.setText(str(round(values[1] * (180/pi), 4)))
            self.ui.tru_ano_CoOE_lbl.setText(keys[2])
            self.ui.tru_ana_coe_n_aoe.setText(str(round(values[2] * (180/pi), 4))) 

        elif ty == 3:
            keys = list(ty.keys())
            values = list(ty.values())
            self.ui.RAAN_CoOE_lbl.setText(keys[0])
            self.ui.RAAN_coe_n_aoe.setText(str(round(values[0] * (180/pi), 4)))
            self.ui.arg_of_per_CoOE_lbl.setText(keys[1])
            self.ui.arg_of_per_coe_n_aoe.setText(str(round(values[1] * (180/pi), 4)))
            self.ui.tru_ano_CoOE_lbl.setHidden(1)
            self.ui.tru_ana_coe_n_aoe.setHidden(1)

        elif ty == 2:
            keys = list(ty.keys())
            values = list(ty.values())
            self.ui.RAAN_CoOE_lbl.setText(keys[0])
            self.ui.RAAN_coe_n_aoe.setText(str(round(values[0] * (180/pi), 4)))
            self.ui.arg_of_per_CoOE_lbl.setText(keys[1])
            self.ui.arg_of_per_coe_n_aoe.setText(str(round(values[1] * (180/pi), 4)))
            self.ui.tru_ano_CoOE_lbl.setHidden(1)
            self.ui.tru_ana_coe_n_aoe.setHidden(1)

        elif ty == 1:
            keys = list(ty.keys())
            values = list(ty.values())
            self.ui.RAAN_CoOE_lbl.setText(keys[0])
            self.ui.RAAN_coe_n_aoe.setText(str(round(values[0] * (180/pi), 4)))
            self.ui.arg_of_per_CoOE_lbl.setHidden(1)
            self.ui.arg_of_per_coe_n_aoe.setHidden(1)
            self.ui.tru_ano_CoOE_lbl.setHidden(1)
            self.ui.tru_ana_coe_n_aoe.setHidden(1)