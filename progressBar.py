class ProgressBar:
    """ simple progressbar """
    def __init__(self, total, marker='#'):
        self.total = total
        self.marker = marker
        self.current = 0

    def __repr__(self):
        return f'ProgressBar(total={self.total}, marker="{self.marker}")'
    
    def update(self):
        if not self.current >= self.total:
            self.current += 1
            self.show()

    def show(self):
        print(f'Progresso: [{int((self.current/self.total)*100)}%] [{self.marker*int((self.current/self.total)*90)}{"."*(90-int((self.current/self.total)*90))}] | {self.current}/{self.total}', end='\r')
