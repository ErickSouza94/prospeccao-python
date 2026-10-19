import csv
import os
import requests
from bs4 import BeautifulSoup


def pesquisar_leads(setor: str, localidade: str):
  query = f"{setor} em {localidade}, Portugal"
  url = "https://html.duckduckgo.com/html/"
  params = {"q": query}

  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/120.0.0.0 Safari/537.36"
      )
  }

  print(
      f"A analisar o mercado para '{setor}' em '{localidade}' (à procura de"
      " oportunidades)..."
  )
  try:
    response = requests.post(url, data=params, headers=headers, timeout=15)
    if response.status_code != 200:
      print(f"Erro ao aceder à pesquisa: {response.status_code}")
      return []

    soup = BeautifulSoup(response.text, "html.parser")
    todos_os_resultados = []

    for resultado in soup.find_all("div", class_="result"):
      link_tag = resultado.find("a", class_="result__url")
      titulo_tag = resultado.find("a", class_="result__a")
      snippet_tag = resultado.find("a", class_="result__snippet")

      if titulo_tag:
        nome = titulo_tag.get_text().strip()
        website = link_tag.get_text().strip() if link_tag else ""
        descricao = snippet_tag.get_text().strip() if snippet_tag else ""

        # Identificar se o resultado é um diretório/redes sociais ou um site próprio
        tem_site_proprio = True
        if not website or any(
            diretorio in website.lower()
            for diretorio in [
                "facebook.com",
                "instagram.com",
                "olx.pt",
                "cuspo.pt",
                "yellowpages",
                "cm-",
            ]
        ):
          tem_site_proprio = False
          website = "NAO TEM SITE"

        todos_os_resultados.append({
            "nome": nome,
            "website": website,
            "tem_website": "SIM" if tem_site_proprio else "NAO",
            "detalhes": descricao,
        })

    return todos_os_resultados

  except Exception as e:
    print(f"Ocorreu um erro: {e}")
    return []


def main():
  localidade = input("Localidade a pesquisar (ex: Marinha Grande): ").strip()
  setor = input("Setor a pesquisar (ex: oficina auto, restaurante): ").strip()

  if not localidade or not setor:
    print("Preencha todos os campos.")
    return

  dados = pesquisar_leads(setor, localidade)

  if not dados:
    print("Nenhum resultado encontrado.")
    return

  # Definir e garantir a existência das subpastas dentro de "leads"
  pasta_sem_site = os.path.join("leads", "sem_site")
  pasta_com_site = os.path.join("leads", "com_site")
  os.makedirs(pasta_sem_site, exist_ok=True)
  os.makedirs(pasta_com_site, exist_ok=True)

  # Separar entre os que têm site e os que NÃO têm site (Leads)
  sem_site = [r for r in dados if r["tem_website"] == "NAO"]
  com_site = [r for r in dados if r["tem_website"] == "SIM"]

  slug = f"{setor}_{localidade}".lower().replace(" ", "_").replace(",", "")

  # Lista de campos declarados explicitamente para o CSV
  campos_csv = ["nome", "website", "tem_website", "detalhes"]

  # Guardar ficheiro de Leads na pasta "leads/sem_site"
  if sem_site:
    nome_ficheiro = f"leads_sem_site_{slug}.csv"
    caminho_leads = os.path.join(pasta_sem_site, nome_ficheiro)

    with open(caminho_leads, "w", newline="", encoding="utf-8-sig") as f:
      writer = csv.DictWriter(f, fieldnames=campos_csv, delimiter=";")
      writer.writeheader()
      writer.writerows(sem_site)
    print(
        f"→ Ficheiro de LEADS guardado em: '{caminho_leads}' ({len(sem_site)}"
        " registos)."
    )
  else:
    print("Não foram encontrados potenciais leads sem site nesta pesquisa.")

  # Guardar ficheiro de negócios com site na pasta "leads/com_site"
  if com_site:
    nome_ficheiro_com = f"negocios_com_site_{slug}.csv"
    caminho_com = os.path.join(pasta_com_site, nome_ficheiro_com)

    with open(caminho_com, "w", newline="", encoding="utf-8-sig") as f:
      writer = csv.DictWriter(f, fieldnames=campos_csv, delimiter=";")
      writer.writeheader()
      writer.writerows(com_site)
    print(
        f"→ Ficheiro de negócios com site guardado em: '{caminho_com}'"
        f" ({len(com_site)} registos)."
    )


if __name__ == "__main__":
  main()