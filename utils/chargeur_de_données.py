import pandas as pd

class ShiseidoChargeurDonnees:
    
    def __init__(self, fichier1, fichier2, fichier3, fichier4):
        self.fichier1 = fichier1
        self.fichier2 = fichier2
        self.fichier3 = fichier3
        self.fichier4 = fichier4
        self.shiseido_usa = None
        self.shiseido_fr = None
        
    
    def ecrire_dataframes(self):
        self.df_shiseido_usa = pd.read_csv(self.fichier1)
        self.df_shiseido_fr = pd.read_csv(self.fichier2)
        self.df_shiseido_usa_rep_age = pd.read_csv(self.fichier3)
        self.df_shiseido_fr_rep_age = pd.read_csv(self.fichier4)
        
    
    def combiner_dataframes_usa(self):
        self.shiseido_usa = pd.merge(self.df_shiseido_usa, self.df_shiseido_usa_rep_age, on='nom_en')
    
    
    def combiner_dataframes_fr(self):
        self.shiseido_fr = pd.merge(self.df_shiseido_fr, self.df_shiseido_fr_rep_age, on='nom_fr')
    
    
    def calculer_avis_sans_age_usa(self):
        shiseido_usa = self.shiseido_usa
        nouvelle_col = ['sans_age']
        shiseido_usa = pd.concat([shiseido_usa, pd.DataFrame(columns = nouvelle_col)])
        shiseido_usa['sans_age'] = shiseido_usa['nombre_avis'] - shiseido_usa.iloc[:,6:13].sum(axis=1)
        shiseido_usa = shiseido_usa.astype({
            "nombre_avis": 'int', 
            "18_a_24": 'int',
            "25_a_34": 'int',
            "35_a_44": 'int',
            "45_a_54": 'int',
            "55_a_64": 'int',
            "superieur_a_65": 'int',
            "sans_age": 'int',
            })
        self.shiseido_usa = shiseido_usa

    def calculer_avis_sans_age_fr(self):
            shiseido_fr = self.shiseido_fr
            nouvelle_col = ['sans_age']
            shiseido_fr = pd.concat([shiseido_fr, pd.DataFrame(columns = nouvelle_col)])
            shiseido_fr['sans_age'] = shiseido_fr['nombre_avis'] - shiseido_fr.iloc[:,6:13].sum(axis=1)
            shiseido_fr = shiseido_fr.astype({
                "nombre_avis": 'int', 
                "18_a_24": 'int',
                "25_a_34": 'int',
                "35_a_44": 'int',
                "45_a_54": 'int',
                "55_a_64": 'int',
                "superieur_a_65": 'int',
                "sans_age": 'int',
            })
            self.shiseido_fr = shiseido_fr
