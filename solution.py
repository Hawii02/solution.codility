# Pseudocode 
# Start with function
#    def solution(A, D);
#  Initialize  bal = 0;
#  create an empty array where final balance will be stored : final_bal = []
# Use if conditional STATEMENT to output card payment and incoming transfers
# Finally add the total result to final_bal which we initialized it as an empty array.

def solution(A, D):
    bal = 0
    final_bal = []
    for i in range(len(A)):
        year = int(D[i].split('-')[0])
        if A[i] <= 0:
        # year = int(D[i]* 12)
        # if A[i] <= 0:
        #     return("card payment")
        # else:
        #     return("incoming transfer")  
          
            bal += A[i]

            if len([transaction for transaction in final_bal if transaction['year'] == year]) >= 3 and sum(transaction['amount'] for transaction in final_bal if transaction['year'] == year) >= 100:
             bal -= 5
    
        else:
            bal += A[i]
        final_bal.append({'amount': A[i], 'year': year})
    return bal  

print(solution([100,100, 100, -10], ['2021-12-31', '2020-12-22', '2020-01-01']))


      







