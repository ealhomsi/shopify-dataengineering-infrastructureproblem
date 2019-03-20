# shopify-data-engineering-infrastructure-challenge
shopify-dataengineering-infrastructureproblem

#Data Engineering / Infrastructure Problem

Build a simple joiner that accepts two files each containing an array of json objects. The user can specify any key that is shared in both files to join on. 
Produce a new array with the joined objects. For simplicity follow the conventions of a standard SQL inner join, bonus points for implementing outer joins as well. 
Try to keep runtime under O(n2).
Join the supplied customers file to the supplied orders file. Using the keys `cid` and `customer_id` respectively.

What to submit: The length of the resulting array and the total for orders placed by Barry and Steve. 


# instructions on running
./solution.py <col1> <col2> [<file1>] [<file2>]
notice that the files are optional. If not specified the program will use the default urls.
