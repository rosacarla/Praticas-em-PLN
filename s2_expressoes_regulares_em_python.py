# -*- coding: utf-8 -*-
"""S2-Expressoes-regulares-em-Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p8qdpZ0THPxi32qaUQpubBSx2-sydNtW

># <b>Expressões Regulares em Python</b>
> Instituição: PUCPR  
> Curso: Tecnologia em Inteligência Artificial Aplicada  
> Disciplina: Processamento de Linguagem Natural  
> Professor: Lucas Emanuel Silva e Olveira  
> Estudante: Carla Edila Silveira  

> <p align='justify'> Objetivo: Nesta atividade, você entrará em contato com <b>Expressões Regulares (RegEx)</b>, talvez a mais importante ferramenta de PLN para descrever/encontrar/substituir padrões de texto. Após esta atividade você será capaz de ler uma expressão regular como essa <i>^[0-9]{1,3}(\.[0-9]{1,3}){1,3}$</i>, como você lê um texto em português.</p>

##**Expressões Regulares - RegEx**  

<p align='justify'> Você poderá fazer uso de expressões regulares nas mais diversas situações em que precise localizar ou extrair padrões em meio ao texto (e.g., <i>encontrar CEPs de endereço no texto, obter os preços de produtos de uma listagem</i>). Você pode usar expressões regulares em linguagens de programação e editores de texto por exemplo.</p>

### **Por onde começar?**

#### 1) Importar a biblioteca de RegEx do Python
"""

import re

"""#### 2) Escrever uma expressão regular para capturar um padrão desejado

"""

# Você deve colocar a letra "r" antes do texto para estabelecer que a variável guarda uma RegEx
padrao = r"clássico"

"""####3) Definir para qual funcionalidade o padrão RegEx será utilizado
Você pode usar um padrão para:
*   Buscar padrões/valores no texto (i.e., `search`, `match`, `findall`)
*   Quebrar texto em sub-textos (i.e., `split`)
*   Substituir dados no texto (i.e., `sub`)


"""

# Texto de exemplo para verificar se o padrão definido acima é encontrado
texto = "clássico é clássico e vice-versa"

# A função search() retorna um objeto, caso encontre o padrão no texto
if re.search(padrao, texto):
  print("Encontrou")
else:
  print("Não encontrou")

# Faça alterações no texto e no padrão. Reexecute o código.

"""### **Quais funções da biblioteca `re` posso utilizar?**
*   `re.match(padrao, texto)`
*   `re.search(padrao, texto)`
*   `re.findall(padrao, texto)`
*   `re.split(padrao, texto)`
*   `re.sub(padrao, texto)`

#### **`re.match()`**
Encontra o padrão desejado se ele ocorrer no **início do texto**
"""

match = re.match(r"clássico", "clássico é clássico e vice-versa")
# Mostra o objeto/match da busca, caso não encontre o padrão retorna None
match

# Caso queira mostrar o trecho de texto encontrado, usar a função group()
# match.group()

# Caso queira obter a posição de início e fim do texto encontrado
# match.start()
# match.end()

"""#### **`re.search()`**
Similar ao `match()`, porém busca pelo padrão em qualquer parte do texto, não se restringindo ao início do mesmo.
"""

match = re.search(r"clássico", "clássico é clássico e vice-versa")
# Mostra o objeto/match da busca, caso não encontre o padrão retorna None
match

"""> *Mas porque a saída é igual ao código anterior?*

<p align='justify'>Apesar da função <b>search( )</b> procurar o padrão em qualquer parte do texto, ela retorna apenas a primeira ocorrência. A seguir uma comparação de <b>match( )</b> e <b>search( )</b>.</p>
"""

m = re.match(r"teste", "Este é um teste de regex.")
print(m)

s = re.search(r"teste", "Este é um teste de regex.")
print(s)

"""#### **`re.findall()`**
Funcionamento similar ao `search()`, porém retorna TODAS as ocorrências encontradas.
"""

match = re.findall(r"clássico", "clássico é clássico e vice-versa")
match

m = re.findall(r"teste", "Este não é apenas mais um teste de regex. Este teste mostra como funciona o findall()")
m

