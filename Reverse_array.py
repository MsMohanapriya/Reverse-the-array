def Reverse_array(array):
    size=len(array)
    for i in range(len(array)//2):
        array[i],array[size-1]=array[size-1],array[i]
        size-=1
    return array
        
    
array=list(map(int,input().split()))
print(Reverse_array(array))