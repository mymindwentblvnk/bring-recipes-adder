import yaml
from pathlib import Path
from typing import Any


def format_time(minutes: int) -> str:
    """Convert minutes to ISO 8601 duration format (PT{minutes}M)."""
    return f"PT{minutes}M"


def generate_html(recipe: dict[str, Any]) -> str:
    """Generate HTML with Schema.org microdata and Bring! widget from recipe data."""

    # Generate ingredients HTML
    ingredients_html = []
    for ingredient in recipe['ingredients']:
        ingredients_html.append(f'''            <li itemprop="recipeIngredient">
                <span class="amount">{ingredient['amount']}</span>
                <span class="ingredient">{ingredient['name']}</span>
            </li>''')

    # Generate instructions HTML
    instructions_html = []
    for instruction in recipe['instructions']:
        instructions_html.append(f'''                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/HowToStep">
                    <span itemprop="text">{instruction}</span>
                </li>''')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{recipe['name']} Recipe</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        .amount {{
            font-weight: bold;
            min-width: 80px;
            display: inline-block;
            color: #2c5282;
        }}
        .ingredient {{
            color: #333;
        }}
        ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        li {{
            padding: 5px 0;
        }}
    </style>
</head>
<body>
    <div itemscope itemtype="https://schema.org/Recipe">
        <h1 itemprop="name">{recipe['name']}</h1>

        <p itemprop="description">{recipe.get('description', '')}</p>

        <div itemprop="author" itemscope itemtype="https://schema.org/Person">
            <meta itemprop="name" content="{recipe.get('author', 'Unknown')}">
        </div>

        <time itemprop="prepTime" datetime="{format_time(recipe['prep_time'])}">Prep time: {recipe['prep_time']} minutes</time>
        <br>
        <time itemprop="cookTime" datetime="{format_time(recipe['cook_time'])}">Cook time: {recipe['cook_time']} minutes</time>
        <br>
        <meta itemprop="recipeYield" content="{recipe['servings']} servings">
        <span>Yield: {recipe['servings']} servings</span>

        <h2>Ingredients:</h2>
        <ul>
{chr(10).join(ingredients_html)}
        </ul>

        <h2>Instructions:</h2>
        <div itemprop="recipeInstructions" itemscope itemtype="https://schema.org/HowToSection">
            <ol>
{chr(10).join(instructions_html)}
            </ol>
        </div>
    </div>
    <script async="async" src="//platform.getbring.com/widgets/import.js"></script>
<div data-bring-import style="display:none">
       <a href="https://www.getbring.com">Bring! Einkaufsliste App f&uuml;r iPhone und Android</a>
</div>
</body>
</html>'''

    return html


def main():
    """Generate HTML files from YAML recipes."""
    recipes_dir = Path("recipes")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Process all YAML files in recipes directory
    for yaml_file in recipes_dir.glob("*.yaml"):
        print(f"Processing {yaml_file.name}...")

        # Read YAML recipe
        with open(yaml_file, 'r', encoding='utf-8') as f:
            recipe = yaml.safe_load(f)

        # Generate HTML
        html = generate_html(recipe)

        # Write HTML file
        output_file = output_dir / f"{yaml_file.stem}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"  → Generated {output_file}")

    print("\nDone! HTML files are in the 'output' directory.")


if __name__ == "__main__":
    main()
