''' Iterador para as wordlists, evita que uma wordlist grande seja carregada de uma vez só na memória causando lentidao
    consumindo muitos recursos ou gerando um erro de código "MemoryError" '''

class WordlistIterator(object):
    def __init__(self, namefile):
        self.wordlist = open(namefile, 'r', encoding="utf8", errors='ignore')
        self.currentLine = ''
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.currentLine = self.wordlist.readline().strip()
        if self.currentLine:
            return self.currentLine
        
        raise StopIteration