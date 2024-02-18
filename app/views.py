from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
import logging

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def consulta(request):
    resultado_cep = None
    cep_digitado = None
    
    if request.method == 'POST':
        # Obtenha o CEP digitado pelo usuário a partir do formulário
        cep_digitado = request.POST.get('cep')
        
        # Lógica para processar a consulta de CEP aqui
        # Suponha que você tenha o resultado da consulta em uma variável chamada 'resultado_cep'
        resultado_cep = cep_digitado  # Agora o resultado é o próprio CEP digitado pelo usuário
   
    if cep_digitado:
            logging.info("Definindo trust_env como False")
            session = requests.Session()
            session.trust_env = False
            logging.info("Iniciando chamada para a API")
            url = f'https://viacep.com.br/ws/{cep_digitado}/json/'
            logging.info("API definida")
            response = requests.get(url)
            logging.info("Chamada para a API concluída")
            
            # Verifique se a resposta foi bem sucedida (código de status 200)
            if response.status_code == 200:
                logging.info("Chamada para a API concluída com sucesso (200)")
                # Converta a resposta para JSON
                data = response.json()
                logging.info("Valores do CEP salvos")
                
                # Extraia os dados relevantes do CEP (por exemplo, rua, bairro, cidade, estado)
                resultado_cep = {
                    'rua': data.get('logradouro'),
                    'bairro': data.get('bairro'),
                    'cidade': data.get('localidade'),
                    'estado': data.get('uf'),
                }
                logging.info("Valores do CEP a serem utilizados determinados")

    return render(request, 'app/consulta.html', {'resultado_cep': resultado_cep, 'cep_digitado': cep_digitado})

def test_connection(request):
    try:
        # Faça uma solicitação HTTP a um serviço externo para testar a conectividade
        response = requests.get('https://api.example.com')

        # Verifique se a resposta foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            return HttpResponse('Conexão bem-sucedida')
        else:
            return HttpResponse('Erro de conexão: {}'.format(response.status_code))
    except Exception as e:
        # Trate exceções que possam ocorrer durante a solicitação
        return HttpResponse('Erro de conexão: {}'.format(str(e)))