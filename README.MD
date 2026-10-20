# 🔍 ProspesScout - Extractor de Leads Locais

Script em Python desenvolvido para automatizar a prospecção de clientes locais (como oficinas, restaurantes, barbearias, etc.) que **ainda não possuem um website próprio**, tornando-os potenciais alvos para serviços de desenvolvimento web e Landing Pages.

---

## 🚀 O que faz?
* **Pesquisa Inteligente:** Utiliza o motor de busca DuckDuckGo para encontrar negócios locais sem depender de chaves de API pagas.
* **Filtro Automático de Leads:** Separa diretórios e redes sociais de sites próprios.
* **Organização em Pastas:** 
  * Leads (sem site) guardados em `leads/sem_site/`.
  * Negócios com site guardados em `leads/com_site/`.
* **Exportação Limpa:** Gera ficheiros `.csv` em formato UTF-8-SIG delimitados por ponto e vírgula.

---

## 🛠️ Tecnologias Utilizadas
* Python 3.x
* `requests`
* `BeautifulSoup4`

---

## ⚙️ Como Instalar e Executar

1. Clona este repositório:
   `git clone [https://github.com/ErickSouza94/prospeccao-python.git](https://github.com/ErickSouza94/prospeccao-python.git)`

2. Entra na pasta do projeto:
   `cd prospeccao-python`

3. Cria e ativa o ambiente virtual:
   `python -m venv .venv`
   *(No Windows PowerShell: `.\.venv\Scripts\Activate.ps1`)*

4. Instala as dependências:
   `pip install requests beautifulsoup4`

5. Executa o script:
   `py prospeccao.py`

---

💡 *Desenvolvido para otimizar processos de prospecção e vendas de serviços digitais.*
