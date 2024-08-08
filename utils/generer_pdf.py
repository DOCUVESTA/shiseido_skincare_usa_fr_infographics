from fpdf import FPDF

class CustomPDF(FPDF):
    
    def __init__(self, shiseido_elements_usa, shiseido_elements_fr):
        super().__init__()
        self.shiseido_elements_usa = shiseido_elements_usa
        self.shiseido_elements_fr = shiseido_elements_fr
        
        
    def lancer_pdf(self):
        width = 960
        height = 540
        self.add_font('League_bold', '', '~/League_bold.ttf', uni=True)
        self.set_auto_page_break(auto=False, margin=0)
        self.add_page(orientation='P', format=(width, height))
        
        
    def importer_arriere_plan(self):
        self.image('/éléments graphiques/arriere_plan.png', 0, 0, w=960, h=540)
    
    
    def ajouter_nom_du_produit_usa(self):
        produit_usa = self.shiseido_elements_usa['info_usa']['nom_produit_usa']
        self.set_xy(423,185)
        self.set_font("League_bold", size=45)
        self.set_text_color(0,0,0)
        self.multi_cell(110,18,produit_usa,align="C")
     
     
    def ajouter_note_generale_usa(self):
        note_usa = self.shiseido_elements_usa['info_usa']['note_usa']
        note_usa = str(note_usa)
        self.set_font("League_bold", size=60)
        self.set_text_color(0,0,0)
        self.text(463,272,note_usa)
     
     
    def ajouter_nombre_avis_usa(self):
        avis_usa = self.shiseido_elements_usa['info_usa']['nombre_avis_usa']
        avis_usa = str(avis_usa)
        self.set_font("League_bold", size=60)
        self.set_text_color(0,0,0)
        self.text(456,336,avis_usa)
    
    
    def ajouter_graphique_usa(self):
        graphique_usa = '/éléments graphiques/graphique_usa.png'
        self.set_xy(0,0)
        self.image(graphique_usa, 355, 367, 247, 160)
    
       
    def ajouter_nom_du_produit_fr(self):
        produit_fr = self.shiseido_elements_fr['info_fr']['nom_produit_fr']
        self.set_xy(700,186)
        self.set_font("League_bold", size=40)
        self.set_text_color(0,0,0)
        self.multi_cell(138,18,produit_fr,align="C")
        
        
    def ajouter_note_generale_fr(self):
        note_fr = self.shiseido_elements_fr['info_fr']['note_fr']
        note_fr = str(note_fr)
        self.set_font("League_bold", size=60)
        self.set_text_color(0,0,0)
        self.text(751,270,note_fr)
     
     
    def ajouter_nombre_avis_fr(self):
        avis_fr = self.shiseido_elements_fr['info_fr']['nombre_avis_fr']
        avis_fr = str(avis_fr)
        self.set_font("League_bold", size=60)
        self.set_text_color(0,0,0)
        self.text(744,336,avis_fr)    
        
        
    def ajouter_graphique_fr(self):
        graphique_fr = '/éléments graphiques/graphique_fr.png'
        self.set_xy(0,0)
        self.image(graphique_fr, 645, 367, 247, 160)    
        
        
    def sauvegarder_pdf(self):
        self.output('shiseido_infographique.pdf')
