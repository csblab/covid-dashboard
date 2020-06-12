set terminal pngcairo  transparent enhanced font "arial,20" fontscale 1.0 size 1200, 900 
set output 'BL_lines.png'

set key top left
set key spacing 1.2 font ",12" w 2 noenhanced
set key box opaque

set style increment default
set datafile missing '-'
set style data linespoints

set xtics border in scale 1,0.5 nomirror rotate by 0 autojustify
set xtics  norangelimit 
set xtics   ()

set title "Best Line Fits Italy" font ",32"
set xlabel "Day Count from 23 Jan 2020" font ",24"
set ylabel "Scaled ( X20) G(t) = ln( ln(N)-ln(X(t)) )" font ",24"

set xrange [0:150] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [-50:100] noreverse writeback
set y2range [ * : * ] noreverse writeback


plot for [i=6:106:2] 'input._50.bl' using 2:i w l lw 2 lc 2 title columnheader(i+1), 'input.bl' using 2:6 w p lw 2 pt 6 ps 2 lc 1 title columnheader(6)
#plot for [i=6:100:2] 'input._50.bl' using 2:i w l lw 2 lc 2 title columnheader(i), 'input.bl' using 2:6 w p pt 6 ps 2 title columnheader(6)
#plot 'input.bl' using 2:6 w p pt 6 ps 2 title columnheader(6), for [i=6:100:2] 'input._50.bl' using 2:i w l lw 2 lc 2 title columnheader(i)
#plot 'input._40.bl' using 2:6 w lp lw 4 title columnheader(6), for [i=6:1001:40] '' using 2:i w l lw 2 title columnheader(i)
