PR 3] 

mpi.c:1:10: fatal error: mpi.h: No such file or directory
    1 | #include <mpi.h>
      |          ^~~~~~~
compilation terminated.


Install the MPI development package by running the following command:

$ sudo apt-get install libopenmpi-dev


Copy code
mpicc -o mpi mpi.c

mpirun -np 1 ./mpi

./mpi




