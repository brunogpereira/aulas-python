from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    ''' 
    
    Endpoint com a mensagem mais incrível do mundo
    
    '''
    return {'Hello':'World'}

@app.get('/api/restaurante/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    
    Endpoint para ver os cardapios dos restaurantes
    
    '''
    
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_do_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_do_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description'] 
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_do_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}
