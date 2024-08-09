<h1 align="center">
	Document PDF Infographique Automatisé: Comparaison d'indicateurs d'avis d'un sérum Shiseido (USA vs FR)
</h1>

<h3 align="center">
	<img src="https://github.com/DOCUVESTA/shiseido_skincare_usa_fr_infographics/blob/329728b66cd969188ffced3427c0088fa25bdb95/%C3%A9l%C3%A9ments%20graphiques/header.png"/>
</h3>

## Introduction


<br>

## Flux de données
<div align="center"">
  <img src="https://github.com/DOCUVESTA/shiseido_skincare_usa_fr_infographics/blob/6cb6001d8cd1064f279b8774262028f89afe9b56/%C3%A9l%C3%A9ments%20graphiques/flux_de_donnees.png" alt="flow" width="655" height="350" />
</div>

<br>

## Contenus du dépôt
### Fichier: shiseido_infographie.pdf
#### Shiseido Beauté Japonaise Infographie
<details open>
<summary>Infographie :sparkles:</summary>
<div align="center"">
  <img src="https://github.com/DOCUVESTA/shiseido_skincare_usa_fr_infographics/blob/0bd23f94bbf2b62c5f6505b96ae359da40098407/%C3%A9l%C3%A9ments%20graphiques/shiseido_infographie.png" alt="preview"/>
</div>
</details>

<br>

### Dossier: data
#### Données brutes
<table style="width:100%">
    <tr>
        <th>Nom du Fichier</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>shiseido_usa.csv</td>
        <td>information sur les produits meilleurs ventes sur le site web usa</td>
    </tr>
    <tr>
        <td>shiseido_fr.csv</td>
        <td>information sur les produits meilleurs ventes sur le site web français</td>
    </tr>
    <tr>
        <td>shiseido_usa_rep_age.csv</td>
        <td>nombre d'avis laissés par catégorie d'âge sur les produits du site web usa</td>
    </tr>
    <tr>
        <td>shiseido_fr_rep_age.csv</td>
        <td>nombre d'avis laissés par catégorie d'âge sur les produits du site web français</td>
    </tr>
</table>


#### Données préparées
<table style="width:100%">
    <tr>
        <th>Nom du Fichier</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>elements_usa.json</td>
        <td>contenu du site web usa sur le sérum pour l'infographie</td>
    </tr>
    <tr>
        <td>elements_fr.json</td>
        <td>contenu du site web français sur le sérum pour l'infographie</td>
    </tr>
    <tr>
        <td>rep_age_usa.json</td>
        <td>répartition en pourcentage des avis par catégorie d'âge pour le site web usa</td>
    </tr>
    <tr>
        <td>rep_age_fr.json</td>
        <td>répartition en pourcentage des avis par catégorie d'âge pour le site web français</td>
    </tr>
</table>
<br>

### Dossier: utils
##### Le package Python qui comprend tout les modules utilisés pour la création infographique
```
utils/
        ├── __init__.py
        ├── chargeur_de_données.py
        ├── preparer_information_infographiques.py
        ├── creer_graphiques.py
        └── generer_pdf.py

```
### Dossier: éléments graphiques
##### Les éléments graphiques utilisés pour completer le projet
- arrière plan
- images
- graphiques
