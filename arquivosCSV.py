import csv

def gerarCSV():
    with open('arquivo.csv','w') as arquivo:
        escritorCSV = csv.writer(arquivo, delimiter=',')
        escritorCSV.writerow(["id","nome","profissao"])
        escritorCSV.writerow(['1','Victor','desenvolvedor'])
        escritorCSV.writerow(['2','Ciclano','Eng de dados'])
        escritorCSV.writerow(['3','Beltrano','Cientista de dados'])
    
    
def gerarCSV2():
    
    lista = [['id','nome','profissao'],[1,'victor','desenvolvedor'],
             [2,'ciclano','engenheiro de dados'],['3','beltrano','cientista de dados']]
    
    with open("arquivo2.csv", "a") as arq:
        escritorCSV = csv.writer(arq, delimiter=',')
        escritorCSV.writerows(lista)
        
def leitorCSV():
    with open('arquivo.csv','r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            print(linha)

if __name__=='__main__':
    leitorCSV()
