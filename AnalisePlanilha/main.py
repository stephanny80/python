# Passo a passo da solução

# Imports
# openpyxl - integração com XLS
import openpyxl
# Message
from app.message import Message

# Abrir os arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
extensao = '.xlsx'
texto = ''
fone_to = '+5534988989078'

meta_venda = 40000

# Para cada arquivo:
for mes in lista_meses:
    dataframe = openpyxl.load_workbook(f'files\\{mes}{extensao}').active
    for row in range(0, dataframe.max_row):
        vendedor = dataframe[f'A{row + 1}'].value
        vendas = dataframe[f'B{row + 1}'].value

        # Verificar se algum valor na coluna VENDAS daquele arquivo é maior que a meta
        if isinstance(vendas, float):
            if vendas > meta_venda:
                texto = f'{texto}Mês/Meta {mes}/{meta_venda} Vendedor {vendedor} Venda {vendas}\n'

# Se for maior que a meta, enviar SMS com nome, mes e a quantidade de vendas

sid = Message.SendWhatsApp(texto, fone_to)
print(message.sid)
