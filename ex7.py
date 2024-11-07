class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostraNo(self):
        print(self.valor)

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []
    
    def inserir(self, valor):
        novoNo = No(valor)
        if self.raiz is None:
            self.raiz = novoNo
        else:
            noAtual = self.raiz
            while True:
                noPai = noAtual
                if valor < noAtual.valor:
                    noAtual = noAtual.esquerda
                    if noAtual is None:
                        noPai.esquerda = novoNo
                        return
                else:
                    noAtual = noAtual.direita
                    if noAtual is None:
                        noPai.direita = novoNo
                        return
    
    def pesquisar(self, valor):
        noAtual = self.raiz
        while noAtual.valor != valor:
            if valor < noAtual.valor:
                noAtual = noAtual.esquerda
            else:
                noAtual = noAtual.direita
            if noAtual is None:
                return None
        return noAtual
    
    def preOrdem(self, no):
        if no is not None:
            print(no.valor)
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)
    
    def emOrdem(self, no):
        if no is not None:
            self.emOrdem(no.esquerda)
            print(no.valor)
            self.emOrdem(no.direita)
    
    def posOrdem(self, no):
        if no is not None:
            self.posOrdem(no.esquerda)
            self.posOrdem(no.direita)
            print(no.valor)
    
    def excluir(self, valor):
        if self.raiz is None:
            print('A árvore está vazia')
            return
        noAtual = self.raiz
        noPai = self.raiz
        eEsquerda = True
        while noAtual.valor != valor:
            noPai = noAtual
            if valor < noAtual.valor:
                eEsquerda = True
                noAtual = noAtual.esquerda
            else:
                eEsquerda = False
                noAtual = noAtual.direita
            if noAtual is None:
                return False
        if noAtual.esquerda is None and noAtual.direita is None:
            if noAtual == self.raiz:
                self.raiz = None
            elif eEsquerda:
                noPai.esquerda = None
            else:
                noPai.direita = None
        elif noAtual.direita is None:
            if noAtual == self.raiz:
                self.raiz = noAtual.esquerda
            elif eEsquerda:
                noPai.esquerda = noAtual.esquerda
            else:
                noPai.direita = noAtual.esquerda
        elif noAtual.esquerda is None:
            if noAtual == self.raiz:
                self.raiz = noAtual.direita
            elif eEsquerda:
                noPai.esquerda = noAtual.direita
            else:
                noPai.direita = noAtual.direita
        else:
            sucessor = self.obterSucessor(noAtual)
            if noAtual == self.raiz:
                self.raiz = sucessor
            elif eEsquerda:
                noPai.esquerda = sucessor
            else:
                noPai.direita = sucessor
            sucessor.esquerda = noAtual.esquerda
        return True
    
    def obterSucessor(self, no):
        paiSucessor = no
        sucessor = no
        noAtual = no.direita
        while noAtual is not None:
            paiSucessor = sucessor
            sucessor = noAtual
            noAtual = noAtual.esquerda
        if sucessor != no.direita:
            paiSucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor

arvore = ArvoreBinariaBusca() 
arvore.inserir(53) 
arvore.inserir(30) 
arvore.inserir(14) 
arvore.inserir(39) 
arvore.inserir(9) 
arvore.inserir(23) 
arvore.inserir(34) 
arvore.inserir(49) 
arvore.inserir(72) 
arvore.inserir(61) 
arvore.inserir(84) 
arvore.inserir(79) 
arvore.pesquisar(39) 
arvore.pesquisar(84) 
arvore.pesquisar(100) 
arvore.excluir(9) 
arvore.excluir(14) 
arvore.excluir(72)

print("\nPré-ordem:")
arvore.preOrdem(arvore.raiz)

print("\nEm-ordem:")
arvore.emOrdem(arvore.raiz)

print("\nPós-ordem:")
arvore.posOrdem(arvore.raiz)
