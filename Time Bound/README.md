# Time-Bound-Computation

After this experiment I found out that Numpy dot function is reasonably faster than normal matrix multiplication. The matrices are in lost form, so they have some limitations, it has difficulty in supporting elementwise addition, subtraction,multiplicatio etc, and the fact that they can contain objects of differing types mean that python must store type information for every element, and must execute type dispatching code when operating on each element. After a little bit research I found out that numpy datastructures take less space, because of this extra space they get better performance and faster runtime.For example in this case, normal list form matrix takes upto 90 seconds for the order 500, whereas in numpy matrix it takes around 1-2 seconds for multiplication of order 500 matrices.

Overall Numpy is more efficient than lists, it is also more convenient to use, using numpy removes unnecessary extra steps required for normal matrix multiplication.Also, there are many useful libraries work with NumPy arrays. Some of them are, statistical analysis and visualization libraries.

Numba function has very low effect on the code, atleast in this case, but numba function can be found beneficial in other types of for loops.
Numba functions uses the "@jit" decorative method to increase the efficiency and speed of a code, but according to my observations it had very less effect on my script.

## Graph
<p align="center">
    <img src=https://github.com/Ayush19-01/GCI-Bound-Computations/blob/master/Time%20Bound/tbc.png>
</p>
