from typing import List

class Sorting:
    
    def mergeSort(self, array: List[int]) -> List[int] or None:
        if len(array) == 1:
            return array
    
        HALF = len(array) // 2
        l = array[:HALF]
        r = array[HALF:]
        
        self.mergeSort(l)
        self.mergeSort(r)
        
        k=i=j=0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i+=1
            else:
                array[k] = r[j]
                j+=1
            k+=1
            
        while i < len(l):
            array[k] = l[i]
            i+=1
            k+=1
            
        while j < len(r):
            array[k] = r[j]
            j+=1
            k+=1
                
        
        return array




    def bubbleSort(self, array: List[int]) -> List[int]:
        
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
        
        return array



    def inversions(self, array: List[int]) -> List[int]:
        inv = 0
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] > array[j] and i < j:
                    array[i], array[j] = array[j], array[i]
                    inv += 1
        return inv   


class Multiply:
    
    def kuratsubaMult(self, num1: int, num2: int) -> int:
        
        if len(str(num1)) or len(str(num2)) == '1':
            return num1*num2
            
        else:
            n = max(len(str(num1)),len(str(num2)))
		
            nby2 = n / 2
            
            a = num1 / 10**(nby2)
            b = num1 % 10**(nby2)
            c = num2 / 10**(nby2)
            d = num2 % 10**(nby2)
            
            ac = self.kuratsubaMult(a,c)
            bd = self.kuratsubaMult(b,d)
            ad_plus_bc = self.kuratsubaMult(a+b,c+d) - ac - bd
            
            # this little trick, writing n as 2*nby2 takes care of both even and odd n
            prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

            return prod
        
    
    def matrixMultiplication(self, a, b):
        
        res = [[0]*len(a[i]) for i in range(len(a))]
        
        for i in range(len(a)):
            for j in range(len(b[0])):        
                for k in range(len(b)):
                    res[i][j] += a[i][k] * b[k][j]
        
        return res
        
        
            

num1 = [[2,2,2,2],
        [2,2,2,2],
        [2,2,2,2],
        [2,2,2,2]]

num2 = [[2,2,2,2],
        [2,2,2,2],
        [2,2,2,2],
        [2,2,2,2]]


sol = Multiply()
print(sol.matrixMultiplication(num1, num2))
