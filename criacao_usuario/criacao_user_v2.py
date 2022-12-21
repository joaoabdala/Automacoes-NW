import pyautogui as pa
import pyperclip as ppc
import time

pa.PAUSE = 0.3

# COLETA DE INFORMAÇÕES

nome = input('Nome: ')
login = input('Login: ')
senha = 'nwadv'
unidade = input('Unidade: ')
perfil = input('Perfil: ')
restrito = '1000-9000'
categoria = '28'
email = input('email: ')
cpf = input('cpf: ')
print('''10 - ACORDO
9 - ADM
11 - COMPLIANCE
1 - CJ
12 - FATURAMENTO
14 - FINANCEIRO
8 - INSTITUCIONAL
6 - LICITAÇÃO
2 - LOGISTICA
5 - SUPORTE CPJ
3 - TECNICA
4 - VERIFICAR''')
setor = input('Setor: ')

# IR PARA CONFIGURACOES E USUARIOS

time.sleep(5)
pa.click(x=168, y=28)  # CONFIGURAÇÕES
pa.click(x=209, y=166)  # USUARIOS

# NOVO USUARIO

pa.click(x=820, y=631)  # NOVO
pa.click(x=724, y=418)  # NAO
pa.press('tab')

# PREENCHER INFORMAÇÕES USUARIOS

time.sleep(1.5)
ppc.copy(nome)
pa.write(nome)
pa.press('tab')
time.sleep(0.3)
ppc.copy(login)
pa.write(login)
pa.click(x=929, y=235)  # CHAVINHA
time.sleep(0.3)
ppc.copy(senha)
pa.write(senha)
pa.press('tab')
time.sleep(0.3)
ppc.copy(senha)
pa.write(senha)
pa.click(x=704, y=434)  # SALVAR SENHA
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
ppc.copy(unidade)
pa.write(unidade)
pa.press('tab')
pa.press('tab')
pa.press('tab')
ppc.copy(perfil)
pa.write(perfil)
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
ppc.copy(restrito)
pa.write(restrito)
pa.press('tab')

# PREENCHER INFORMAÇÕES AGENDA

pa.press('f2')
pa.click(x=828, y=561)  # NOVO AGENDA
pa.click(x=450, y=271)  # CATEGORIA
ppc.copy(categoria)
pa.write(categoria)
pa.press('tab')
ppc.copy(nome)
pa.write(nome)
pa.press('tab')
ppc.copy(email)
pa.write(email)
pa.click(x=930, y=368)  # INF COMP.
pa.click(x=617, y=265)  # NIVEL.
pa.click(x=607, y=324)  # NIVEL2
pa.press('tab')
pa.press('tab')
ppc.copy(cpf)
pa.write(cpf)
pa.click(x=530, y=240)  # NW
pa.press('tab')
ppc.copy(setor)
pa.write(setor)
pa.press('tab')
pa.press('f3')
pa.press('f3')
pa.click(x=581, y=342, clicks=2)  # SELECIONA AGENDA
pa.press('tab')