"""#### **`re.split()`**
Divide o texto toda vez que encontrar a ocorrência do padrão dado
"""

partes = re.split(r"/", "10/05/1999")
partes

partes = re.split(r"a", "a história das expressões regulares")
partes

"""#### **`re.sub()`**
Busca pelo padrão desejado e o substitui por um texto desejado
"""

r = re.sub(r"nossa universidade", "PUCPR", "A nossa universidade lhe dá as boas-vindas!")
r

r = re.sub(r"gato", "cachorro", "Este é meu gato Thomas. Eu adoro ter um gato em casa.")
r

"""###**Como escrever padrões mais complexos?**  

<p align='justify'> Agora que você sabe utilizar as principais funções da biblioteca <b>re</b>, podemos criar padrões de busca mais complexos e poderosos. Existe uma série de caracteres especiais que podem lhe ajudar a construir os padrões de texto desejados. Não é preciso decorá-los, apenas saber como utilizá-los. A seguir uma tabela de referência com vários destes caracteres. </p>  
</br>

![Caracteres especiais das Expressões Regulares](https://docs.google.com/uc?export=download&id=1wK1aO8y_J7q79Mh4bQ_gzczDkEj4pLCQ)

> <p align='justify'> <b>DICA IMPORTANTE</b>: Você também pode testar as expressões regulares a seguir no site [Pythex](https://pythex.org/), que tem uma interface bem interessante para visualizar e testar suas expressões regulares.</p>

#### Groups & Ranges
Os **colchetes** indicam um **RANGE** de caracteres que podem fazer parte do padrão.
> Por exemplo, para encontrar todas vogais no texto: `[aeiou]`
"""

re.findall(r"[aeiou]", "Sentença para obter vogais.")

"""**`[0-9]`** - Obtém todos números"""

re.findall(r"[0-9]", "Hoje, dia 26/11/2019 o dólar alcançou o valor de R$ 4,20 perante o real.")

"""**`[a-z]`** - Obtém todos números

"""

re.findall(r"[A-Z]", "AFV-5631")

"""Os **parênteses** indicam um **GRUPO** de caracteres que podem fazer parte do padrão. Podemos juntar a eles outros caracteres especiais.

**`|`** - Indica o operador lógico OU
"""

# Busca Lucas OU Rodrigo
re.findall(r"(Lucas|Rodrigo)", "Lucas Oliveira\nMurilo Silva\nDiego Prudêncio\nRodrigo Rezende")

"""**`^`** - Indica operador lógico NÃO"""

# Busca tudo, exceto letras minúsculas
re.findall(r"[^a-z]", "Lucas Oliveira\nMurilo Silva\nDiego Prudêncio\nRodrigo Rezende")

"""**`.`** - Indica QUALQUER caracter, exceto quebra de linha (`\n`)"""

# Busca toda ocorrencia de "ato" e o caracter anterior
re.findall(r".ato", "O rato é amigo do pato que presenciou o ato no meio do mato.")

"""#### Classes de caracteres

**`\s`** - Obtém todos espaços (white-space)

**`\S`** - Obtém todos NÃO espaços (white-space)
"""

re.findall(r"\s", "Conseguimos pegar o que não é espaço?")

re.findall(r"\S", "Conseguimos pegar o que não é espaço?")

"""#### Âncoras

**`^`** - Indica início de texto
"""

# Faz match apenas se a palavra clássico estiver no início do texto
match = re.findall(r"^clássico", "clássico é clássico e vice-versa")
match

# Faz match apenas se a palavra clássico estiver no início do texto
match = re.findall(r"^clássico", "Este jogo é um clássico")
match

"""**`$`** - Indica fim de texto"""

# Faz match apenas se a palavra clássico estiver no fim do texto
match = re.findall(r"clássico$", "Este jogo é um clássico")
match

# Faz match apenas se a palavra clássico estiver no fim do texto
match = re.findall(r"clássico$", "clássico é clássico e vice-versa")
match

"""#### Quantificadores
Em alguns momentos pode ser preciso quantificar a quantidade de vezes que um determinado padrão aparece.
"""

# Padrão que encontra dois números em sequencia ou par de dígitos consecutivos
match = re.findall(r"[0-9]{2}", "João tem 5 laranjas, enquanto Maria tem 25.")
match

