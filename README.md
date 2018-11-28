# CodingInterviewTipsAndTricks

Resources, solved problems and references for interview practice.

# Part 1: Classic problems

These are the problems that you should solve before an interview.
Knowing the best solution for these problem may give you idea for more complex prblems.

In the following I will give a few examples of "classic" problems (you can also find the python implementation in this repository)
Some of these problems appear difficult the first time you read them but if you understand the "suggested" solution for them 
you will be able to solve it very quickly in the next coding interview.

The first problem that we will solve is usually asked as a warm up question in technical interviews  

    Classic Problem no. 0: You are given a list of n-1 integers and these integers are in the range of 1 to n. 
    There are no duplicates in list. One of the integers is missing in the list.  
How do you find the missing number as quickly as possible?  
Of course you can add all the numbers in the interval and substract the sum of the given numbers and you will find the missing one.  
But that is not very interesting so the proposed solution is using bit operations (a must read subject before an interview).  
The operation that we will use is Xor.   
Fact: If we xor a number with itself the result will be 0 as thew binary representation is identical. We also observ that 0  
is a neutral element for the Xor operation since 0 xor 0 = 0 and 1 xor 0 = 0  
Using those observations we can see that if we xor all the elements that are given with all the elements in the interval [1,n]  
we will have pairs, 1 xor 1 = 0, 2 xor 2 = 0... n xor n = 0 , the only element that will not have a pair is the missing one.  
So the result of this operation is the missing element xor a lot of 0's but since 0 is the neutral element we are left with the answer. 

Short version of the solution discussed above:  
Input: a, an array of lenght n-1 with numbers in [1,n]  
R1 = a[0] xor a[1] xor a[n-1]  
R2 = 1 xor 2... xor n  
R3 = R1 xor R2 = the missing number  

The set of "classic" problems that we will solve uses one of the most used data structures in interviews, the Linked List.  
Languages such as Java or C# have their own implementation for the linked list but is good practice to implement your own.  

    Classic Problem no. 1: Find the "middle" of a linked list.
    Classic Problem no. 2: Detect a cycle in a linked list.

The general approach for these two problems is very similar.  
Use 2 pointers instead of one and give them diffent speed!  

If you want to find the middle of the list you need move a pointer two noded every time you move the other one once.
When the first pointer reaches the end of the list the second one is at the middle (for n = 2k+1 nodes, otherwise he is at k+1 and we can consider the previous node to as the middle)  
(detect_list_middle.py)  

If you want to detect a cycle use the same approach but in this case the first pointer will never reach the end if there is a cycle  
so the first time you have both pointers at the same node you detected the cycle.(detect_list_cycle).py)   
  
The complexity for both solutions is O(N) time and O(1) memory.(we can detect a cycle with only one pointer but it will require O(N)   memory).  

To be continued...  

# Part 2: Classic solutions  

    Classic Solution no. 1: Use a HashMap  
To quote Gayle Laakmann(the author of Cracking the Coding Interview) the Hashmap should be on top of your mind whenever you are solving   an interview question.  
It's the magic weapon with "almost" O(1) get and O(1) update operations.  

    Classic Solution no. 2: Binary search or smth like it

Problems that demand a certain numeric value with rounding error are usually a hint that binary search is involved.  
For example find the K order root of a number N can be solved by starting with 0 and the number (or 1 if the number is less than 1).  
You just have to compare middle^K with N to see i which way you have to shift the interval and the problem is over.  
Another exit condition can be that your interval is less than the maximum error defined in the problem.  
Python implmentation can be find in MathRelatedProblems/KRootAprroximation.py.  
