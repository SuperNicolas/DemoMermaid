import csv
import json
import os

def process_relations(relations_str):
    if not relations_str:
        return []
    
    relations = []
    # Les relations sont séparées par des points-virgules
    raw_rels = relations_str.split(';')
    for rel in raw_rels:
        if not rel.strip():
            continue
        # Format: Cible|Type|Force
        parts = rel.split('|')
        if len(parts) == 3:
            relations.append({
                "target": parts[0].strip(),
                "type": parts[1].strip(),
                "strength": parts[2].strip()
            })
    return relations

def process_intrigues(intrigues_str):
    if not intrigues_str:
        return []
    return [i.strip() for i in intrigues_str.split(';') if i.strip()]

def main():
    source_path = os.path.join("sources", "personnages.csv")
    output_path = os.path.join("processed", "data.json")
    
    if not os.path.exists(source_path):
        print(f"Erreur: Le fichier source {source_path} n'existe pas.")
        return

    data = []
    
    with open(source_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            character = {
                "name": row['Nom'],
                "group": row['Groupe'],
                "intrigues": process_intrigues(row.get('Intrigues', '')),
                "relations": process_relations(row.get('Relations', '')),
                "influence": int(row.get('Influence', 0)),
                "secrets": int(row.get('Secrets', 0))
            }
            data.append(character)
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"Conversion terminée. Données sauvegardées dans {output_path}")

if __name__ == "__main__":
    main()
