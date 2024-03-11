  // Pseudocode
// Account was empty at beginning of year
   // initialize bal = 0;
// if amount is negative or less than zero(amount <= 0) then it was cardPayment; else if was  incoming transfer
// there is a fee for having a card which is 5 per month. deducted from account balance unless atleast 3 payments made by card for total cost of atleast 100
// start with function solution(A, D)
// A represents transaction amounts and D transaction dates. Should return final balance of account at the end of year 2020
// fee for having the card == (-5) per month else if payments <= 3; 100
// array A == transaction amounts D == transaction Dates

  //  function solution(A,D){
  //   let bal = 0;

  //       if( A <= 0 ){
  //          return bal - 5[D];
  //     }
  //     else if(3[A] && A <= 100){
  //          return bal;
  //     }
  //     else{
  //       return bal -5[D];
  //     }
  //   }
  //   console.log(A=[100, 100,100, -10])
    
  

    // if( A <= 0 ){
    //     return bal - 5[D];
    // }
    // else if(3[A] && A <= 100){
    //     return bal;
    // }
    // else{
    //     return bal -5[D];
    // }


    // function solution(A,D){
    //   A = [
    //     100, 100, 100, -10
    //   ]
    //   D = [

    //   ]
    //   let bal = 0;
    //   const finalBal = [];
    //   for (let i = 0; i < A.length; i ++){
    //     const year = parseInt(D[i].split('-')[0]);
    //     if(A[i] <= 0){
    //       if (finalBal.filter(trans => trans.year === year).length >= 3 &&
    //       finalBal.filter(trans => trans.year === year).reduce((total, trans) => total + trans.amount) >= 100){
    //         bal -= 5;
    //       }  
    //       bal += A[i];
    //     }
    //     else {
    //       bal += A[i];
    //     }
    //     finalBal.push({amount: A[i], year: year});
    //   }
    //    return bal;
    // }
    // console.log(solution([100, 100, 100, -10], ['2020-12-31', '2020-12-22', '2020-01-01']));


    // Javascript to be continued...