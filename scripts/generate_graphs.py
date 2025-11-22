import json
import os
from collections import Counter

def load_data():
    with open(os.path.join("processed", "data.json"), 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_relational_graph(data):
    # Configuration pour un rendu plus "organique"
    mermaid = ["%%{init: {'flowchart': {'curve': 'basis'}}}%%"]
    mermaid.append("flowchart TD")
    
    # Styles - Palette plus douce et moderne (Pastel)
    mermaid.append("    classDef noble fill:#FFB7B2,stroke:#333,stroke-width:1px,color:black;")
    mermaid.append("    classDef milice fill:#A0E7E5,stroke:#333,stroke-width:1px,color:black;")
    mermaid.append("    classDef magic fill:#B4F8C8,stroke:#333,stroke-width:1px,color:black;")
    mermaid.append("    classDef peuple fill:#FBE7C6,stroke:#333,stroke-width:1px,color:black;")
    mermaid.append("    classDef exile fill:#E0E0E0,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5,color:#555;")
    
    # Nodes
    ids = {}
    for i, char in enumerate(data):
        safe_id = f"C{i}"
        ids[char['name']] = safe_id
        
        # Determine class based on group (simple mapping)
        style_class = ""
        grp = char['group'].lower()
        if "noblesse" in grp: style_class = ":::noble"
        elif "milice" in grp: style_class = ":::milice"
        elif "cercle" in grp: style_class = ":::magic"
        elif "peuple" in grp or "bourgeoisie" in grp: style_class = ":::peuple"
        else: style_class = ":::exile"
        
        # Utilisation de formes arrondies ([Nom]) au lieu de rectangles
        mermaid.append(f"    {safe_id}([{char['name']}])")
    
    # Apply class styles
    for i, char in enumerate(data):
        safe_id = f"C{i}"
        grp = char['group'].lower()
        if "noblesse" in grp: class_name = "noble"
        elif "milice" in grp: class_name = "milice"
        elif "cercle" in grp: class_name = "magic"
        elif "peuple" in grp or "bourgeoisie" in grp: class_name = "peuple"
        else: class_name = "exile"
        mermaid.append(f"    class {safe_id} {class_name}")

    # Edges
    for char in data:
        source_id = ids.get(char['name'])
        if not source_id: continue
        
        for rel in char['relations']:
            target_name = rel['target']
            target_id = ids.get(target_name)
            
            if target_id:
                # Arrow style based on strength
                arrow = "-->"
                if rel['strength'].lower() == "fort": arrow = "==>"
                elif rel['strength'].lower() == "faible": arrow = "-.->"
                
                label = rel['type']
                mermaid.append(f"    {source_id} {arrow}|{label}| {target_id}")
                
    return "\n".join(mermaid)

def generate_intrigue_pie(data):
    intrigues = []
    for char in data:
        intrigues.extend(char['intrigues'])
    
    counts = Counter(intrigues)
    
    mermaid = ["pie title Répartition des Intrigues"]
    for intrigue, count in counts.items():
        mermaid.append(f"    \"{intrigue}\" : {count}")
        
    return "\n".join(mermaid)

def generate_narrative_load(data):
    # Load = nb intrigues + nb relations
    # We want to sort by load to see extremes
    
    loads = []
    for char in data:
        load = len(char['intrigues']) + len(char['relations'])
        loads.append((char['name'], load))
        
    # Sort descending
    loads.sort(key=lambda x: x[1], reverse=True)
    
    # Using xychart-beta for bar chart
    mermaid = ["xychart-beta"]
    mermaid.append("    title \"Puissance Narrative (Intrigues + Relations)\"")
    
    names = [f"\"{x[0]}\"" for x in loads]
    values = [str(x[1]) for x in loads]
    
    mermaid.append(f"    x-axis [{', '.join(names)}]")
    mermaid.append(f"    bar [{', '.join(values)}]")
    
    return "\n".join(mermaid)

def generate_group_pie(data):
    groups = [c['group'] for c in data]
    counts = Counter(groups)
    
    mermaid = ["pie title Répartition des Groupes"]
    for grp, count in counts.items():
        mermaid.append(f"    \"{grp}\" : {count}")
        
    return "\n".join(mermaid)

def generate_intrigue_mindmap(data):
    # Map intrigue -> list of characters
    intrigue_map = {}
    for char in data:
        for intrigue in char['intrigues']:
            if intrigue not in intrigue_map:
                intrigue_map[intrigue] = []
            intrigue_map[intrigue].append(char['name'])
            
    mermaid = ["%%{init: {'theme': 'base'}}%%"]
    mermaid.append("mindmap")
    mermaid.append("  root((Intrigues))")
    
    for intrigue, chars in intrigue_map.items():
        mermaid.append(f"    {intrigue}")
        for char in chars:
            mermaid.append(f"      {char}")
            
    return "\n".join(mermaid)

def generate_influence_secrets_chart(data):
    # Using xychart instead of quadrant for better compatibility
    lines = []
    lines.append("xychart-beta")
    lines.append("    title \"Matrice Influence vs Secrets\"")
    lines.append("    x-axis \"Influence\" 0 --> 10")
    lines.append("    y-axis \"Secrets\" 0 --> 10")
    
    # Create series for scatter plot
    influence_values = [str(char['influence']) for char in data]
    secrets_values = [str(char['secrets']) for char in data]
    
    lines.append(f"    line [{', '.join(influence_values)}]")
    lines.append(f"    line [{', '.join(secrets_values)}]")
        
    return "\n".join(lines)

def main():
    data = load_data()
    
    md_content = "# Rapport d'Analyse GN\n\n"
    
    md_content += "## 1. Graphe Relationnel\n"
    md_content += "Visualisation des liens entre personnages. \n"
    md_content += "- **Trait plein** : Relation Moyenne\n"
    md_content += "- **Trait gras** : Relation Forte\n"
    md_content += "- **Trait pointillé** : Relation Faible\n\n"
    md_content += "```mermaid\n" + generate_relational_graph(data) + "\n```\n\n"
    
    md_content += "## 2. Cartographie des Intrigues (Mindmap)\n"
    md_content += "Vue d'ensemble des intrigues et des personnages impliqués.\n\n"
    md_content += "```mermaid\n" + generate_intrigue_mindmap(data) + "\n```\n\n"

    md_content += "## 3. Matrice Influence / Secrets\n"
    md_content += "Comparaison de l'influence politique et des secrets détenus par chaque personnage.\n\n"
    md_content += "```mermaid\n" + generate_influence_secrets_chart(data) + "\n```\n\n"

    md_content += "## 4. Puissance Narrative\n"
    md_content += "Estimation de la charge de jeu (Nombre d'intrigues + Nombre de relations).\n"
    md_content += "Permet d'identifier les personnages surchargés ou délaissés.\n\n"
    md_content += "```mermaid\n" + generate_narrative_load(data) + "\n```\n\n"
    
    md_content += "## 5. Répartition des Intrigues\n"
    md_content += "Quelles sont les intrigues les plus connectées ?\n\n"
    md_content += "```mermaid\n" + generate_intrigue_pie(data) + "\n```\n\n"

    md_content += "## 6. Répartition des Groupes\n\n"
    md_content += "```mermaid\n" + generate_group_pie(data) + "\n```\n\n"
    
    output_path = os.path.join("output", "rapport.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Rapport généré : {output_path}")

if __name__ == "__main__":
    main()
