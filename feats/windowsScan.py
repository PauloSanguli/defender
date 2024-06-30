
import os
import subprocess
import tempfile
import win32api
import win32file
import win32con
from hashlib import sha256

def verificar_pendrives(toReturn=False):
    # Carrega os hashes e informações do malware a partir dos arquivos
    PATH = os.path.dirname(os.path.abspath(__file__))
    hash_malware = list(open(f'{PATH}\\virusHash.unibit', 'r').read().split('\n'))
    inf_malware = list(open(f'{PATH}\\virusInfo.unibit', 'r').read().split('\n'))

    
    def calcular_hash(arquivo):
        with open(arquivo, "rb") as file:
            bytes = file.read()
            return sha256(bytes).hexdigest()

    def verificar_ransomware(arquivo):
        arquivo_hash = calcular_hash(arquivo)
        for i, hash_mal in enumerate(hash_malware):
            if hash_mal == arquivo_hash:
                return inf_malware[i] + f'arquivo_malicioso: {os.path.basename(arquivo)}'
        return None

    
    def ler_tudo(diretorio):
        virus_total = []
        for dirpath, _, arq_nome in os.walk(diretorio):
            for arquivo_nome in arq_nome:
                arquivo_path = os.path.join(dirpath, arquivo_nome)
                if verificar_ransomware(arquivo_path):
                    virus_total.append(verificar_ransomware(arquivo_path) + f'arquivo_malicioso: {arquivo_path}')
        return virus_total

   
   
    def detectar_insercao():
        drives = []
        bitmask = win32file.GetLogicalDrives()
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            mask = 1 << (ord(letter) - 65)
            if bitmask & mask:
                drive_type = win32file.GetDriveType(letter + ':\\')
                if drive_type == win32file.DRIVE_REMOVABLE:
                    drives.append(letter + ':\\')
        return drives

   
    pendrives = detectar_insercao()
    if toReturn:
        if not pendrives: return False
        return True 
    if pendrives:
        for pendrive in pendrives:
           # print("Pendrive detectado:", pendrive)
            virus_total = ler_tudo(pendrive)
            if virus_total:
               # print("Vírus encontrados no pendrive:")
                for info in virus_total:
                    print(info)
            else:
                
                print("Nenhum vírus encontrado no pendrive.")
    else:
        print("Nenhum pendrive detectado.")


verificar_pendrives()
