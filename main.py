from utils import chargeur_de_données, preparer_information_infographiques, creer_graphiques, generer_pdf

def main():
    
    # importer les fichiers csv
    fichier1 = 'shiseido_usa.csv'
    fichier2 = 'shiseido_fr.csv'
    fichier3 = 'shiseido_usa_rep_age.csv'
    fichier4 = 'shiseido_fr_rep_age.csv'
    
    # charger les données dans les dataframes
    shiseido_data = chargeur_de_données.ShiseidoChargeurDonnees(fichier1, fichier2, fichier3, fichier4)
    shiseido_data.ecrire_dataframes()
    shiseido_data.combiner_dataframes_usa()
    shiseido_data.combiner_dataframes_fr()
    shiseido_data.calculer_avis_sans_age_usa()
    shiseido_data.calculer_avis_sans_age_fr()
    
    shiseido_usa = shiseido_data.shiseido_usa
    shiseido_fr = shiseido_data.shiseido_fr
    
    # preparer les informations pour l'infographique
    shiseido_infographique = preparer_information_infographiques.ShiseidoElementsInfographiques(shiseido_usa, shiseido_fr)
    
    shiseido_infographique.generer_elements_usa()
    shiseido_infographique.generer_elements_fr()
    shiseido_infographique.calculer_repartition_avis_usa()
    shiseido_infographique.calculer_repartition_avis_fr()
    
    shiseido_elements_usa = shiseido_infographique.shiseido_elements_usa
    shiseido_elements_fr = shiseido_infographique.shiseido_elements_fr
    shiseido_rep_age_usa = shiseido_infographique.shiseido_rep_age_usa
    shiseido_rep_age_fr = shiseido_infographique.shiseido_rep_age_fr
    
    # créer graphiques pour la répartition des avis par catégories d'âges
    shiseido_graphique = creer_graphique.ShiseidoGraphique(shiseido_rep_age_usa, shiseido_rep_age_fr)
    
    shiseido_graphique.generer_graphique_repartition_avis_usa()
    shiseido_graphique.generer_graphique_repartition_avis_fr()
    
    # générer infographique en format pdf
    shiseido_pdf = generer_pdf.CustomPDF(shiseido_elements_usa, shiseido_elements_fr)
    
    shiseido_pdf.lancer_pdf()
    shiseido_pdf.importer_arriere_plan()
    shiseido_pdf.ajouter_nom_du_produit_usa()
    shiseido_pdf.ajouter_note_generale_usa()
    shiseido_pdf.ajouter_nombre_avis_usa()
    shiseido_pdf.ajouter_graphique_usa()
    shiseido_pdf.ajouter_nom_du_produit_fr()
    shiseido_pdf.ajouter_note_generale_fr()
    shiseido_pdf.ajouter_nombre_avis_fr()
    shiseido_pdf.ajouter_graphique_fr()
    shiseido_pdf.sauvegarder_pdf()

if __name__ == '__main__':
    main()
