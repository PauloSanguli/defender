import  requests 



def verificar_malware_totalvirus(arquivo_path, api_key):
   
    url = 'https://api.totalvirus.com/v1/file/report'

   
    params = {
        'apikey': api_key,
        'resource': arquivo_path
    }

    
    response = requests.get(url, params=params)

    
    if response.status_code == 200:
       
        data = response.json()

        
        if 'results' in data:
            # Retorna o resultado da análise
            return data['results']['positives'] > 0
        else:
            print("Arquivo não encontrado no TotalVirus.")
            return False
    else:
        print("Erro ao se conectar ao TotalVirus.")
        return False


def verificar_arquivo_malware(arquivo_path):
   
    api_key = 'sua_api_key_do_TotalVirus'

    
    resultado = verificar_malware_totalvirus(arquivo_path, api_key)

    if resultado:
        print("O arquivo é um malware.")
    else:
        print("O arquivo não é um malware.")
        


arquivo_path = 'caminho/do/arquivo.exe'
verificar_arquivo_malware(arquivo_path)
