# -*- coding: utf-8 -*-
"""S5-pln-gerador-de-resumos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n0g94npr3zeBvZPP5BWIXbVYvI33RIww

> # GERADOR DE RESUMOS DE TEXTOS COM PYTHON  
> Autora: Carla Edila Silveira  
> Descrição: programa desenvolvido com a biblioteca `sumy` de NLP do Python para gerar resumos de textos; este é um exemplo simples de como você pode ser feita a aplicação.  
> Data: 07/05/2024
>
> <img src='https://i.postimg.cc/FHdXdLZC/ai-content-generators.png'>  
> Crédito da imagem: [Hardware.com.br](https://www.hardware.com.br/artigos/5-ferramentas-de-ia-que-voce-pode-usar-para-resumir-textos/)
"""

# Instala a biblioteca sumy
# Fornece várias estratégias de sumarização e tem suporte para vários idiomas
!pip install sumy

# Importa pacotes necessários da biblioteca sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

import nltk
nltk.download('punkt')

# Define funcao para gerar resumo
def generate_summary(text, sentences_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # parser = PlaintextParser.from_string(text, Tokenizer("portuguese"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)

# Exemplo de utilizacao da funcao
# Será resumido um capítulo de artigo disponivel em: https://www.scielo.br/j/ea/a/c4sqqrthGMS3ngdBhGWtKhh/
if __name__ == "__main__":
    texto = """
    O que vem a ser IA?
Sempre que ocorre um entusiasmo com os resultados de uma tecnologia, existe uma tendência da mídia em fornecer definições e explicações, por vezes não muito precisas, dos seus principais aspectos. Isso é, certamente, o que ocorre com a IA nos dias de hoje.

Em primeiro lugar, cabe ressaltar que não existe uma definição acadêmica, propriamente dita, do que vem a ser IA. Trata-se certamente de um ramo da ciência/engenharia da computação, e portanto visa desenvolver sistemas computacionais que solucionam problemas. Para tal, utiliza um número diverso de técnicas e modelos, dependendo dos problemas abordados. Portanto, é inadequado utilizar-se expressões como “a IA da empresa X”; mais adequado (porém com menos apelo) seria dizer “um sistema da empresa X que utiliza técnicas de IA”.

Ao invés de tentar fornecer uma definição de IA, mais adequado seria tentar caracterizar quais são os objetivos da área. Uma das primeiras tentativas desta abordagem, proposta em Rich e Knight (1991), é a seguinte: o objetivo da IA é desenvolver sistemas para realizar tarefas que, no momento: (i) são mais bem realizadas por seres humanos que por máquinas, ou (ii) não possuem solução algorítmica viável pela computação convencional.

Para entender melhor essa definição, necessita-se esclarecer o que vem a ser um algoritmo, palavra que também é bastante citada na mídia, às vezes de modo não muito preciso. Um algoritmo nada mais é do que uma sequência finita de ações que resolve um certo problema. Uma receita culinária, como a de um risoto, é um algoritmo. Assim, um algoritmo pode resolver problemas de tipos bastante diferentes: cálculo estrutural (projeto de uma ponte), processamento de dados (geração de uma folha de pagamentos) ou planejamento (definição de um pacote de turismo).

Qual a principal diferença entre esses problemas? Basicamente, certos problemas têm soluções exatas, como o projeto da ponte, o processamento da folha de pagamentos e a receita do risoto. Solução exata, nesse caso, significa que se os passos definidos no algoritmo forem executados exatamente na ordem definida, ter-se-á ao final uma ponte que resistirá às intempéries, uma folha de pagamentos sem futuros problemas com o fisco e um delicioso risoto à moda italiana.

Por outro lado, problemas como a definição do pacote de turismo não têm uma solução exata, ou uma única solução. Outros exemplos similares são produção de diagnósticos (médicos, legais), geração automática de diálogos, reconhecimento de imagens etc. No caso do pacote de turismo, como garantir que é o melhor a ser adquirido? Deve-se escolher primeiro o voo ou o hotel? Quais datas teriam um custo menor? Existe disponibilidade nessas datas para todos os recursos desejados (hotéis, voos, passeios), e em caso positivo as férias podem ser marcadas nesse período?

Uma possível abordagem para solucionar tais problemas seria tentar gerar as possíveis soluções até que se obtenha a primeira delas, ou até que se encontre a melhor delas, caso existam várias soluções. Tal abordagem, apesar de teoricamente plausível, quase sempre é inviável na prática: a quantidade de possíveis soluções geradas é muito grande, e mesmo com um computador muito potente levaria muito tempo para obtê-las. Por exemplo, um problema de definição de rotas entre cidades poderia levar centenas de dias de processamento!2

Assim, tais problemas são usualmente mais bem solucionados por seres humanos, e na maioria dos casos de interesse não possuem solução algorítmica viável (em tempo de processamento) pela computação convencional.

Uma pergunta que se coloca então é a seguinte: Como nós, humanos, solucionamos esses problemas? Uma possível resposta é que utilizamos, de modo inato, um mecanismo de busca e poda: (i) geramos soluções candidatas ... mas quase nunca todas elas! (ii) escolhemos a melhor solução... de acordo com certo critério! e (iii) eventualmente, analisamos a posteriori o efeito das escolhas feitas... e as alteramos para o futuro i.e., aprendemos!

Assim, o domínio de IA se caracteriza por ser uma coleção de modelos, técnicas e tecnologias (busca, raciocínio e representação de conhecimento, mecanismos de decisão, percepção, planejamento, processamento de linguagem natural, tratamento de incertezas, aprendizado de máquina) que, isoladamente ou agrupadas, resolvem problemas de tal natureza. Para tal, podem utilizar paradigmas distintos, sendo os principais os paradigmas simbólico, conexionista, evolutivo e probabilístico.

Segundo o paradigma simbólico, deve-se inicialmente identificar o conhecimento do domínio (modelo do problema), para então representá-lo utilizando uma linguagem formal de representação e implementar um mecanismo de inferência para utilizar esse conhecimento.

Já no paradigma conexionista, a linguagem é uma rede de elementos simples, inspirada no funcionamento do cérebro, onde neurônios artificiais, conectados em rede, são capazes de aprender e de generalizar a partir de exemplos. O raciocínio consiste em aprender diretamente a função entrada-saída. Matematicamente, trata-se de uma técnica de aproximação de funções por regressão não linear.

O paradigma evolutivo, por sua vez, utiliza um método probabilístico de busca de soluções de problemas (otimização), onde soluções são representadas como indivíduos, aos quais se aplicam técnicas “inspiradas” na teoria da evolução como hereditariedade, mutação, seleção natural e recombinação (ou crossing over), para selecionar para as gerações seguintes os indivíduos mais adaptados, i.e., os que maximizam uma função objetivo (ou fitness function).

Finalmente, o paradigma probabilístico utiliza modelos para representar o conceito estatístico de independência condicional, a partir de relacionamentos causais no domínio. A inferência consiste em calcular a distribuição condicional de probabilidades dessa distribuição, e em alguns casos particulares de topologia, existem algoritmos bastante eficientes.

    """
    resumo = generate_summary(texto)
    print(resumo)

"""<p align='justify'>SAÍDA COM TOKENIZADOR EM INGLÊS - RESUMO1: Uma das primeiras tentativas desta abordagem, proposta em Rich e Knight (1991), é a seguinte: o objetivo da IA é desenvolver sistemas para realizar tarefas que, no momento: (i) são mais bem realizadas por seres humanos que por máquinas, ou (ii) não possuem solução algorítmica viável pela computação convencional. Existe disponibilidade nessas datas para todos os recursos desejados (hotéis, voos, passeios), e em caso positivo as férias podem ser marcadas nesse período?</p>"""

# Exemplo de utilizacao da funcao
# Será resumido um capítulo de artigo disponivel em: https://www.scielo.br/j/ea/a/c4sqqrthGMS3ngdBhGWtKhh/
if __name__ == "__main__":
    texto = """
     Os apaixonados receberam hoje uma boa notícia dos cardiologistas: o amor faz bem
ao coração.
Enquanto os apaixonados enviavam cartas e rosas vermelhas em comemoração ao
Dia dos Namorados (dia de São Valentim, comemorado em muitos países), a Federação
Mundial do Coração (WHF, na sigla em inglês) divulgou um comunicado pedindo aos
casais de todo o mundo que demonstrem suas emoções com liberdade. “Os namorados
têm outra razão para comemorar porque estudos mostram que estar apaixonado e
ser correspondido nos ajuda a manter a saúde e é particularmente bom para nossos
corações”, afirma o comunicado do WHF, que tem sua sede em Genebra, na Suíça.
 A federação, cujo objetivo é combater doenças cardíacas e reúne 166 sociedades
de cardiologia de 97 países, também acrescentou que o amor reduz o estresse, a
depressão e a ansiedade — três fatores de risco associados às doenças do coração.
 “Uma em cada três mortes no mundo ocorrem devido a problemas no coração e
derrame, seis vezes superior do que as mortes associadas à Aids”, afirmou o professor
Philip Poole-Wilson, cardiologista do Imperial College, em Londres, e presidente da
federação.
 “É por essa razão que estamos ressaltando a importância de adotar um estilo de
vida saudável e o impacto positivo que o amor pode ter para a saúde.”
 De acordo com a WHF, muitos estudos publicados demonstraram que fatores psi
cológicos, assim como os físicos, estão envolvidos com a doença cardíaca. Em uma
pesquisa de cinco anos, 10 mil homens com risco elevado de desenvolver angina
(dor no peito) foram questionados se a mulher com quem estavam demonstrava
seu amor por eles.
 Aqueles que responderam “sim” tinham a metade do risco de apresentar a condição.
    """
    resumo = generate_summary(texto)
    print(resumo)

"""<p align='justify'>SAÍDA COM TOKENIZADOR EM INGLÊS - RESUMO2: Os namorados têm outra razão para comemorar porque estudos mostram que estar apaixonado e ser correspondido nos ajuda a manter a saúde e é particularmente bom para nossos corações”, afirma o comunicado do WHF, que tem sua sede em Genebra, na Suíça. “Uma em cada três mortes no mundo ocorrem devido a problemas no coração e derrame, seis vezes superior do que as mortes associadas à Aids”, afirmou o professor Philip Poole-Wilson, cardiologista do Imperial College, em Londres, e presidente da federação.</p>


"""