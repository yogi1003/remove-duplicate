class Dup:


    def __init__(self):
        self.st = set()
        self.result = 'result.txt'
        self.awal = 0
        self.weblist = 'weblist.txt'

    def hitung(self):
        return self.weblist.__len__()

    def remove(self):
        for line in self.weblist:
            self.st.add(line)
        open(self.result, "w").writelines(''.join(self.st))
        return self.st.__len__()
    
    @property
    def main(self):
        self.weblist = open(input('Yourlist : '), "r").readlines()
        self.result = input('Saved : ')
        #self.weblist = open(self.weblist, "r").read().splitlines()
        print('from', self.hitung())
        print('to', self.remove())

if __name__ == "__main__":
    Dup().main


