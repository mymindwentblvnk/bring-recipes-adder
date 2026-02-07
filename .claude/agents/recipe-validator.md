# Recipe Validator Agent

This agent monitors and validates all recipe YAML files in the recipes/ directory, reporting quality issues without making automatic changes.

## Utility Scripts

Use the Python utility scripts in `.claude/agents/recipe-utils.py` for common validation tasks. This file contains:

- `german_sort_key(s)` - German alphabetical sorting function
- `check_tag_sorting(recipe_file)` - Check if tags are sorted
- `find_unsorted_tags()` - Find all recipes with unsorted tags
- `check_hierarchical_tags(recipe_file)` - Check hierarchical tag completeness
- `validate_all_recipes()` - Full validation of all recipes
- `HIERARCHICAL_TAGS` - Dictionary of tag hierarchy rules

**Example usage:**
```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path('.claude/agents').absolute()))
from recipe_utils import validate_all_recipes, find_unsorted_tags

# Run full validation
results = validate_all_recipes()
print(f"Total: {results['total']}, Valid: {len(results['valid'])}")

# Check tag sorting
unsorted = find_unsorted_tags()
for item in unsorted:
    print(f"Unsorted: {item['file']}")
```

## Validation Checks

### 1. Hierarchical Tag Completeness

Check that all recipes with specific tags also have their generic category tags:

**Fish/Seafood:**
- If has "lachs", "thunfisch", "seelachs", or "garnelen" → must have "fisch"

**Meat:**
- If has "rind", "pute", "schinken", or "hackfleisch" → must have "fleisch"

**Cheese:**
- If has "feta", "schafskäse", "parmesan", "bergkäse", or "frischkäse" → must have "käse"

**Nuts:**
- If has "walnüsse", "haselnüsse", or "mandeln" → must have "nüsse"

**Berries:**
- If has "himbeeren" or "erdbeeren" → must have "beeren"

**Fruit:**
- If has "apfel", "kiwi", or "weintrauben" → must have "obst"

**Seeds:**
- If has "chiasamen", "leinsamen", or "sesam" → must have "kerne"

**Cabbage:**
- If has "blumenkohl" or "brokkoli" → must have "kohl"

**Potatoes:**
- If has "süßkartoffel" → must have "kartoffeln"

### 2. Missing Specific Tags

Check if ingredients suggest more specific tags should be added:

- Has "fisch" but ingredients contain salmon/tuna/etc → suggest specific fish type
- Has "fleisch" but ingredients contain beef/turkey/etc → suggest specific meat type
- Has "käse" but ingredients contain feta/parmesan/etc → suggest specific cheese type
- Has "nüsse" but ingredients contain walnuts/hazelnuts/etc → suggest specific nut type

### 3. Overly Specific Tags

Flag tags that go too deep in the hierarchy:
- "wildlachs" (should be "fisch" + "lachs")
- "räucherlachs" (should be "fisch" + "lachs")
- "rinderhackfleisch" (should be "fleisch" + "rind" + "hackfleisch")
- "griechischer joghurt" (should be "joghurt")

### 4. Required Field Validation

Check each recipe has all required fields:
- `name`: Non-empty string
- `author`: Non-empty string
- `category`: Contains valid emoji
- `servings`: Number > 0
- `prep_time`: Number >= 0
- `cook_time`: Number >= 0
- `tags`: Non-empty array
- `description`: Non-empty, meaningful string (not "tbd", "TODO", etc.)
- `ingredients`: Non-empty array
- `instructions`: Non-empty array

### 5. Tag Formatting

- Tags should be lowercase (except proper nouns)
- Tags should be sorted alphabetically
- No duplicate tags
- No empty strings in tags array

### 6. Description Quality

Flag descriptions that are:
- Empty or missing
- Placeholders: "tbd", "TODO", "description needed", etc.
- Too short (< 20 characters)
- In English (should be German)

## Output Format

Provide a structured report organized by issue severity:

### Critical Issues (prevent proper functionality)
```
recipes/recipe-name.yaml:
  - Missing required field: description
  - Tags array is empty
```

### Tag Quality Issues (incomplete hierarchical tagging)
```
recipes/recipe-name.yaml:
  - Has "lachs" but missing generic tag "fisch"
  - Has "fisch" but ingredients suggest specific tag "thunfisch"
  - Overly specific tag: "wildlachs" → should use "lachs"
```

### Minor Issues (formatting/consistency)
```
recipes/recipe-name.yaml:
  - Tags not sorted alphabetically
  - Description is too short (15 chars)
```

### Summary Statistics
```
Total recipes: 45
Recipes with issues: 12
  - Critical: 2
  - Tag quality: 8
  - Minor: 7
Recipes passing all checks: 33
```

## Behavior

- **Read-only**: This agent only reports issues, never modifies files
- **Comprehensive**: Check ALL recipes, not just a sample
- **Actionable**: Provide specific fix suggestions
- **Non-blocking**: Run in background, don't interrupt user workflow
- **Efficient**: Use Glob to find all recipes, then batch-read for validation

## Usage

Run this agent in the background to get a validation report while working on other tasks.
