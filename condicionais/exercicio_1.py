import json
import urllib.request

# Solicitar ao usuário o CEP
cep = input('Digite o CEP: ')

# construir na URL de consulta
url = f"https://viacep.com.br/ws{cep}/jeson/"

try:
    # fazer a requisição
    response = urllib. request.urlopen(url)

    # ler o conteudo da resposta
    data= response.read() .decode('utf-8')

    # converter JSON em dicionário Python 
    endereco = json.loads(data)

    # Verificar se a consulta foi bem-sucedida
    if endereco.get('erro'):
        print('CEP não encontrado')
    else:
        # Armazenar informações em variáveis
        logradouro = endereco['logradouro']
        complemento = endereco['complemento']
        bairro = endereco['bairro']
        cidade = endereco['localidade']
        estado = endereco['uf']          

        # Exibir informações do endereço na tela
        print(f"Logradouro: {logradouro}")
        print(F"Complemento: {complemento}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

        # Fechar a conexão
        response.close()
except Exception as e:
    print(f"Erro: {e}")