# 🔍 ProspesScout Portugal - Extractor de Leads Locais

Script em Python desenvolvido para automatizar a prospecção de clientes locais (como oficinas, restaurantes, barbearias, etc.) em Portugal que **ainda não possuem um website próprio**, tornando-os potenciais alvos para serviços de desenvolvimento web e Landing Pages.

---

## 🚀 O que faz?
* **Pesquisa Inteligente:** Utiliza o motor de busca DuckDuckGo (via HTML scraping) para encontrar negócios locais sem depender de chaves de API pagas ou limites de requisição.
* **Filtro Automático de Leads:** Analisa os resultados e separa o que são diretórios/redes sociais (como Facebook ou TripAdvisor) de sites próprios.
* **Organização em Pastas:** 
  * Guarda os potenciais clientes (sem site) na pasta `leads/sem_site/`.
  * Guarda os negócios com site na pasta `leads/com_site/`.
* **Exportação Limpa:** Gera ficheiros `.csv` formatados com codificação `utf-8-sig` e delimitados por ponto e vírgula (perfeitos para abrir diretamente no Excel).

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* `requests` (para requisições HTTP)
* `BeautifulSoup4` (para análise e extração do HTML)

---

## ⚙️ Como Instalar e Executar

1. Clona este repositório ou descarrega os ficheiros:
   ```bash
   git clone [https://github.com/ErickSouza94/prospeccao-python.git](https://github.com/ErickSouza94/prospeccao-python.git)
   cd prospeccao-python

2. Criar um ambiente virtual:
 ```bash
python -m venv .venv

# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

3. Instala as dependências necessárias:
 ```bash 
pip install requests beautifulsoup4

4. Executa o script:
 ```bash
py prospeccao.py

---

** 💡 Desenvolvido para otimizar processos de prospecção e vendas de serviços digitais em Portugal.
