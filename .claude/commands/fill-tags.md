# Fill Recipe Tags

Find all recipe YAML files in the recipes/ directory that are missing the 'tags' field.

For each recipe without tags:
1. Read the full recipe YAML file
2. Analyze the ingredients list
3. Generate tags based on high-level ingredient categories using the mapping below
4. Add the tags field after the cook_time line
5. Save the updated file

## Ingredient to Tag Mappings

Use these mappings to convert specific ingredients to general tags:

### Fish & Seafood
- "Lachs", "Seelachs", "Wildlachs", "Räucherlachs" → "fisch"
- "Thunfisch" → "fisch"
- "Garnelen" → "fisch"

### Meat & Poultry
- "Rinderhackfleisch", "Rindfleisch", "Rinderfilet", "Hackfleisch" → "fleisch"
- "Putenbrustfilet", "Pute" → "pute"
- "Kochschinken" → "fleisch"

### Dairy & Cheese
- "Frischkäse", "Kräuterfrischkäse", "Körniger Frischkäse" → "frischkäse"
- "Magerquark", "Quark" → "quark"
- "Schafskäse", "Feta", "Parmesan", "Bergkäse" → "käse"
- "Joghurt", "Griechischer Joghurt", "Naturjoghurt" → "joghurt"
- "Milch", "Hafermilch", "Haferdrink", "Kokosdrink" → "milch"
- "Butter", "Butterschmalz" → "butter"

### Vegetables (IMPORTANT: Use SPECIFIC tags, NOT "gemüse")
- "Zwiebel", "Frühlingszwiebel", "Rote Zwiebel" → "zwiebel"
- "Knoblauch", "Knoblauchzehe" → "knoblauch"
- "Möhren", "Karotte" → "karotte"
- "Zucchini" → "zucchini"
- "Aubergine" → "aubergine"
- "Paprika", "Gelbe Paprika" → "paprika"
- "Tomate", "Tomaten", "Kirschtomaten", "Getrocknete Tomaten" → "tomate"
- "Blumenkohl", "Brokkoli" → "kohl"
- "Spinat", "Blattspinat" → "spinat"
- "Porree", "Porreestange" → "porree"
- "Sellerie", "Knollensellerie", "Stangensellerie", "Petersilienwurzel" → "sellerie"
- "Gurke", "Salatgurke" → "gurke"
- "Avocado" → "avocado"
- "Radieschen" → "radieschen"
- "Rucola", "Salatherz", "Romana" → "salat"
- "Erbsen" → "erbsen"

### Herbs
- "Minze", "Petersilie", "Dill", "Schnittlauch" → "kräuter"

### Potatoes & Pasta
- "Kartoffel", "Süßkartoffel" → "kartoffeln"
- "Gnocchi", "Pasta", "Nudeln", "Buchweizenpasta" → "pasta"

### Rice & Grains
- "Reis", "Wildreis", "Risottoreis" → "reis"
- "Haferflocken" → "haferflocken"
- "Chiasamen" → "chiasamen"

### Flour
- "Mehl", "Buchweizenmehl", "Dinkelmehl", "Mandelmehl" → "mehl"

### Nuts & Seeds
- "Nüsse", "Walnüsse", "Mandeln", "Haselnüsse" → "nüsse"
- "Sesam" → "sesam"
- "Leinsamen" → "leinsamen"
- "Kürbiskerne", "Sonnenblumenkerne" → "kerne"

### Eggs
- "Eier", "Ei" → "eier"

### Fruits
- "Himbeeren", "Erdbeeren" → "beeren"
- "Äpfel", "Apfel", "Kiwi", "Weintrauben" → "obst"

### Fats & Oils
- "Kokosöl", "Olivenöl", "Leinöl", "Sesamöl" → "öl"

### Other
- "Honig" → "honig"

## Implementation Notes

- Match ingredient names in a case-insensitive manner
- For compound ingredients (e.g., "Kräuterfrischkäse"), match the longest substring first
- Tags should be sorted alphabetically
- Insert tags after the "cook_time:" line in the YAML file
- Format:
  ```yaml
  tags:
    - tag1
    - tag2
  ```

## After Processing

- Show a summary of which recipes were updated
- Regenerate HTML files using: python main.py
- Commit changes with message: "Add tags to recipes without tags"
