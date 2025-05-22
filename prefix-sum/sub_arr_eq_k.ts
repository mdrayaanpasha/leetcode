function subarraySum(nums: number[], k: number): number {
    /*
     WHAT IS THE INTUTION SuuR???
    
    quite simple frankly, it uses somethjing called prefix sum, which is u collect the accumauled sum array.

    here store that accumulated sum array and see if the accumated sum at this point and 
    there exist someother sub array that has the exact difference that would make me work!
    

    */
    
    let HashMap = new Map<number,number>(); //space: O(n)
    HashMap.set(0,1);


    let accumulatedSum = 0;
    let NumberOfSubArrEqK = 0;

    for(let ele of nums){ //time: O(n)
        accumulatedSum+=ele;

        if(HashMap.has(accumulatedSum - k)){
            NumberOfSubArrEqK+=HashMap.get(accumulatedSum - k);
        }

        HashMap.set(accumulatedSum, (HashMap.get(accumulatedSum) ?? 0) + 1);

    }

    return NumberOfSubArrEqK;

};


// SPACE & TIME: Linear
