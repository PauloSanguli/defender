import  json
from    pathlib import Path

carro=[]
carro.clear()
for x in range(50):
    carro.append(x)

carros=json.dumps(carro)
Path('res.json').write_text(carros)




