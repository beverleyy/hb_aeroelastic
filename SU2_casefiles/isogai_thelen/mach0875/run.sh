#!/bin/bash

for i in */; do
	for j in mode1 mode2; do
		if [ "${i}" != "steady/" ]; then
			copy0='cp steady/restart_flow.dat "${i}${j}/restart_flow_0.dat"'
			copy1='cp steady/restart_flow.dat "${i}${j}/restart_flow_1.dat"'
			copy2='cp steady/restart_flow.dat "${i}${j}/restart_flow_2.dat"'
			command='mpirun -np 16 SU2_CFD "${i}${j}/HB.cfg"'
			move='mv HB_output.csv "${i}${j}/"'
			cp steady/restart_flow.dat restart_flow_0.dat
			cp steady/restart_flow.dat restart_flow_1.dat
			cp steady/restart_flow.dat restart_flow_2.dat
			eval $copy0
			eval $copy1
			eval $copy2
			eval $command
			eval $move
			rm -rf *.vtu *.dat history*
		fi;
	done;
done;
