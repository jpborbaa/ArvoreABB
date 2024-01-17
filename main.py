from NodeABB import NodeABB
from ArrayQueue import ArrayQueue


def carregarEntrada(raiz):
  f = open('entrada.txt', 'r')
  lines = f.readlines()
  # funciona tanto pro caso dos valores estarem separados por linha quanto por espaço no arquivo entrada.txt
  for line in lines:
    elems = line.split(' ')
    for elem in elems:
      raiz.add(NodeABB(elem))

  return raiz

def mostrarNiveis2(raiz, niveis=-1):
	arb = NodeABB()
	nivel_atual = 0

	if raiz.raizArbin() is not None:
		fila = ArrayQueue()
		fila.enqueue(raiz)

		# se for -1 sempre ignorar, exibir a árvore toda
		while not fila.is_empty() and (niveis == -1 or nivel_atual < niveis):
			# a raíz é considerada nível 0
			print(f"Nível {nivel_atual}")
			nivel_atual += 1
			tam = fila.__len__()
			# só iterar pelo tamanho salvo na variável acima, para conseguir parar no nível definido
			for _ in range(tam):
				# tira da fila e salva na variável
				arb = fila.dequeue()
				if arb is not None and arb.raizArbin() is not None:
					print(arb.raizArbin())
					fila.enqueue(arb.esqArbin())
					fila.enqueue(arb.dirArbin())

def mostrarNiveis(raiz, niveis=-1):
  if raiz is not None:
    mostrarNiveisRecursivo(raiz, niveis)


def mostrarNiveisRecursivo(no, niveis, nivel_atual=0):
  if no is None or (niveis != -1 and nivel_atual > niveis):
    return

  mostrarNiveisRecursivo(no._dir, niveis, nivel_atual + 1)

  print("  " * nivel_atual + str(no._data))

  mostrarNiveisRecursivo(no._esq, niveis, nivel_atual + 1)


def preOrdem(raiz):
  if raiz is not None and raiz.raizArbin() is not None:
    print(raiz.raizArbin())
    preOrdem(raiz.esqArbin())
    preOrdem(raiz.dirArbin())


def inOrdem(raiz):
  if raiz is not None and raiz.raizArbin() is not None:
    inOrdem(raiz.esqArbin())
    print(raiz.raizArbin())
    inOrdem(raiz.dirArbin())


def posOrdem(raiz):
  if raiz is not None and raiz.raizArbin() is not None:
    posOrdem(raiz.esqArbin())
    posOrdem(raiz.dirArbin())
    print(raiz.raizArbin())


def removerElemento(raiz):
    elem = input('String a remover: ')
    raiz = removerElementoRecursivo(raiz, elem)
    return raiz

def removerElementoRecursivo(no, elem):
    if no is None:
        return None

    if elem < no._data:
        no._esq = removerElementoRecursivo(no._esq, elem)
    elif elem > no._data:
        no._dir = removerElementoRecursivo(no._dir, elem)
    else:
        # Caso 1: Nó folha (sem filhos)
        if no._esq is None and no._dir is None:
            return None
        # Caso 2: Nó com um filho
        elif no._esq is None:
            return no._dir
        elif no._dir is None:
            return no._esq
        # Caso 3: Nó com dois filhos
        else:
            sucessor = encontrarSucessor(no._dir)
            no._data = sucessor._data
            no._dir = removerElementoRecursivo(no._dir, sucessor._data)

    return no

def encontrarSucessor(no):
    while no._esq is not None:
        no = no._esq
    return no



def main():
  opt = None
  raiz = NodeABB()
  while True:
    switch = {
      '1': lambda: carregarEntrada(raiz),
      '2': lambda: mostrarNiveis2(raiz, 4),  # 4 primeiros níveis: 0, 1, 2 e 3
      '3': lambda: mostrarNiveis(raiz),
      '4': lambda: preOrdem(raiz),
      '5': lambda: inOrdem(raiz),
      '6': lambda: posOrdem(raiz),
      '7': lambda: removerElemento(raiz),
      '8': lambda: print('Fim do Programa')
    }

    print('1 - Carregar o arquivo de nomes na ABB (entrada.txt)')
    print('2 - Mostrar árvore (os 4 primeiros níveis): caminhamento por nível')
    print('3 - Mostrar a árvore (todos os níveis): caminhamento por nível')
    print('4 - Mostrar a árvore: pré-ordem')
    print('5 - Mostrar a árvore: In-ordem')
    print('6 - Mostrar a árvore: pós-ordem')
    print('7 - Remover um elemento da árvore')
    print('8 - Encerrar')

    opt = input('Escolha: ')

    fn = switch.get(opt)
    if fn:
      fn()
    else:
      print('Opção Inválida')

    if opt == '8':
      break

    print('\n')


if __name__ == '__main__':
  main()
