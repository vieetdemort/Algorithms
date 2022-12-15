from typing import List
import numpy as np
import random
import math
import copy
from collections import Counter

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


class DSelect:

    
    def median_of_medians(self, arr):
        """
        Median of medians is an algorithm to select an approximate median as a pivot for a partitioning algorithm.
        :param arr:
        :return:
        """
        if arr is None or len(arr) == 0:
            return None

        return self.select_pivot(arr, len(arr) // 2)


    def select_pivot(self, arr, k):
        """
        Select a pivot corresponding to the kth largest element in the array
        :param arr: Array from which we need to find the median.
        :param k: cardinality that represents the kth larget element in the array
        :return: The value of the pivot
        """
        # Divide array into chunks of 5
        #chunks by taking i from 0 to 4, 5 to 9, 10 to 14, etc
        chunks = [arr[i : i+5] for i in range(0, len(arr), 5)]

        #sort each chunks
        sorted_chunks = [sorted(chunk) for chunk in chunks]


        #take the median of each chunk
        medians = [chunk[len(chunk) // 2] for chunk in sorted_chunks]

        #find the median of medians
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians) // 2]
        else:
            pivot = self.select_pivot(len(medians) // 2)



        #partition the array around the pivot
        p = self.partition(arr, pivot)

        #is the pivot position at the k position?
        if k == p:
            #select that pivot
            return pivot

        if k < p:
            #select a new pivot by looking on the left side of the partioning
            return self.select_pivot(arr[0:p], k)
        else:
            #select a new pivot by looking on the right side of the partioning
            return self.select_pivot(arr[p+1:len(arr)], k - p - 1)


    def partition(self, arr, pivot):
        """
        Partition the array around the given pivot
        :param arr: array to be partitioned
        :param pivot: pivot used for the partitioning
        :return: final position of the pivot used as a partioning point
        """
        left = 0
        right = len(arr) - 1
        i = 0

        while i <= right:
            if arr[i] == pivot:
                i += 1

            elif arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
                i += 1
            else:
                arr[right], arr[i] = arr[i], arr[right]
                right -= 1

        return left

    

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


# Karger's Algorithm

class Graph(object):
    def __init__(self, vlist):
        self.verts = {v[0]:Counter(v[1:]) for v in vlist}
        self.update_edges()

    def update_edges(self):
        self.edges = []
        
        for k, v in self.verts.items():
            self.edges += ([(k, t) for t in v.keys() for n in range(v[t]) if k < t])

    @property
    def vertex_count(self):
        return len(self.verts)

    @property
    def edge_count(self):
        return len(self.edges)

    def merge_vertices(self, edge_index):
        hi, ti = self.edges[edge_index]
        
        head = self.verts[hi]
        tail = self.verts[ti]

        # Remove the edge between head and tail
        del head[ti]
        del tail[hi]

        # Merge tails
        head.update(tail)

        # Update all the neighboring vertices of the fused vertex
        for i in tail.keys():
            v = self.verts[i]
            v[hi] += v[ti]
            del v[ti]
            
        # Finally remove the tail vertex
        del self.verts[ti]

        self.update_edges()
        
def contract(graph, min_v=2):
    g = copy.deepcopy(graph)
    while g.vertex_count > min_v:
        r = random.randrange(0, g.edge_count)
        g.merge_vertices(r)

    return g

# Karger's Algorithm
# For failure probabilty upper bound of 1/n, repeat the algorithm nC2 logn times
def min_cut(graph):
    m = graph.edge_count
    n = graph.vertex_count
    for i in range(int(n * (n-1) * math.log(n)/2)):
        g = contract(graph)
        m = min(m, g.edge_count)
        # print(i, m)
    return m


def _fast_min_cut(graph):
    if graph.vertex_count <= 6:
        return min_cut(graph)
    else:
        t = math.floor(1 + graph.vertex_count / math.sqrt(2))
        g1 = contract(graph, t)
        g2 = contract(graph, t)
        
        return min(_fast_min_cut(g1), _fast_min_cut(g2))


# For failure probabilty upper bound of 1/n, repeat the algorithm nlogn/(n - 1) times
def fast_min_cut(graph):
    m = graph.edge_count
    n = graph.vertex_count
    for i in range(int(n * math.log(n)/(n - 1))):
        m = min(m, _fast_min_cut(graph))
        # print(i, m)
    return m
    
    
# Simple test
'''graph = Graph([[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]])
print(fast_min_cut(graph))'''