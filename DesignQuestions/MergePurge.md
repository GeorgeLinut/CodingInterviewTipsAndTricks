# Merge-Purge related problems

    Suppose that you are the CEO of a large company like Amazon and  
    you just aquired another company that provides similar services  
    like Emag. It's blackfriday and you have to send mails to all your 
    users with their favourite items that are on sale but you don't want to send multiple mails to the same person. What is your approach?  

Now from the start there are a few problems that you should point out to the interviewer:  

* Most likely there are users that are customors of the both entities.  
* We can have the same customer that used different emails for registration in these two companies  

* There are typos in our databases.

* The ammount of data.  

The solution for this problem was designed in the mid 90's and is called Merge-Purge.  
Merge-Purge is a process of merging records from one or multiple data sources and eliminating  
duplicate records. The core issue of the merge purge process is identifying equivalent attributes.  

So your answer should highlight the scenarios that merge-purge resolves:  

* Combine multiple lists to create a "master" list.  
* Combine multiple fields of data to create a "complete" record.
* Exclude certain records from your mailing.
* Find common records acrosss lists.

The classic Merge-Purge algorithm is the Sorted Neighborhood method.

To be continued..


