"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA? R: SOMA = 91 
k = 0
SOMA = 0
INDICE = 13

while k < INDICE:
    k += 1
    SOMA += k
print(SOMA)


2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
R:

def verifica(list,param):
    for i in list:
        if param == i:
            return "está na sequência"
    assert i != param
    return "não está na sequência"

lista = [0,1]
Tam_min = 0

Tam = int(input("Qual tamanho da sequência de Fibonacci ? "))
num = int(input("informe um número para saber se estará na sequência: "))


while(Tam_min <= Tam):
    novo_valor = lista[Tam_min] + lista[Tam_min + 1]
    lista.append(novo_valor) 
    Tam_min = Tam_min + 1
else:
    print(lista)
    print(verifica(lista, num))

3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, _ 9 _

b) 2, 4, 8, 16, 32, 64, _ 128 _

c) 0, 1, 4, 9, 16, 25, 36, _ 49 _

d) 4, 16, 36, 64, _ 100 _

e) 1, 1, 2, 3, 5, 8, _ 13 _

f) 2,10, 12, 16, 17, 18, 19, _ 23 _


4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

R: O carro viaja a 110km/h, logo 0,9091(100km/110km) enquanto que o caminhão será 80km/h, porém tem 10 minutos por causa dos 2 pedágios
então ficará 100/80 + 1/6(10 minutos) totalizando 1,25 horas.Quando se compara os tempos do carro e do caminhão, O carro leva 0,91 horas 
para chegar ao ponto de cruzamento, enquanto o caminhão leva 1,25 horas. Então, o carro estará mais próximo da cidade de Ribeirão Preto 
quando eles se cruzarem na rodovia, já que leva menos tempo para percorrer a mesma distância em relação ao caminhão.  

5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

R:
Primeira formar:
palavra = input("Digite uma palavra: ")
print(palavra[::-1])

Segunda forma:
def inversa(str): 
  str_inversa = "" 
  for i in str: 
    str_inversa = i + str_inversa
  return str_inversa
  
palavra = input("Digite uma palavra: ")
print(inversa(palavra))

"""
