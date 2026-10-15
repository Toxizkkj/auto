# Automação de Extração Fiscal & Documental (Demo)

Este projeto demonstra a extração estruturada de dados de documentos (notas fiscais, recibos, pedidos de compra em PDF ou imagem) utilizando o modelo **Gemini 2.5 Flash** e saída validada via **Pydantic**, exportando os dados diretamente para um arquivo `.csv` compatível com Excel e ERPs.

---

## 1. Estrutura de Pastas

Crie a estrutura de diretórios exatamente como abaixo:

```text
automacao_documentos/
├── entrada/              <-- Coloque aqui os arquivos de teste (.png, .jpg, .pdf)
├── processados/          <-- O script moverá os arquivos para cá automaticamente
├── .env                  <-- Arquivo com sua chave GEMINI_API_KEY (não comitar)
├── .env.example          <-- Exemplo de configuração
├── requirements.txt      <-- Bibliotecas necessárias
├── app.py                <-- Script principal
└── dados_extraidos.csv   <-- Criado automaticamente ao rodar o script
```

---

## 2. Instalação e Configuração

### Passo A: Criar e Ativar Ambiente Virtual (Recomendado)
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Passo B: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo C: Configurar a Chave da API
Crie um arquivo chamado `.env` na raiz do projeto contendo:
```env
GEMINI_API_KEY=AIzaSy...SuaChaveAqui
```

---

## 3. Roteiro para a Demonstração com o Cliente

1. **Antes da reunião:**
   - Peça 1 ou 2 exemplos reais de notas/pedidos que o cliente costuma redigitar.
   - Coloque os arquivos dentro da pasta `entrada/`.
   - Certifique-se de que o arquivo `dados_extraidos.csv` esteja limpo ou excluído se quiser mostrar a criação do zero.

2. **Durante a apresentação:**
   - Abra a pasta `entrada/` e mostre o documento original (com destaque para campos complexos como tabelas de itens e valores).
   - Abra o terminal e execute:
     ```bash
     python app.py
     ```
   - Mostre o terminal processando em tempo real com mensagens de progresso.
   - Abra o arquivo `dados_extraidos.csv` gerado no Excel ou no Google Planilhas.
   - Mostre que o arquivo original foi movido para `processados/`, mantendo a auditoria e impedindo leituras duplicadas.