# Padrão que encontra de um a cinco números em sequencia
match = re.findall(r"[0-9]{1,5}", "João tem 5 laranjas, enquanto Maria tem 25. Já Henrique possui 10000.")
match

# Padrão que encontra um ou mais numeros em sequencia
match = re.findall(r"[0-9]{1,}", "João tem 5 laranjas, enquanto Maria tem 25. Já Henrique possui 10000.")
match

"""**`*`** - Zero ou mais ocorrências"""

# Padrão que encontra sequência de letras, seguida por zero ou mais caracteres 'x', e então outra sequência de letras
match = re.findall(r"[a-zA-Z]{1,} x* [a-zA-Z]{1,}", "Vasco x Palmeiras - Corinthians x Santos - Portuguesa xxx Guarani")
match

"""**`+`** - Uma ou mais ocorrências"""

# Padrão que encontra um ou mais numeros em sequencia
match = re.findall(r"[0-9]+", "João tem 5 laranjas, enquanto Maria tem 25. Já Henrique possui 10000.")
match

"""**`?`** - Zero ou uma ocorrência"""

# Padrão que encontra 9 numeros, seguidos ou não por um hífen, seguidos de dois números
match = re.findall(r"[0-9]{9}-?[0-9]{2}", "RG: 8122691-8 CPF: 064555874-90 / RG: 81623338 CPF: 06454357320 ")
match

"""### **Exemplo do e-mail**
Vamos fazer uma expressão regular para obter endereços de e-mail no texto
"""

texto = "Lucas Oliveira: lucas.oliveira@pucpr.br \n maria-silva@gmail.com \n jobs@apple.com "
texto

re.findall(r"[a-z]+", texto)

re.findall(r"[a-z]+@[a-z]+", texto)

"""O padrão acima obtém as letras, porém, ignora o hífen e o ponto final. Para resolver podemos criar um RANGE adicionando estes caracteres."""

re.findall(r"[a-z-]+@[a-z-]+", texto)

re.findall(r"[a-z-.]+@[a-z-.]+", texto)

"""> <p align='justify'> <b>DICA</b>: Você pode realizar o que chamamos de <b>EXTRAÇÃO DE GRUPO</b> usando as expressões regulares. Basta agrupar os sub-padrões que deseja extrair separadamente com os parênteses.</p>"""

re.findall(r"([a-z-.]+)@([a-z-.]+)", texto)

"""Digamos que você queira remover todos os e-mails do texto por questões de privacidade."""

re.sub(r"[a-z-.]+@[a-z-.]+", "-CONFIDENCIAL-", texto)

"""É possível ainda utilizar os agrupamentos para efetuar substituições mais complexas.

Por exemplo, imagine que queiramos apenas substituir o servidor de e-mail, mas mantendo o nome de usuário.
"""

# Nesse caso podemos usar os agrupamentos da expressão regular
# \1 indica a informação obtida no primeiro agrupamento - neste caso o nome do usuário
# \2 indica a informação obtida no segundo agrupamento - neste caso o servidor do e-mail
re.sub(r"([a-z-.]+)@([a-z-.]+)", r"\1@regex.com", texto)

""">  <p align='justify'> <b>IMPORTANTE</b>: E quando eu quero procurar algum caractere que já representa algo em expressões regulares? (e.g., ponto final, interrogação)</b>

Nesse caso, podemos usar o que chamamos de **CARACTER DE ESCAPE**, representado pelo caracter **`\`**

Exemplo: Quero obter todas perguntas presentes em um texto
"""

texto = """Este é um texto de exemplo.
Mas será que ele é confiável?
Além dos questionamentos acima há outras questões a serem levantadas.
Você está gostando de aprender expressões regulares?
PLN é uma área de seu interesse?"""

# Obtém qualquer sequencia de caracteres (exceto quebra de linha)
re.findall(r".+", texto)

# Gostaríamos de pegar toda sequencia, seguida de uma ponto de interrogação
re.findall(r".+?", texto)

""" <p align='justify'> Neste caso, o ponto de interrogação é considerado um quantificador de Expressão Regular, portanto, é interpretado como tal. Para fazermos com que ele seja interpretado como um caracter comum, usamos o escape `\`</p>"""

