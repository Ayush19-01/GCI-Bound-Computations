# Space Bound Computations

The results were quite same as we got in the Time bound computation task, the numpy dot functions is reasonably faster than both
normal multiplication and using the numba @jit multiplication. Although @jit method should've made my normal multiplication much faster
but only a slight improvement was seen in this result. 

## Graph

<p align="center">
    <img src =https://github.com/Ayush19-01/GCI-Bound-Computations/blob/master/Space%20Bound/sbc.png>
</p>

## Comparison with last graph

The numba @jit multiplication and normal multiplication results are almost identical in both the tasks, but the numpy dot results were
not same, we cannot see the difference in this graph so I created 2 different graphs just for numpy dot function with and without the 
ravel function.

## What is ravel function?

Ravel is numpy function, basically it converts a 2-D or 3-D array into 1-D array, which in turn makes calculation much easier.
It takes the matrix and order style as arguments. Order styles are : "C" ,"F","A" and "K"


‘C’ means to index the elements in row-major, C-style order, with the lastaxis index changing fastest, back to the first axis 
index changing slowest. ‘F’ means to index the elements in column-major, Fortran-style order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options
take no account of the memory layout of the underlying array, and only refer to the order of axis indexing.

<p align="center">
    <img src = https://github.com/Ayush19-01/GCI-Bound-Computations/blob/master/Space%20Bound/mvp.png width=50% height=50%>
</p>


While normal numpy dot
"C" method is used, n this code i have used the "F" method which the column major style of calculating and I found it to be faster than the "C"
calculations. The results with ravel and without ravel are shown below.

### Numpy with Ravel

<p align="center">
    <img src=https://github.com/Ayush19-01/GCI-Bound-Computations/blob/master/Space%20Bound/cs.png>
</p>

### Normal Numpy

<p align="center">
    <img src=https://github.com/Ayush19-01/GCI-Bound-Computations/blob/master/Space%20Bound/ct.png>
</p>

After comparing both the graphs, we can say that the fortran style/column-major is much more faster than the normal numpy dot function.
