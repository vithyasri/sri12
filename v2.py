def multiplyFactors(n) : 
    prod = 1
      
    i = 1
    while i * i <= n : 
        if (n % i == 0) : 
           
            if (n / i == i) : 
                prod = (prod * i) % M 
         
            else : 
                prod = (prod * i) % M 
                prod = (prod * n / i) % M 
        i = i + 1
  
    return prod 
