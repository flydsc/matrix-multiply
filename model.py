class MatrixMul:
    def __init__(self, mat_left, mat_right):#n*m m*p 
        self.mat_left = mat_left
        self.mat_right = mat_right
        self.mat_left_n = len(mat_left)
        self.mat_right_p = len(mat_right[0])
        self.mat_m = len(mat_right)
        self.result = [[0]*self.mat_right_p for row in range(self.mat_left_n)]
        self._generate()

    def getresult(self):
        return self.result
    
    def _generate(self):
        for n in range(self.mat_left_n):#each left mat row
            for p in range(0, self.mat_right_p): #each right mat row
                for m in range(0, self.mat_m): # each element
                    self.result[n][p]=self.result[n][p]+self.mat_left[n][m]*self.mat_right[m][p]
