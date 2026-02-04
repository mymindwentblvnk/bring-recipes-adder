# Fill Recipe Tags

Find all recipe YAML files in the recipes/ directory that are missing the 'tags' field.

For each recipe without tags:
1. Read the full recipe YAML file
2. Analyze the ingredients list
3. Generate tags based on high-level ingredient categories using the rules and examples below
4. Add the tags field after the cook_time line
5. Save the updated file

## Tagging Rules

### General Principles

1. **Remove descriptors and adjectives**: "Griechischer Joghurt" → "joghurt", "Rote Zwiebel" → "zwiebel"
2. **Use base ingredient name**: "Kräuterfrischkäse" → "frischkäse", "Salatgurke" → "gurke"
3. **Group similar items**: "Möhren" and "Karotte" both → "karotte"
4. **Be specific for vegetables**: Don't use generic "gemüse", use specific names like "karotte", "zwiebel", "tomate"
5. **Use singular form**: "Eier" → "eier", "Tomaten" → "tomate"
6. **Lowercase tags**: All tags should be lowercase
7. **Sort alphabetically**: Tags list should be sorted
8. **Use hierarchical tags**: For categorized ingredients, include BOTH the generic category tag AND the specific ingredient tag (e.g., both "fisch" and "lachs", both "nüsse" and "mandeln")

### Hierarchical Tagging

For ingredients that belong to broader categories, add BOTH the generic tag AND the specific tag. Do NOT go deeper than one level of specificity.

**Examples:**
- Wildlachs → Add tags: "fisch" + "lachs" (NOT "wildlachs")
- Haselnüsse → Add tags: "nüsse" + "haselnüsse"
- Süßkartoffel → Add tags: "kartoffeln" + "süßkartoffel"
- Frischkäse → Add tags: "käse" + "frischkäse"

**Tag Hierarchies:**

1. **Fish (Fisch):**
   - Add "fisch" + specific type: "lachs", "thunfisch", "seelachs", "garnelen"
   - Example: Wildlachsfilet → tags: "fisch", "lachs"

2. **Meat (Fleisch):**
   - Add "fleisch" + specific type: "rind", "pute", "schinken", "hackfleisch"
   - Example: Rinderfilet → tags: "fleisch", "rind"

3. **Cheese (Käse):**
   - Add "käse" + specific type: "feta", "schafskäse", "parmesan", "bergkäse", "frischkäse"
   - Example: Kräuterfrischkäse → tags: "käse", "frischkäse"

4. **Nuts (Nüsse):**
   - Add "nüsse" + specific type: "walnüsse", "haselnüsse", "mandeln"
   - Example: Haselnüsse (gehackt) → tags: "nüsse", "haselnüsse"

5. **Berries (Beeren):**
   - Add "beeren" + specific type: "himbeeren", "erdbeeren"
   - Example: Himbeeren (frisch) → tags: "beeren", "himbeeren"

6. **Fruit (Obst):**
   - Add "obst" + specific type: "apfel", "kiwi", "weintrauben"
   - Example: Äpfel → tags: "obst", "apfel"

7. **Seeds (Kerne):**
   - Add "kerne" + specific type: "chiasamen", "leinsamen", "sesam"
   - Example: Chiasamen → tags: "kerne", "chiasamen"
   - Note: "Kürbiskerne", "Sonnenblumenkerne" → only "kerne" (these ARE the specific level)

8. **Potatoes (Kartoffeln):**
   - Add "kartoffeln" + specific type: "süßkartoffel"
   - Example: Süßkartoffel → tags: "kartoffeln", "süßkartoffel"

9. **Cabbage/Brassica (Kohl):**
   - Add "kohl" + specific type: "blumenkohl", "brokkoli"
   - Example: Blumenkohl → tags: "kohl", "blumenkohl"

### Category Guidelines

**For vegetables:** Use the specific vegetable name (e.g., "karotte", "zwiebel", "tomate", "gurke", "spinat")
- Exception: For cabbage family, use both "kohl" + specific type ("blumenkohl", "brokkoli")

**For proteins:** Use hierarchical tagging:
- Fish → Always add BOTH "fisch" + specific type ("lachs", "thunfisch", "seelachs", "garnelen")
- Meat → Always add BOTH "fleisch" + specific type ("rind", "pute", "schinken", "hackfleisch")
- Eggs → "eier" (no subtypes)

**For dairy:** Use hierarchical tagging for cheese:
- Cheese → Always add BOTH "käse" + specific type ("feta", "schafskäse", "parmesan", "bergkäse", "frischkäse")
- Milk products → "milch", "joghurt", "quark" (no subtypes)
- Butter → "butter" (no subtypes)

