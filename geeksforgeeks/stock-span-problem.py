
# A stack based efficient method to calculate s 
def calculateSpan(price): 
    S = [0 for i in range(len(price)+1)] 

    n = len(price) 
    # Create a stack and push index of fist element to it 
    st = []  
    st.append(0) 
  
    # Span value of first element is always 1 
    S[0] = 1 
  
    # Calculate span values for rest of the elements 
    for i in range(1, n): 
          
        # Pop elements from stack whlie stack is not 
        # empty and top of stack is smaller than price[i] 
        while( len(st) > 0 and price[st[0]] <= price[i]): 
            st.pop() 
  
        # If stack becomes empty, then price[i] is greater 
        # than all elements on left of it, i.e. price[0], 
        # price[1], ..price[i-1]. Else the price[i]  is 
        # greater than elements after top of stack 
        S[i] = i+1 if len(st) <= 0 else (i - st[0]) 
  
        # Push this element to stack 
        st.append(i) 
  
    return S


price = [1,8,6,2,5,4,8,3,7]
print(calculateSpan(price))