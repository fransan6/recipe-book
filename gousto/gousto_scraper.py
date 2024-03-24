#!/usr/bin/env python3

from recipe_scrapers import scrape_me
import sys
import os

def generate_markdown(scraper):
    markdown = f"# {scraper.title()}\n\n"

    if scraper.total_time():
        markdown += f"**Cooking time:** {scraper.total_time()} mins\n\n"

    if scraper.ingredients():
        markdown += "## Ingredients:\n\n"
        for ingredient in scraper.ingredients():
            markdown += f"- {ingredient}\n"
        markdown += "\n"

    if scraper.instructions_list():
        markdown += "## Instructions:\n\n"
        for instruction in scraper.instructions_list():
            markdown += f"- {instruction}\n\n"
        markdown += "\n"

    return markdown

def write_to_file(recipe, filename):
    if os.path.exists(filename):
        print("Recipe file already exists")
    else:
        with open(filename, "w") as file:
            file.write(recipe)
        print(f"{filename} has been generated")

recipe_url = sys.argv[1]
scraper = scrape_me(f"https://www.gousto.co.uk/cookbook/{recipe_url}")

markdown_content = generate_markdown(scraper)

cleaned_recipe_title = scraper.title().replace(":", " ")
filename = f"{cleaned_recipe_title}.md"

write_to_file(markdown_content, filename)
