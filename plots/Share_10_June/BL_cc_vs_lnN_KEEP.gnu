set terminal pngcairo  transparent enhanced font "arial,20" fontscale 1.0 size 1200, 900 
set output 'CC_vs_lnN.png'

set key top right
set key spacing 1.5 font ",14" w 2
set key box opaque

set style increment default
set datafile missing '-'
set style data linespoints

set xtics border in scale 1,0.5 nomirror rotate by 0 autojustify
set xtics  norangelimit 
set xtics   ()

set title "Correlation Coefficient vs. lnN" font ",32"
set ylabel "Correlation Coefficient" font ",24"
set xlabel "ln(N) Value" font ",24"

set xrange [12.36:12.42] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [0.998:1.0] noreverse writeback
set y2range [ * : * ] noreverse writeback


plot 'input.OOO' using 8:5 w l lw 4 title "Correlation Coefficient"
