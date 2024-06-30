from  SOFTWARE  import *
from  threading  import  *
import  os  


def  s():
    cao_de_guarda1(root_dir, hash_file_path)

tred1=Thread(target=s ,daemon=True)

root_dir = '/home/sd/Transferências'
hash_file_path = 'virusHash.unibit'


print("""                             »»»»»»»  
                »»»»»»»»»HUNTER_STUDIO««««««»»»                         
                   »»»»»»»»»»»»»»»»»»»»»»»»»»                                                      
                      »»»»»»»»»»»»»»»»»»»»                             
                         »»»»»»»»»»»»»   """)
dados=0
while dados==0:
    comando=input('terminal⋊>:').strip()
    if comando== 'ransom/scanner/curto':
        
        ingição2()
    elif comando=='ransom/scanner/longo':
        ingição()
    elif   comando=="ransom/scanner/destruir":
        
        modo_agrecisso(root_dir,  hash_file_path)
    elif  comando =='ransom/guarda/ativo':
        tred1.start()









       
        
       

      
       
      


    

    
    
    
        



