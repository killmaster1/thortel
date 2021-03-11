from telegram.ext import *
import logging
import urllib
import re 
import os
import time
import datetime
import logging
from time import sleep
import requests, time, re
import platform
from lxml import html
from bs4 import BeautifulSoup
import requests
import bs4
updater = Updater(token='1646160421:AAEKWctSCSY_FkAASWJschHBPMwBX4vn1_4', use_context=True)
def pr(msg, tempo):
    for i in msg:
        sys.stdout.write('')
        sys.stdout.write(f'{i}')
        sys.stdout.flush()
        sleep(tempo)
os.system('cls')
print('''


              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||


     Soque o Enter para continuar
''')

from os import system
import sys
from getpass import getpass
# password = getpass(" ")

# pr('''
# .=====================================================.
# ||                                                   ||
# ||   _       _--""--_                                ||
# ||     " --""   |    |   .--.           |    ||      ||
# ||   " . _|     |    |  |    |          |    ||      ||
# ||   _    |  _--""--_|  |----| |.-  .-i |.-. ||      ||
# ||     " --""   |    |  |    | |   |  | |  |         ||
# ||   " . _|     |    |  |    | |    `-( |  | ()      ||
# ||   _    |  _--""--_|             |  |              ||
# ||     " --""                      `--'              ||
# ||                                                   ||
# `=====================================================`


# ''', 0.001)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def cep(update, context):
    import requests
    import json
    try:
        cep = update.message.text[5:]
        requisicao = requests.get("http://viacep.com.br/ws/" + cep + "/json/")
        cotacao = requisicao.json()
        cotacao
        cep = cotacao['cep']
        logradouro = cotacao['logradouro']
        bairro = cotacao['bairro']
        uf = cotacao['uf']
        localidade = cotacao['localidade']
        ibge = cotacao['ibge']
        gia = cotacao['gia']
        ddd = cotacao['ddd']
        siafi = cotacao['siafi']
        complemento = cotacao['complemento']
        update.message.reply_text(f'''Informações do Cep:

Cep:  {cep}
Cidade: {localidade}
UF: {uf}
DDD: {ddd}
Bairro: {bairro}
Logradouro: {logradouro}
Complemento: {complemento}
IBGE: {ibge}
GIA: {gia}
SIAFI: {siafi}
    ''')
    except:
        update.message.reply_text(f'Cep inválido!')

#Snuking/Somos uma legião. 2021 ©

def comandos(update, context):
    update.message.reply_text('''
======Thor Comandos======

/cpf xxx.xxx.xxx-xx
/vizinhos xxx.xxx.xxx-xx
/ip xx.xxx.xxx.xx
/placa abc1234
/cep (em breve)
/email (em breve)
/telefone (em breve)

Meu criador @killman1''')

def ip(update, context):
  ip = update.message.text[3:].strip()
  print(ip)
  try:
      api = f"https://ipapi.co/{ip}/json"
      print(api)
      api = requests.get(api)
      resultado = api.json()
      print(resultado)
      ip = resultado['ip']
      cidade =f"Cidade: {resultado['city']}"
      regiao =f"Região: {resultado['region']}"
      cep = f"Código postal: {resultado['postal']}"
      la =f"Latitude: {resultado['latitude']}"
      lo = f"Longitude: {resultado['longitude']}"
      city =f"Fuso horário: {resultado['timezone']}"
      net =f"ORG: {resultado['org']}"
      ver = f"Versão: {resultado['version']}"
      api = requests.get(f"https://ipapi.co/{ip}/json")
      resultado = api.json()
      print ('\n' + f'Google Maps: {Y}' + 'https://www.google.com/maps/place/' + f"{resultado['latitude']}" + '+' + f"{resultado['longitude']}")
      gps = f'Google Maps: ' + 'https://www.google.com/maps/place/' + f"{resultado['latitude']}" + '+' + f"{resultado['longitude']}"
      update.message.reply_text(f''' 
==========Thor Bot=========

IP: {ip}
{cidade}
{regiao}
{cep}
{la}
{lo}
{city}
{net}
{ver}
Google: {gps}
''')
  except:
      print("erro inesperado")
      update.message.reply_text('Ocorreu um erro inesperada ao consultar o ip: '+ip)


