import requests
import random
import re # Importamos a biblioteca de Expressões Regulares

def get_random_quote():
    """
    Busca uma lista de citações de programação e retorna uma aleatoriamente.
    """
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
        print(f"Ocorreu um erro: {e}")
        return "> *Ocorreu um erro ao buscar a citação.*"

def update_readme(quote):
    """
    Atualiza o README.md com a nova citação usando Expressões Regulares
    para garantir que o conteúdo antigo seja sempre substituído.
    """
    README_PATH = "README.md"
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Usamos re.sub() para encontrar o conteúdo entre as tags e substituí-lo.
    # O padrão (?s) permite que o '.' capture múltiplas linhas.
    # \1 e \2 são referências para manter as tags originais no lugar.
    tag_start = ""
    tag_end = ""
    
    pattern = f"({tag_start})(?s)(.*)({tag_end})"
    
    new_readme_content = re.sub(
        pattern,
        f"\\1\n{quote}\n\\3",
        readme_content
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme_content)
    
    print("README.md atualizado com sucesso!")

if __name__ == "__main__":
    citação_do_dia = get_random_quote()
    update_readme(citação_do_dia)