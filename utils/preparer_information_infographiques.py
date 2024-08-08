class ShiseidoElementsInfographiques:
    
    def __init__(self, shiseido_usa, shiseido_fr):
        self.shiseido_usa = shiseido_usa
        self.shiseido_fr = shiseido_fr
        self.shiseido_elements_usa = {}
        self.shiseido_elements_fr = {}
        self.shiseido_rep_age_usa = {}
        self.shiseido_rep_age_fr = {}
        
        
    def generer_elements_usa(self):
        shiseido_usa = self.shiseido_usa
        
        idx_avis_usa = shiseido_usa['nombre_avis'].idxmax()
        nom_produit_usa = shiseido_usa.loc[idx_avis_usa, 'nom_en']
        note_usa = shiseido_usa.loc[idx_avis_usa, 'note']
        nombre_avis_usa = shiseido_usa.loc[idx_avis_usa, 'nombre_avis']
        
        self.shiseido_elements_usa['info_usa'] = {
            'nom_produit_usa': str(nom_produit_usa),
            'note_usa': float(note_usa),
            'nombre_avis_usa': int(nombre_avis_usa)
        }
        
        
    def generer_elements_fr(self):
        shiseido_fr = self.shiseido_fr
        
        idx_avis_fr = shiseido_fr['nombre_avis'].idxmax()
        nom_produit_fr = shiseido_fr.loc[idx_avis_fr, 'nom_fr']
        note_fr = shiseido_fr.loc[idx_avis_fr, 'note']
        nombre_avis_fr = shiseido_fr.loc[idx_avis_fr, 'nombre_avis']
        
        self.shiseido_elements_fr['info_fr'] = {
            'nom_produit_fr': str(nom_produit_fr),
            'note_fr': float(note_fr),
            'nombre_avis_fr': int(nombre_avis_fr)
        }
        
        
    def calculer_repartition_avis_usa(self):
        shiseido_usa = self.shiseido_usa
        avis_total = shiseido_usa['nombre_avis'].sum()
        
        entre_18_et_24 = ((shiseido_usa['18_a_24'].sum()/avis_total) * 100).round(1)
        entre_25_et_34 = ((shiseido_usa['25_a_34'].sum()/avis_total) * 100).round(1)
        entre_35_et_44 = ((shiseido_usa['35_a_44'].sum()/avis_total) * 100).round(1)
        entre_45_et_54 = ((shiseido_usa['45_a_54'].sum()/avis_total) * 100).round(1)
        entre_55_et_64 = ((shiseido_usa['55_a_64'].sum()/avis_total) * 100).round(1)
        superieur_a_65 = ((shiseido_usa['superieur_a_65'].sum()/avis_total) * 100).round(1)
        sans_age =  ((shiseido_usa['sans_age'].sum()/avis_total) * 100).round(1)
        
        self.shiseido_rep_age_usa['pourcentage_repartition_avis'] = {
            "18-24": float(entre_18_et_24),
            "25-34": float(entre_25_et_34),
            "35-44": float(entre_35_et_44),
            "45-54": float(entre_45_et_54),
            "55-64": float(entre_55_et_64),
            ">65": float(superieur_a_65),
            "sans age": float(sans_age)
            
        }
               
                
    def calculer_repartition_avis_fr(self):
        shiseido_fr = self.shiseido_fr
        avis_total = shiseido_fr['nombre_avis'].sum()
        
        entre_18_et_24 = ((shiseido_fr['18_a_24'].sum()/avis_total) * 100).round(1)
        entre_25_et_34 = ((shiseido_fr['25_a_34'].sum()/avis_total) * 100).round(1)
        entre_35_et_44 = ((shiseido_fr['35_a_44'].sum()/avis_total) * 100).round(1)
        entre_45_et_54 = ((shiseido_fr['45_a_54'].sum()/avis_total) * 100).round(1)
        entre_55_et_64 = ((shiseido_fr['55_a_64'].sum()/avis_total) * 100).round(1)
        superieur_a_65 = ((shiseido_fr['superieur_a_65'].sum()/avis_total) * 100).round(1)
        sans_age =  ((shiseido_fr['sans_age'].sum()/avis_total) * 100).round(1)
        
        self.shiseido_rep_age_fr['pourcentage_repartition_avis'] = {
            "18-24": float(entre_18_et_24),
            "25-34": float(entre_25_et_34),
            "35-44": float(entre_35_et_44),
            "45-54": float(entre_45_et_54),
            "55-64": float(entre_55_et_64),
            ">65": float(superieur_a_65),
            "sans age": float(sans_age)
            
        }