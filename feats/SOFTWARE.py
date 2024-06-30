import  json
from hashlib import *
import hashlib

import os
from  time   import  *
from    pathlib import Path
from   threading import  *



# root_dir = '/home/sd/Documentos/Livros'
hash_file_path = 'virusHash.unibit'

PATH = os.path.dirname(os.path.abspath(__file__))
hash_malware=list(open(f'{PATH}\\virusHash.unibit','r').read().split('\n'))
inf_malware=list(open(f'{PATH}\\virusInfo.unibit').read().split('\n'))
def transformar_hash(arquivo):
    with open(arquivo,"rb") as file:
        bytes=file.read()
        SHA256=sha256(bytes).hexdigest()

    return SHA256

virus=[]
def verifcar_ransomware(file):
    arquivo_hash=transformar_hash(file)
    global hash_malware
    global inf_malware
    counter=0

    for  i in  hash_malware:
        if i ==arquivo_hash:
           
            return inf_malware[counter]
        counter +=1
    return 0
virusTOTAL=[]

def scanner_pasta(path='/home/sd/Documentos/HunterStudio'):
  dir_list=os.listdir(path)
  arquivo=""
  for i in  dir_list:
      arquivo=path+"//"+i
      if verifcar_ransomware(arquivo) !=0:
           virusTOTAL.append(verifcar_ransomware(arquivo)+f'arquivo_malicioso:'+i)
          
          
      
def  ler_tudo():
    dir_list=list()
    for(dirpath,dir_nome, arq_nome) in os.walk('/home/sd/Transferências'):
        dir_list+=[os.path.join(dirpath,file)for file in  arq_nome]

       


    
    for i in  dir_list:


        
        if verifcar_ransomware(i) !=0:
               
                   
               
               virusTOTAL.append(verifcar_ransomware(i)+f'a(rquivo_malicioso:'+i)


def pegar_arquivo(file_path, hash_function='sha256'):
    
    hash_func = hashlib.new(hash_function)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def modo_agrecisso(root_dir):
    lista=[]
    lista1=[]
    
    hash_file_path = f'{PATH}\\virusHash.unibit'




    with open(hash_file_path, 'r') as hash_file:
        hash_set = {line.strip() for line in hash_file}
    
    
    for dirpath, dirnames, filenames in os.walk(root_dir):

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            lista1.append(file_path)



            
            try:
                
                file_hash = pegar_arquivo(file_path)
               
                if file_hash in hash_set:
                    os.remove(file_path)
                    #print(f" arquivo destruido: {file_path}")
                    lista.append(file_path)


            except Exception as e:
                print(f"erro  em  buscar resposta {file_path}: {e}")
            dados0=json.dumps(lista1)
            dados1 = json.dumps(lista)
            Path('feats/res.json').write_text(dados0)
            Path('feats/delatados.json').write_text(dados1)




def transformar_hash(file_path, hash_function='sha256'):
    
    hash_func = hashlib.new(hash_function)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def load_hashes(hash_file_path):
   
    with open(hash_file_path, 'r') as hash_file:
        return {line.strip() for line in hash_file}

def delatar_arquivo_no_scanner(root_dir, hash_set):
    delatados=[]
    


    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
         
                
               

            try:

                
                file_hash = transformar_hash(file_path)
                
                if file_hash in hash_set:
                    os.remove(file_path)
                    #print(f"arquivo malicioso  deletado : {file_path}")
                    delatados.append(file_path)
    
  
                

                   
                        
            except Exception as e:
                print(f"erro    {file_path}: {e}")
    dados1 = json.dumps(delatados)
    Path('feats/delatados.json').write_text(dados1)

def cao_de_guarda1(root_dir, hash_file_path, interval=20):
    while True:
        hash_set = load_hashes(hash_file_path)
        delatar_arquivo_no_scanner(root_dir, hash_set)



def ingição():
   
       ler_tudo()
       print(virusTOTAL)
    
      
def ingição2():
    scanner_pasta()
    print(virusTOTAL)




def scanner_geral():
    root='C:\\Users\\Paulo Sanguli\\Documents\\Projects\\defender-app\\assets'
    modo_agrecisso(root)
root='C:\\Users\\Paulo Sanguli\\Documents\\Projects\\defender-app\\assets'
# scanner_geral()
    







 














    



        
