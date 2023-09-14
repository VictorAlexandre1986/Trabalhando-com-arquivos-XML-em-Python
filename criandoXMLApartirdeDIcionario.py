import xml.etree.ElementTree as xml
import os


def criaTagPessoa(nome,cpf,sexo,endereco):
    
    no_pessoa = xml.Element("Pessoa", attrib={"Nome":nome})

    no_cpf = xml.SubElement(no_pessoa, "cpf")
    no_cpf.text = cpf

    no_sexo = xml.SubElement(no_pessoa, "sexo")
    no_sexo.text = sexo

    no_endereco = xml.SubElement(no_pessoa, "endereco")
    no_endereco.text = endereco
    
    return no_pessoa


dados={
    'Victor':{
        'cpf':'123456789',
        'sexo': 'masculino',
        'endereco':'casa 345'
    },
    'Beltrano':{
        'cpf':'987654321',
        'sexo':'masculino',
        'endereco':'rua xpto nº0',
        'filhos':["Rodrigo", "Lucas"]
    }
}

raiz = xml.Element("Pessoais")

for key in dados:
    nome=key
    dados_pessoa = dados[nome]
    cpf = dados_pessoa['cpf']
    sexo = dados_pessoa['sexo']
    endereco = dados_pessoa['endereco']
    pessoa =criaTagPessoa(nome, cpf, sexo, endereco)
    if 'filhos' in dados_pessoa:
        filhos = xml.SubElement(pessoa,'Filhos')
        for filho in dados_pessoa['filhos']:
            pessoa_filho = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})
            
    raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais3.xml','wb') as files:
    arvore.write(files)