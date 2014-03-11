#!/usr/bin/env python
from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD
print("hello world")
print("my rank is: %d, at node %s"%(comm.rank, socket.gethostname()))