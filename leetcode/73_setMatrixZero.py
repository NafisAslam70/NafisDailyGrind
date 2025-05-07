class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        firstRow=False
        firstCol=False

        m=len(matrix)
        n=len(matrix[0])

        # ham pehle row aur column ko use kr rhe as space yaaa

        #check kro koi pehla row ka element zero toh ni

        for j in range(n):
            if matrix[0][j]==0:
                firstRow=True
                break

           #check kro koi pehla col ka element zero toh ni

        for i in range(m):
            if matrix[i][0]==0:
                firstCol=True
                break

           #check kro koi pehla har ek row and col (pehla ko chhorkr) ka koi element zero toh ni

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

          #ab chek krna zra har ek row and col agar koi zero hai toh poora ko zero kro
       
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            
             #ab pehla row and column ko chcek kro zero toh ni ..agar hai to zero bhar do poore me
        
        if firstRow:
            for j in range(n):
                matrix[0][j]=0
        
        if firstCol:
            for i in range(m):
                matrix[i][0]=0



        
        