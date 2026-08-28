class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows=len(matrix)
        cols=len(matrix[0])

        top=0
        bottom=rows-1

        left=0
        right=cols-1
        ans=[]
        direc=0


        while left<=right and top<=bottom:
            
            if direc==0:
                for j in range(left, right+1):
                    ans.append(matrix[top][j])
                top+=1
                direc=1
            
            elif direc==1:
                for i in range(top, bottom+1):
                    ans.append(matrix[i][right])
                
                right-=1
                direc=2
            
            elif direc==2:
                for k in range(right,left-1,-1):
                    ans.append(matrix[bottom][k])
                bottom-=1
                direc=3
            
            else:
                for l in range(bottom, top-1, -1):
                    ans.append(matrix[l][left])
                left+=1
                direc=0
            
        return ans
    
                    

