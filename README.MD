# 🔍 ProspesScout - Extractor de Leads Locais

Script em Python desenvolvido para automatizar a prospecção de clientes locais (como oficinas, restaurantes, barbearias, etc.) que **ainda não possuem um website próprio**, tornando-os alvos ideais para serviços de desenvolvimento web (Landing Pages).

---

## 🚀 O que faz?

- **Pesquisa Inteligente:** Utiliza o motor de busca DuckDuckGo (via HTML scraping) para encontrar negócios locais sem depender de chaves de API pagas ou limites de requisição.
- **Filtro Automático de Leads:** Analisa os resultados e separa o que são diretórios/redes sociais (como Facebook ou TripAdvisor) de sites próprios.
- **Organização em Pastas:**
  - Guarda os potenciais clientes (sem site) na pasta `leads/sem_site/`.
  - Guarda os negócios com site na pasta `leads/com_site/`.
- **Exportação Limpa:** Gera ficheiros `.csv` formatados com codificação `utf-8-sig` e delimitados por ponto e vírgula (perfeitos para abrir no Excel).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- `requests` (para requisições HTTP)
- `BeautifulSoup4` (para análise e extração do HTML)

---

## ⚙️ Como Instalar e Executar

1. Clona este repositório ou descarrega os ficheiros:
   ```bash
   git clone [https://github.com/teu-utilizador/prospeccao-python.git](https://github.com/teu-utilizador/prospeccao-python.git)
   cd prospeccao-python
   ```
