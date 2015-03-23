#!/usr/bin/env python2.6
import json, sys, os, commands
 
data = None
with open("input.json") as json_data:
    data = json.load(json_data)
 
niters = data['niters']
nprocs = data['nprocs']
 
dir = os.path.dirname(os.path.realpath(__file__))
 
cmd = "module add openmpi/1.6.4-gnu-4.7.2-ib && (mpiexec -np %s %s/pi_mpi %s > output.json)" % (nprocs, dir, niters)

status, output = commands.getstatusoutput(cmd)
print output

# w kodzie pi_mpi...
# printf("{\"status\": \"ok\", \"results\": { \"steps\": %ld, \"time\": %lf, \"value\": %lf}}\n", steps, time, pi);