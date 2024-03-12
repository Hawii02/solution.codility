# Pseudocode 
# Start with function
#    def solution(A, D);
#  Initialize  bal = 0;
#  create an empty array where final balance will be stored : final_bal = []
# Iterate through the array with a for loop to get the balances and finally final_bal
# Use if conditional STATEMENT to output card payment and incoming transfers
# Negate the amount by 5 per month if user posssess a card else if transactions more than 3 and transactions > 100 dont negate by 5
# Finally add the total result to final_bal which we initialized it as an empty array.

  
def solution(A, D):
    bal = 0
    final_bal = []
    for i in range(len(A)):
        year = int(D[i].split('-')[0])
        if A[i] <= 0:
            bal += A[i]

            if len([transaction for transaction in final_bal if transaction['year'] == year]) >= 3 and sum(transaction['amount'] for transaction in final_bal if transaction['year'] == year) >= 100:
             bal -= 5
    
        else:
            bal += A[i]
        final_bal.append({'amount': A[i], 'year': year})
        print(bal)
    return bal  
    

print(solution([100,100, 100, -10], ['2021-12-31', '2020-12-22', '2020-01-01']))    

