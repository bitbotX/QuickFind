class QuickFind:
    id = list()
    def __init__(self, n=None, arr=None):
        if arr == None:
            self.id = self._constuct_array(n)
        else:
            self.id = arr

    def generate_array(self, n):
        temp_arr = []
        for e in range(n):
            temp_arr.append(e)
        return temp_arr

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for e in range(len(self.id)):
            if self.id[e] == pid:
                self.id[e] = qid

if __name__ == '__main__':
    qf=QuickFind(10,[0,1,1,3,4,5,2,2,3,3])
    qf.generate_array(10)
    union(4,2)
    print(connected(4,2))