import requests
import random

def get_random_quote():
    try:
        QUOTES_URL = "https://raw.githubusercontent.com/skolakoda/programming-quotes-api/master/Data/quotes.json"
        response = requests.get(QUOTES_URL)
        if response.status_code == 200:
            quotes = response.json()
            random_quote = random.choice(quotes)
            return f"> *\"{random_quote['en']}\"*\n> — {random_quote['author']}"
        else:
            return "> *Não consegui buscar uma citação inspiradora hoje... :(*"
    except Exception as e:
        return f"> *Ocorreu um erro ao buscar a citação: {e}*"

def update_readme(quote):
    README_PATH = "README.md"
    tag_start = ""
    tag_end = ""
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()
    start_index = readme_content.find(tag_start)
    end_index = readme_content.find(tag_end)
    if start_index == -1 or end_index == -1: return
    new_readme_content = (readme_content[:start_index + len(tag_start)] + "\n" + quote + "\n" + readme_content[end_index:])
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme_content)
    print("README.md atualizado com sucesso!")

if __name__ == "__main__":
    update_readme(get_random_quote())