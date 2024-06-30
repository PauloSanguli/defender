import os
import subprocess
import tempfile
from datetime import datetime


import platform
if platform.system() == 'Windows':
    import win32api


def e_pendrive(dev):
    if platform.system() == 'Linux':
        return dev.get('ID_BUS') == 'usb' and dev.get('SUBSYSTEM') == 'block'
    elif platform.system() == 'Windows':
        return win32api.GetDriveType(dev) == win32api.DRIVE_REMOVABLE

# Função para escrever os detalhes da inserção do pendrive em um arquivo de log
def registrar_insercao_pendrive(dispositivo):
    with open("registro_pendrives.txt", 'a') as f:
        f.write(f"{'='*40}\n")
        f.write(f"Data e hora de inserção: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Nome do dispositivo: {dispositivo}\n")
        f.write(f"{'='*40}\n\n")

#
def monitorar_pendrives():
    if platform.system() == 'Linux':
       
        import pyudev
        
        
        contexto = pyudev.Context()

        
        monitor = pyudev.Monitor.from_netlink(contexto)
        monitor.filter_by(subsystem='block')

        print("Aguardando a detecção do pendrive...")

        
        for acao, dispositivo in monitor:
            if acao == 'add' and e_pendrive(dispositivo):
                print("Pendrive detectado:", dispositivo.device_node)
                
                # Registra a inserção do pendrive em um arquivo de log
                registrar_insercao_pendrive(dispositivo.device_node)
                
                # Monta o dispositivo em um diretório temporário
                diretorio_montado = tempfile.mkdtemp(prefix='pendrive_')
                subprocess.run(['sudo', 'mount', dispositivo.device_node, diretorio_montado])
                
                # Lista os arquivos no pendrive
                arquivos = os.listdir(diretorio_montado)
                print("Arquivos no pendrive:", arquivos)
                
               
            
                subprocess.run(['sudo', 'umount', diretorio_montado])
                os.rmdir(diretorio_montado)  
    elif platform.system() == 'Windows':
        print("Aguardando a detecção do pendrive...")


        drives_anteriores = []
        while True:
            drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]
            novos_drives = [drive for drive in drives if drive not in drives_anteriores]
            drives_anteriores = drives

            for novo_drive in novos_drives:

                registrar_insercao_pendrive(novo_drive)

     
     
if __name__ == "__main__":
    monitorar_pendrives()


