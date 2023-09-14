import xml.etree.ElementTree as ET

def primeiro_exemplo():
    tree = ET.parse('dados.xml')  # Carrega o arquivo XML em uma estrutura de árvore
    root = tree.getroot()   

    # Acessar elementos e atributos
    elemento1 = root.find('elemento1')  # Encontra o elemento 'elemento1'
    atributo_valor = elemento1.get('atributo')  # Obtém o valor do atributo 'atributo'
    conteudo = elemento1.text  # Obtém o conteúdo do elemento 'elemento1'

    print("Elemento:", elemento1.tag)
    print("Atributo:", atributo_valor)
    print("Conteúdo:", conteudo)


def segundo_exemplo():
    tree = ET.parse('dados_exemplo.xml')
    root = tree.getroot()
    
    for pessoa in root:
        print(' ',pessoa.tag, pessoa.attrib['Nome'] )
        for dado in pessoa:
            print('\t', dado.tag, dado.text)

def terceiro_exemplo():
    tree = ET.parse('dados_pessoais3.xml')
    root = tree.getroot()
    for pessoa in root:
        print(' ', pessoa.tag, pessoa.attrib['Nome'])
        for dado in pessoa:
            if(dado.tag == 'Filhos'):
                for filho in dado:
                    print(' ', filho.tag, filho.attrib['nome'])
            else:
                print(' ',dado.tag, dado.text)
    
terceiro_exemplo()