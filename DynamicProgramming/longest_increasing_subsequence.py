def longest_subsequence(arr): 
    n = len(arr) 
  
    lista_crescatoare = [1]*n 
  
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lista_crescatoare[i]< lista_crescatoare[j] + 1 : 
                lista_crescatoare[i] = lista_crescatoare[j]+1
  
    maximum = 0
  
    for i in range(n): 
        maximum = max(maximum , lista_crescatoare[i]) 
  
    return maximum 
  
arr = [1, 0, 3, 4, 2, 10, 4] 
print "Length of lista_crescatoare is", longest_subsequence(arr) 
