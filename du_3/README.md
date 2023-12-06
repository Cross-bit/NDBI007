# hw_03 solutioin: litwin, fagin

In the end I decided to insert only the student ID attribute values, 
for simplicity of parsing and this description, but obviously we could 
insert all the values, if needed.

## Comment to litwin:

Page capacity: 3

What i have noticed is that when we have a lot of duplicate entries
(e.g. lets say meaning in terms of least significant bits for given stage) 
they tend to get clustered in the same page (which is obivous why).

If we would have many numbers that would be diffrentiable only by the most significant bits
(meaning, we would have multiple same values (based on the LSb) in the same page 
then there would be e.g. only zeroes in the middle for all these numbers... 
so lets say e.g. numbers like 10100000000011, 11100000000011, 10000000000011)
then wew would have to wait for many stages, before we would finally get some differentiation.

Looking at our input values(studentIds) we can see that such cases our very rear 
we can conclude that the pages will not overflow very often(at least not extremly).
Thus I don't see a reason to increase this constant.



 
Splitting after: 2
Because the data seams to have well "random" least significant bits. 
There is good chance that we will be able to redistribute data 
from a single page into another pages by splitting more often. 
Since this constant specifies frequency, "how often we will be splitting"
it makes sense to choose it low. (in our case) 




## Comment to fagin:
Chosen capacity: 3

Similarly to the litwin case. Based on the input data I don't think we will have to split very often
since the LSbs of the values are well "randomized". So I think that size of n = 3 is sufficient.