re.findall(r".+\?", texto)

"""##**ATIVIDADE PRÁTICA**
Atividades de fixação no uso de Expressões Regulares

### 1) Obtenha todas palavras do texto
"""

texto = "Um texto qualquer sem qualquer valor semântico."
palavras = re.findall(r'\b\w+\b', texto)

print(palavras)

"""### 2) Obtenha a primeira palavra do texto"""

texto = "Um texto qualquer sem qualquer valor semântico."
primeira_palavra = re.findall(r'\b\w+\b', texto)[0]

print(primeira_palavra)

"""### 3) Obtenha a posição de início do primeiro espaço (white-space) encontrado no texto a seguir"""

texto = "Um texto qualquer sem qualquer valor semântico."
match = re.search(r'\s', texto)

if match:
    posicao_primeiro_espaco = match.start()
    print(posicao_primeiro_espaco)

"""### 4) Obtenha os dois primeiros caracteres de cada palavra
Dica: Pesquise sobre o caracter de word boundary `\b`, que encontra as delimitações de cada palavra
"""

import re

texto = "Um texto qualquer sem qualquer valor semântico."
dois_primeiros_caracteres = re.findall(r'\b\w{1,2}\b', texto)

print(dois_primeiros_caracteres)

"""### 5) Obtenha datas no formato brasileiro (dd/mm/aaaa) e americano (aaaa-mm-dd)"""

texto = "Data: 27/02/1987. Date: 1987-02-27."

# Busca datas no formato brasileiro (dd/mm/aaaa)
datas_brasileiras = re.findall(r'\b(\d{2})/(\d{2})/(\d{4})\b', texto)

# Busca datas no formato americano (aaaa-mm-dd)
datas_americanas = re.findall(r'\b(\d{4})-(\d{2})-(\d{2})\b', texto)

print("Datas no formato brasileiro:", datas_brasileiras)
print("Datas no formato americano:", datas_americanas)

texto = "Data: 27/02/1987. Date: 1987-02-27."
re.findall(r"([0-9]{2}/[0-9]{2}/[0-9]{4})|([0-9]{4}-[0-9]{2}-[0-9]{2})", texto)

"""### 6) Obtenha todas palavras que terminem com vogal"""

texto = "Um texto qualquer sem qualquer valor semântico."
palavras_terminadas_com_vogal = re.findall(r'\b\w*[aeiouAEIOU]\b', texto)

print(palavras_terminadas_com_vogal)

"""### 7) Substitua toda ocorrência da palavra "Avenida" por "Av."

"""

texto = "Endereço: Avenida Getúlio Vargas, 1811\nEndereço: avenida visconde de guarapuava, 1533"

novo_texto = re.sub(r'\bAvenida\b', 'Av.', texto)

print(novo_texto)

"""###8) Obtenha os endereços sem a numeração"""

texto = "Endereço: Avenida Getúlio Vargas, 1811\nEndereço: avenida visconde de guarapuava, 1533"
# Remover números e vírgula após a vírgula
enderecos_sem_numeracao = re.sub(r',\s*\d+', '', texto)

print(enderecos_sem_numeracao)

"""### 9) Substitua todas ocorrências de espaços, vírgulas e pontos pelo underline"""

text = 'Python Exercises, PHP exercises.'

text_substituted = re.sub(r'[ ,.]', '_', text)

print(text_substituted)

"""O gabarito das atividades pode ser encontrado [aqui](https://colab.research.google.com/drive/1zsWPZyAPuXscBjbd2yu12zg4-tG0eHR8).

## Referências e Material complementar


*   [RegEx Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)
*   [Tutorial sobre expressões regulares para iniciantes em Python](https://www.vooo.pro/insights/tutorial-sobre-expressoes-regulares-para-iniciantes-em-python/)
*   [Python Regular Expressions by Google](https://developers.google.com/edu/python/regular-expressions)
*   [Python ReGex Exercises](https://www.w3resource.com/python-exercises/re/)

Este notebook foi produzido por Prof. [Lucas Oliveira](http://lattes.cnpq.br/3611246009892500) e revisado por Carla Silveira.
"""