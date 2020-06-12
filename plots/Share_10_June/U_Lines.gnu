set terminal pngcairo  transparent enhanced font "arial,20" fontscale 1.0 size 1200, 900 
set output 'U_lines.png'

set key bottom left
set key spacing 1.2 font ",12" w 2 noenhanced
set key box opaque

set style increment default
set datafile missing '-'
set style data linespoints

set xtics border in scale 1,0.5 nomirror rotate by 0 autojustify
set xtics  norangelimit 
set xtics   ()

set title "U (tau) Values of Deaths Countries of Interest" font ",32"
set xlabel "Day Count from 23 Jan 2020" font ",24"
set ylabel "U (tau) Value in days" font ",24"

set xrange [0:150] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [* : * ] noreverse writeback
set y2range [ * : * ] noreverse writeback

plot for [i=2:7] 'LockDown_K_Deaths.gp1' using 1:i w lp lw 2 title columnheader(i)

