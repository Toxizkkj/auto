import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PASTA_ENTRADA = Path("entrada")
PASTA_ENTRADA.mkdir(exist_ok=True)

# Dimensões simulando bobina térmica padrão 80mm
largura = 500
altura = 680
imagem = Image.new("RGB", (largura, altura), color=(250, 250, 245))
draw = ImageDraw.Draw(imagem)

# Carrega fonte padrão do sistema
try:
    fonte = ImageFont.load_default()
except Exception:
    fonte = None

linhas_texto = [
    "================================================",
    "       AUTO MECANICA & PECAS CENTRAL LTDA       ",
    "  CNPJ: 12.345.678/0001-90 | IE: 87.654.321    ",
    "      RUA DAS PALMEIRAS, 150 - CENTRO           ",
    "================================================",
    "DATA: 14/10/2026                 HORA: 16:42:10 ",
    "DOC / ORDEM DE SERVICO: 004821                  ",
    "------------------------------------------------",
    "QTD  DESC. ITEM                VL.UNIT   VL.TOT ",
    "------------------------------------------------",
    "04   OLEO MOTOR 5W30 SINT      R$ 48,00  192,00 ",
    "01   FILTRO DE OLEO PH6017     R$ 38,50   38,50 ",
    "01   JOGO PASTILHA FREIO DIANT R$ 145,00 145,00 ",
    "02   DISCO DE FREIO VENTILADO  R$ 180,00 360,00 ",
    "01   MAO DE OBRA REVISAO GERAL R$ 220,00 220,00 ",
    "------------------------------------------------",
    "QTD. TOTAL DE ITENS:                         5  ",
    "SUBTOTAL:                             R$ 955,50 ",
    "DESCONTO A VISTA:                      R$ 45,50 ",
    "VALOR TOTAL A PAGAR:                  R$ 910,00 ",
    "------------------------------------------------",
    "FORMA DE PAGAMENTO: PIX                         ",
    "OPERADOR: CARLOS TIAGO (CAIXA 02)               ",
    "================================================",
    "          OBRIGADO PELA PREFERENCIA!            ",
    "================================================"
]

# Desenha as linhas simulando o cupom impresso
posicao_y = 35
for linha in linhas_texto:
    draw.text((25, posicao_y), linha, fill=(20, 20, 20), font=fonte)
    posicao_y += 24

caminho_saida = PASTA_ENTRADA / "recibo_mecanica_004821.png"
imagem.save(caminho_saida)
print(f"[OK] Recibo de teste gerado com sucesso em: {caminho_saida}")