**For grains/starches:** Use the base name:
- Any rice → "reis"
- Any pasta/noodles → "pasta"
- Potatoes → "kartoffeln" (add "süßkartoffel" if applicable)
- Flour → "mehl"

**For nuts/seeds:** Use hierarchical tagging:
- Nuts → Always add BOTH "nüsse" + specific type ("walnüsse", "haselnüsse", "mandeln")
- Seeds → Always add BOTH "kerne" + specific type ("chiasamen", "leinsamen", "sesam")
  - Exception: "Kürbiskerne", "Sonnenblumenkerne" use only "kerne"

**For fruits:** Use hierarchical tagging:
- Berries → Always add BOTH "beeren" + specific type ("himbeeren", "erdbeeren")
- Other fruits → Always add BOTH "obst" + specific type ("apfel", "kiwi", "weintrauben")

## Ingredient Mapping Examples

Use these examples as a guide. For new ingredients not listed, apply the general principles above.

**IMPORTANT**: For categorized ingredients, add BOTH the generic category tag AND the specific tag.

### Fish & Seafood
- "Lachs", "Seelachs", "Wildlachs", "Räucherlachs" → "fisch" + "lachs"
- "Wildlachs" → "fisch" + "lachs" (NOT "wildlachs" - don't go deeper)
- "Seelachs" → "fisch" + "seelachs"
- "Thunfisch" → "fisch" + "thunfisch"
- "Garnelen" → "fisch" + "garnelen"

### Meat & Poultry
- "Rinderhackfleisch", "Rindfleisch", "Rinderfilet" → "fleisch" + "rind"
- "Hackfleisch" → "fleisch" + "hackfleisch"
- "Putenbrustfilet", "Pute" → "fleisch" + "pute"
- "Kochschinken" → "fleisch" + "schinken"

### Dairy & Cheese
- "Frischkäse", "Kräuterfrischkäse", "Körniger Frischkäse" → "käse" + "frischkäse"
- "Magerquark", "Quark" → "quark"
- "Schafskäse" → "käse" + "schafskäse"
- "Feta" → "käse" + "feta"
- "Parmesan" → "käse" + "parmesan"
- "Bergkäse" → "käse" + "bergkäse"
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
- "Blumenkohl" → "kohl" + "blumenkohl"
- "Brokkoli" → "kohl" + "brokkoli"
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
- "Kartoffel" → "kartoffeln"
- "Süßkartoffel" → "kartoffeln" + "süßkartoffel"
- "Gnocchi", "Pasta", "Nudeln", "Buchweizenpasta" → "pasta"

### Rice & Grains
- "Reis", "Wildreis", "Risottoreis" → "reis"
- "Haferflocken" → "haferflocken"

### Flour
- "Mehl", "Buchweizenmehl", "Dinkelmehl", "Mandelmehl" → "mehl"

### Nuts & Seeds
- "Walnüsse" → "nüsse" + "walnüsse"
- "Haselnüsse" → "nüsse" + "haselnüsse"
- "Mandeln (gemahlen)" → "nüsse" + "mandeln"
- "Chiasamen" → "kerne" + "chiasamen"
- "Leinsamen" → "kerne" + "leinsamen"
- "Sesam" → "kerne" + "sesam"
- "Kürbiskerne", "Sonnenblumenkerne" → "kerne" (these are the specific level)

### Eggs
- "Eier", "Ei" → "eier"

### Fruits & Berries
- "Himbeeren" → "beeren" + "himbeeren"
- "Erdbeeren" → "beeren" + "erdbeeren"
- "Äpfel", "Apfel" → "obst" + "apfel"
- "Kiwi" → "obst" + "kiwi"
- "Weintrauben" → "obst" + "weintrauben"

### Fats & Oils
- "Kokosöl", "Olivenöl", "Leinöl", "Sesamöl" → "öl"

### Other
- "Honig" → "honig"

## How to Handle Unknown Ingredients

If you encounter an ingredient not in the examples:

1. **Identify the base ingredient**: Remove brands, adjectives, preparation methods
   - "Bio-Vollkornmehl" → "mehl"
   - "Geräucherter Tofu" → "tofu"
   - "Wildlachs" → "lachs" (don't go too specific)

2. **Determine the category and apply hierarchical tagging**:
   - Vegetable? Use the specific vegetable name (or "kohl" + specific for cabbage family)
   - Fish? Add BOTH "fisch" + specific type ("lachs", "thunfisch", etc.)
   - Meat? Add BOTH "fleisch" + specific type ("rind", "pute", "schinken", "hackfleisch")
   - Cheese? Add BOTH "käse" + specific type ("feta", "parmesan", "frischkäse", etc.)
   - Nuts? Add BOTH "nüsse" + specific type ("walnüsse", "mandeln", "haselnüsse")
   - Berries? Add BOTH "beeren" + specific type ("himbeeren", "erdbeeren")
   - Fruit? Add BOTH "obst" + specific type ("apfel", "kiwi", "weintrauben")
   - Seeds? Add BOTH "kerne" + specific type ("chiasamen", "leinsamen", "sesam")
   - Eggs? Use "eier"
   - Other dairy? Use "joghurt", "milch", "quark", or "butter"
   - Grains? Use "reis", "pasta", "mehl", "haferflocken"

3. **Use German base form**: Keep it simple and in German
   - "Cherry tomatoes" → "tomate"
   - "Spring onions" → "zwiebel"
   - "Wild salmon" → "fisch" + "lachs" (NOT "wildlachs")

4. **Be consistent**: If similar ingredients already have tags, use the same pattern
   - If "Karotten" → "karotte", then "Babymöhren" → "karotte"
   - If "Wildlachs" → "fisch" + "lachs", then "Räucherlachs" → "fisch" + "lachs"

5. **Don't go deeper than one level of specificity**:
   - ✓ Correct: "Wildlachs" → "fisch" + "lachs"
   - ✗ Wrong: "Wildlachs" → "fisch" + "lachs" + "wildlachs"

## Implementation Notes

- Match ingredient names in a case-insensitive manner
- For compound ingredients (e.g., "Kräuterfrischkäse"), extract the base ingredient
- Apply the tagging rules to determine the appropriate tag
- Tags should be sorted alphabetically
- Insert tags after the "cook_time:" line in the YAML file
- Format:
  ```yaml
  tags:
    - tag1
    - tag2
  ```

## Hierarchical Tagging Summary

### Quick Reference Table

| Ingredient | Generic Tag | + Specific Tag | Example |
|------------|-------------|----------------|---------|
| Wildlachs | fisch | lachs | "fisch", "lachs" |
| Thunfisch | fisch | thunfisch | "fisch", "thunfisch" |
| Seelachs | fisch | seelachs | "fisch", "seelachs" |
| Garnelen | fisch | garnelen | "fisch", "garnelen" |
| Rinderfilet | fleisch | rind | "fleisch", "rind" |
| Hackfleisch | fleisch | hackfleisch | "fleisch", "hackfleisch" |
| Putenbrustfilet | fleisch | pute | "fleisch", "pute" |
| Kochschinken | fleisch | schinken | "fleisch", "schinken" |
| Frischkäse | käse | frischkäse | "käse", "frischkäse" |
| Feta | käse | feta | "käse", "feta" |
| Schafskäse | käse | schafskäse | "käse", "schafskäse" |
| Parmesan | käse | parmesan | "käse", "parmesan" |
| Bergkäse | käse | bergkäse | "käse", "bergkäse" |
| Walnüsse | nüsse | walnüsse | "nüsse", "walnüsse" |
| Haselnüsse | nüsse | haselnüsse | "nüsse", "haselnüsse" |
| Mandeln | nüsse | mandeln | "nüsse", "mandeln" |
| Himbeeren | beeren | himbeeren | "beeren", "himbeeren" |
| Erdbeeren | beeren | erdbeeren | "beeren", "erdbeeren" |
| Äpfel | obst | apfel | "obst", "apfel" |
| Kiwi | obst | kiwi | "obst", "kiwi" |
| Weintrauben | obst | weintrauben | "obst", "weintrauben" |
| Chiasamen | kerne | chiasamen | "kerne", "chiasamen" |
| Leinsamen | kerne | leinsamen | "kerne", "leinsamen" |
| Sesam | kerne | sesam | "kerne", "sesam" |
| Süßkartoffel | kartoffeln | süßkartoffel | "kartoffeln", "süßkartoffel" |
| Blumenkohl | kohl | blumenkohl | "kohl", "blumenkohl" |
| Brokkoli | kohl | brokkoli | "kohl", "brokkoli" |

### Key Rule: ONE LEVEL OF SPECIFICITY

**Always stop at the second level. Never go deeper.**

- ✓ Correct: Wildlachsfilet → "fisch", "lachs"
- ✗ Wrong: Wildlachsfilet → "fisch", "lachs", "wildlachs"

## After Processing

- Show a summary of which recipes were updated
- Regenerate HTML files using: python main.py
- Commit changes with message: "Add tags to recipes without tags"