def placa(update, context):
    import time
    import urllib.request
    inicio = time.time()
    p = update.message.text.split(' ')
    if(len(p[1])>7 or len(p[1]) < 7):
        print(len(p[1]))  
        update.message.reply_text(f'⚠️PLACA INVÁLIDA!')
    else:
        if(is_number(p[1][3:7]) == False or is_number(p[1][0]) == True or is_number(p[1][1]) == True or is_number(p[1][2]) == True):
            print('Placa inválida!')
            update.message.reply_text(f'⚠️PLACA INVÁLIDA!')
        else:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
                api = requests.get(f'https://thorconsultas.000webhostapp.com/placa.php?placa={p[1]}', headers=headers).json()
                if(len(api['VEICULO']['placa']) < 4):
                    update.message.reply_text(f'⚠️Nada encontrado....')
                    exit()
                else:
                    cont = len(api['VEICULO']['cpf'])
                    print(cont)
                    print(api['VEICULO']['cpf'][:11])
                    cpf = 0
                    if(cont == 14):
                        cpf = api['VEICULO']['cpf'][:11]
                        print(cpf)
                    if(cont == 17):
                        cpf = api['VEICULO']['cpf'][:14]
                        print(cpf)
                    fim = time.time()-inicio
                    fim =str(fim)
                    fim = fim[:4]
                    print(fim)

                    placa = f'''
==========Thor Bot=========

Placa: {api['VEICULO']['placa']}
Chassi: {api['VEICULO']['chassi']}
Renavam: {api['VEICULO']['renavam']}

ESPECIFICÕES:

Veiculo: {api['VEICULO']['veiculo'].title()}
Cor: {api['VEICULO']['cor']}
Tipo: {api['VEICULO']['tipo']}
Fabricção: {api['VEICULO']['fabric']}
Ano: {api['VEICULO']['ano']}

DADOS DO PROPRIETARIO:

Nome: {api['VEICULO']['nome'].title()}
Cpf: {cpf}

Endereço:

Cidade: {api['VEICULO']['cidade'].title().strip()}
UF: {api['VEICULO']['uf']}

Delay: {fim} '''
                    print(placa)
                    update.message.reply_text(placa)
                    
            except:
                update.message.reply_text(f'⚠️Ocorreu um erro ao tentar buscar a placa {p[1]}')
                print(exit)
def is_number(num):
    try:
        float(num)
        return True
    except:
        pass
    return False

def vizinho(update, context):
    import requests
    import json
    green = "\033[0;32m"
    default = "\033[0m"
    cpf = update.message.text[10:].strip()
    print(cpf)
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        resp = requests.get('https://tudosobretodos.info/'+cpf, headers=headers,
                        proxies=dict(http='socks5://94.103.88.24:1080',
                                    https='socks5://94.103.88.24:1080'))
        print(resp.text)
        soup = BeautifulSoup(resp.content)
        result = ''
        for i in soup.findAll('div', attrs={'class': 'itemMoradores'}):
            m = i.text
            # m.replace("\t", "").replace("\n", "")
            result+=(m.strip().title())
            result+='\n'
            # for i in result:
            #     print(ace("\ti.repl", "").replace("\n", ""))
        if len(result) < 2:
            update.message.reply_text('''Nada encontrado...''')
            print (green + "Não foi possível pegar os nomes dos vizinhos" + default)
        else:
            result.strip()
            result.replace("\t", "").replace("\n", "")
            print(result)
            update.message.reply_text(f'''
==========Thor Bot=========

CPF: {cpf}
Vizinhos encontrados:

{result}''')
    except:
        print('erro')
def cpf(update, context):
    import requests
    import json
    cpf = update.message.text[5:].strip()
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if(is_number(cpf) == 'False'):
        print(is_number(cpf))
        update.message.reply_text(''' 
==========Thor Bot=========

Consulte somente com números 
Exemplo: 
/cpf 00769610013 ou
/cpf 007.696.100-13

Caso esteja digitando corretamente consulte o meu criador: @killman1''')
    else:
        print(len(cpf))
        if(len(cpf) < 11 or len(cpf) > 11):
            print(len(cpf) < 11 or len(cpf) > 11)
            update.message.reply_text(''' 
==========Thor Bot=========

Cpf digitado menor ou maior que 12 digitos. Tente novamente!

Exemplo: 
/cpf 00769610013 ou
/cpf 007.696.100-13

Caso esteja digitando corretamente consulte o meu criador: @killman1''')
        else:
            try:
                requisicao = requests.get(f"https://thorconsultas.000webhostapp.com/?cpf={cpf}", timeout=(5, 60))
                cotacao = requisicao.json()
                a = cotacao
                print(cotacao)
                update.message.reply_text(f'''
======Consulta Realizada!======

CPF: {a['Dados']['CPF']}
Nome: {a['Dados']['Nome']}
Nome da Mãe: {a['Dados']['Mae']}
Nascimento: {a['Dados']['Nascimento']}

Endereço:

Logradouro: {a['Dados']['logradouro']}
Número: {a['Dados']['Numero']}
Complemento: {a['Dados']['Complemento']}
Cidade: {a['Dados']['Cidade']}
CEP: {a['Dados']['Cep']}
UF: {a['Dados']['Estado']}

Delay: {str(a['Dados']['Delay'])[:7]}''')
            except:
                update.message.reply_text('''Nada encontrado...''')
    
def erro(update, context):
    update.message.reply_text(f'Comando inexistente!')

def sorteio(update, context):
    entities = update.message.parse_entities()
    print(entities)





dispatcher = updater.dispatcher
dp = updater.dispatcher.add_handler
#dp(CommandHandler('online', online))
dp(CommandHandler('cpf', cpf))
dp(CommandHandler('vizinhos', vizinho))
dp(CommandHandler('comandos', comandos))
dp(CommandHandler('ip', ip))
dp(CommandHandler('sorteio', sorteio))
dp(CommandHandler('placa', placa))
dp(CommandHandler('cep', cep))
dp(MessageHandler(Filters.command, erro))
updater.start_polling()
updater.idle()