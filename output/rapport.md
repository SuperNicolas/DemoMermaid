# Rapport d'Analyse GN

## 1. Graphe Relationnel
Visualisation des liens entre personnages. 
- **Trait plein** : Relation Moyenne
- **Trait gras** : Relation Forte
- **Trait pointillé** : Relation Faible

```mermaid
%%{init: {'flowchart': {'curve': 'basis'}}}%%
flowchart TD
    classDef noble fill:#FFB7B2,stroke:#333,stroke-width:1px,color:black;
    classDef milice fill:#A0E7E5,stroke:#333,stroke-width:1px,color:black;
    classDef magic fill:#B4F8C8,stroke:#333,stroke-width:1px,color:black;
    classDef peuple fill:#FBE7C6,stroke:#333,stroke-width:1px,color:black;
    classDef exile fill:#E0E0E0,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5,color:#555;
    C0([Baron Alaric])
    C1([Comtesse Elara])
    C2([Capitaine Thorne])
    C3([Mage Valerius])
    C4([Servante Lise])
    C5([Soldat Garret])
    C6([Apprenti Milo])
    C7([Ermite Vieux-Jean])
    C8([Marchand Silas])
    C9([Vagabond Inconnu])
    class C0 noble
    class C1 noble
    class C2 milice
    class C3 magic
    class C4 peuple
    class C5 milice
    class C6 magic
    class C7 exile
    class C8 peuple
    class C9 exile
    C0 ==>|Amant| C1
    C0 -->|Rival| C2
    C0 -.->|Maitre| C4
    C1 ==>|Amant| C0
    C1 -->|Confidente| C3
    C2 -->|Rival| C0
    C2 ==>|Superieur| C5
    C3 -->|Conseiller| C1
    C3 ==>|Maitre| C6
    C4 -.->|Serviteur| C0
    C4 ==>|Soeur| C5
    C5 ==>|Subordonne| C2
    C5 ==>|Frere| C4
    C6 ==>|Eleve| C3
    C8 -->|Creancier| C0
    C8 -.->|Creancier| C2
```

## 2. Cartographie des Intrigues (Mindmap)
Vue d'ensemble des intrigues et des personnages impliqués.

```mermaid
%%{init: {'theme': 'base'}}%%
mindmap
  root((Intrigues))
    Complot du Roi
      Baron Alaric
      Comtesse Elara
    Dette de Jeu
      Baron Alaric
      Capitaine Thorne
      Marchand Silas
    Héritage Caché
      Baron Alaric
      Mage Valerius
      Servante Lise
    Secret du Sanctuaire
      Comtesse Elara
      Mage Valerius
    Menace Frontalière
      Capitaine Thorne
      Soldat Garret
    Rituel Interdit
      Mage Valerius
      Apprenti Milo
```

## 3. Matrice Influence / Secrets
Comparaison de l'influence politique et des secrets détenus par chaque personnage.

```mermaid
xychart-beta
    title "Matrice Influence vs Secrets"
    x-axis "Influence" 0 --> 10
    y-axis "Secrets" 0 --> 10
    line [9, 8, 6, 7, 2, 3, 4, 1, 5, 0]
    line [8, 9, 4, 10, 7, 2, 5, 9, 3, 1]
```

## 4. Puissance Narrative
Estimation de la charge de jeu (Nombre d'intrigues + Nombre de relations).
Permet d'identifier les personnages surchargés ou délaissés.

```mermaid
xychart-beta
    title "Puissance Narrative (Intrigues + Relations)"
    x-axis ["Baron Alaric", "Mage Valerius", "Comtesse Elara", "Capitaine Thorne", "Servante Lise", "Soldat Garret", "Marchand Silas", "Apprenti Milo", "Ermite Vieux-Jean", "Vagabond Inconnu"]
    bar [6, 5, 4, 4, 3, 3, 3, 2, 0, 0]
```

## 5. Répartition des Intrigues
Quelles sont les intrigues les plus connectées ?

```mermaid
pie title Répartition des Intrigues
    "Complot du Roi" : 2
    "Dette de Jeu" : 3
    "Héritage Caché" : 3
    "Secret du Sanctuaire" : 2
    "Menace Frontalière" : 2
    "Rituel Interdit" : 2
```

## 6. Répartition des Groupes

```mermaid
pie title Répartition des Groupes
    "Noblesse" : 2
    "Milice" : 2
    "Cercle Magique" : 2
    "Peuple" : 1
    "Exilés" : 2
    "Bourgeoisie" : 1
```

