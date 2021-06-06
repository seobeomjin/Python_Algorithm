# (1) 32-35쪽: [실습프로그램] 방법1을 이용하여 makeHeap을 구현하고 힙정렬 알고리즘을 python으로 완성하라. 

# p32-35 
# method-1 : arrange the heap each time during putting each element
# implement makeHeap via method-1 and complete the heapsort  

# Heapsort 
    # makeHeap
        # siftDown(Hsub)
    # removeKeys
        # s[i] = root(H)

import math
class Heap(object):
    n=0
    def __init__(self, data):
        self.data=data
        self.n=len(self.data)-1 # start index from 1. to calculate 2*n , 2*n+1 , flooe[2*n+1] , etc  
                                # heap size를 하나 줄여야 한다. 인덱스는 1부터. 인덱스의 2* 연산 가능하도록.         
    
    def addElt(self,elt):
        self.data.append(elt)
        self.n += 1
        self.siftUp(self.n)

    def siftUp(self, i): # down -> up 
        while(i>=2):
            parent = math.floor(i/2)
            if parent >=1 and self.data[parent] < self.data[i] : 
                self.data[parent], self.data[i] = self.data[i], self.data[parent]
                self.siftUp(parent)
            else : 
                break

    def siftDown(self, i) : # up -> down 
        siftkey = self.data[i]
        parent = i 
        spotfound = False 
        while 2*parent <=self.n and not spotfound:
            # First comparison to find a bigger child  
            if 2*parent < self.n and self.data[2*parent] < self.data[2*parent+1]:  #  left child < right child
                largerchild = 2*parent+1 # right child 
            else : # left child > right child 
                largerchild = 2*parent # else left child 
            # Second comparison to be valid or not for changing the position  
            if siftkey < self.data[largerchild] :  # if key is smaller than child 
                self.data[parent] = self.data[largerchild]
                parent = largerchild # it changes parent index to larger child index 
            else : 
                spotfound = True
            self.data[parent] = siftkey

    def root(self):
        if(self.n>0): # if heap is empty, no need to do siftdown
            keyout = self.data[1]
            self.data[1] = self.data[self.n]
            self.n =self.n-1
            self.siftDown(1)
            return keyout    
        
    def removeKeys(self):
        sorted_value = []
        for i in range(self.n,0,-1):
             sorted_value.append(self.root())
        return sorted_value

    def makeHeap2(self):
        i = math.floor(self.n/2)
        for k in range(i,0,-1):
            self.siftDown(k) 

    def makeHeap1(self): 
        # when each element is put in the tree, arrange the data each time   
        # 1. add to the end 
        # 2. take sift-up 
        for i in range(1, self.n+1):
            self.siftUp(i)

def heapSort(a):
    heap_A = Heap(a)
    heap_A.makeHeap1() 
    return heap_A.removeKeys()



#p34
# a=[0,11,14,2,7,6,3,9,5]
# b=Heap(a)
# b.makeHeap2()
# print(b.data)
# b.addElt(50)
# print(b.data)
# s=heapSort(a)
# print(s)

#p35
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap1()
print(b.data)
s=heapSort(a)
print(s)
