# Démo Mermaid pour Organisation de GN (LARP)

Ce projet est une démonstration basique visant à montrer comment utiliser **Mermaid** pour générer rapidement des rapports visuels à partir de données de personnages de GN.

L'objectif est de visualiser en un coup d'œil des ensembles de mesures éloquentes sur les personnages en cours d'écriture.

## Workflow du projet

Le processus est conçu pour être simple et automatisé :

1.  **Sources** : Les fichiers sources (Excel, Docx) contenant les données des personnages sont déposés dans un dossier `sources`.
2.  **Conversion** : Un script utilise **Pandoc** pour transformer ces fichiers en un format plus digeste (Markdown/Texte) dans un dossier `processed`.
3.  **Génération** : Un script Python lit les données traitées et génère des graphiques Mermaid (statistiques, relations, etc.).

## Structure du projet

-   `readme.md` : Ce fichier.
-   `sources/` : Dossier contenant les fichiers originaux (Excel, Word, etc.).
-   `processed/` : Dossier contenant les fichiers convertis par Pandoc.
-   `scripts/` : Contient les scripts Python pour la conversion et la génération.
-   `output/` : Contient les rapports générés avec les graphiques Mermaid.

## Prérequis

-   Python 3.x
-   Pandoc
-   Bibliothèques Python (à définir, ex: `pandas`, `matplotlib` ou simplement génération de texte)
