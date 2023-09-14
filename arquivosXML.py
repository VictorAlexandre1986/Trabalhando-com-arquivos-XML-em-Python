import xml.etree.ElementTree as xml
import os

def criarXML():
    no_raiz = xml.Element("Dados Pessoais")
    no_pessoa = xml.Element("Pessoa", attrib={"Nome":"Victor"})

    no_cpf = xml.SubElement(no_pessoa, "cpf")
    no_cpf.text = "123456789"

    no_sexo = xml.SubElement(no_pessoa, "sexo")
    no_sexo.text = "Masculino"

    no_endereco = xml.SubElement(no_pessoa, "endereco")
    no_endereco.text = "Dom Pedro II"

    #Add elemento pessoa no nó raiz
    no_raiz.append(no_pessoa)

    #Criando a arvore do objeto raiz
    arvore = xml.ElementTree(no_raiz)

    with open('dados_exemplo.xml', 'wb') as files:
        arvore.write(files)
    

def criaTagPessoa(nome,cpf,sexo,endereco):
    
    no_pessoa = xml.Element("Pessoa", attrib={"Nome":nome})

    no_cpf = xml.SubElement(no_pessoa, "cpf")
    no_cpf.text = cpf

    no_sexo = xml.SubElement(no_pessoa, "sexo")
    no_sexo.text = sexo

    no_endereco = xml.SubElement(no_pessoa, "endereco")
    no_endereco.text = endereco
    
    return no_pessoa

raiz = xml.Element("DadosPessoais")

pessoa1 = criaTagPessoa("Victor","33025825841","Masculino","Dom Pedro I")
pessoa2 = criaTagPessoa("Xispita","33025825842","Feminino","Dom Pedro I")

raiz.append(pessoa1)
raiz.append(pessoa2)

arvore = xml.ElementTree(raiz)

with open('dados_exemplo2.xml', 'wb') as files:
    arvore.write(files) 
    
if __name__=='__main__':
    criarXML()