 Your data model is so lovely, created with love and care.

However, someone did not appreciate that and decided to give you the new data in a messed-up format

(changed the order of the columns, names, or even values order!).

This could lead to computation errors if you are retyping a script that gets specific numbers from a particular column, you merged data on a specific set of columns, or even errors if your data model is in a power query or something.

We want to pass the data in an acceptable way, where every single value knows its way home.

We have two methods to accomplish that, an easy way and the hard way.

but before discussing ways let's see the first steps to thinking and fixing that problem:

we need for each row, a single list that represents each element in that row, then we need to pass each value to its beloved column.

and we do not know the names of the columns, we only know the structure of the new data, any number of rows, 4 columns.

Skills Used:
	1.Python
	2.Pandas
	3.re module
	4.Regular Expressions

you can find an article about this issue: https://theveryamateuredatascientist.blogspot.com/2022/07/assign-data-to-columns-using-regular.html