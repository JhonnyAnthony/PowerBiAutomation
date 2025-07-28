import requests
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv,find_dotenv
import logging
class Automate():
    def __init__(self, **kwargs):
        
        load_dotenv(find_dotenv())
        # Informações do aplicativo registrado
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.tenant_id = kwargs.get('tenant_id')

        # IDs do workspace e dataset
        self.group_id = kwargs.get('workspace_id')
        self.dataset_id = kwargs.get('dataset_id')

    def getToken(self):
        # Autenticação
        credential = ClientSecretCredential(self.tenant_id, self.client_id, self.client_secret)
        token = credential.get_token("https://analysis.windows.net/powerbi/api/.default").token
        logging.info('Token de autenticação obtido com sucesso.')
        return token
    
    def Authorization(self):
        # Cabeçalhos da requisição
        token = self.getToken()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        logging.info('Cabeçalhos de autorização configurados com sucesso.') 
        return headers
    
    def refreshDataset(self):
        headers = self.Authorization()
        # URL da API para atualizar o dataset
        url = f'https://api.powerbi.com/v1.0/myorg/groups/{self.group_id}/datasets/{self.dataset_id}/refreshes'

        # Requisição de atualização
        response = requests.post(url, headers=headers)
        logging.info('Requisição de atualização enviada com sucesso.')
        # Verificar resultado
        if response.status_code == 202:
            logging.info("Atualização iniciada com sucesso!")
        else:
            logging.error(f"Erro ao iniciar atualização: {response.status_code}")
            print(response.content)

    def run(self):
        # Executa o processo de atualização do dataset
        logging.info("Iniciando atualização do dataset...")
        self.refreshDataset()
        logging.info("Processo concluído.")
