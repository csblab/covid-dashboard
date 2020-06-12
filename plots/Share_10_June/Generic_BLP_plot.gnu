set terminal pngcairo  transparent enhanced font "arial,20" fontscale 1.0 size 2000, 900 
set output 'LOCATION_TYPE_VERSION_plot2.png'

set key  bottom right
set key spacing 2. font ",16" w 2
set key box opaque

set style increment default
set datafile missing '-'
set xtics border 1,0.5 rotate by -90 autojustify font ",14"
set ytics nomirror
set y2tics nomirror

set title "Predicted TYPE LOCATION DATE" noenhanced font ",24"
set ylabel "Total Number of TYPE" font ",24"
set y2label "U Value (=1/K) in days" font ",24"

set xrange [0:140] noreverse writeback
set yrange [ * : * ] noreverse writeback
set y2range [0:30] noreverse writeback

set grid ytics lt 0 lw 1 lc rgb "black"
set grid xtics lt 0 lw 1 lc rgb "black"

set style line 1 lc rgb '#ff0000' pt 6 ps 1.5 lt 1 lw 2 dt 2 # --- red
set style line 3 lc rgb '#0000ff' pt 6 ps 3 lt 1 lw 2        # --- blue
set style line 2 lc rgb 'black'   pt 6 ps 2 lt 1 lw 3        # --- black
set style line 4 lc rgb 'brown'   pt 6 ps 4 lt 1 lw 2        # --- brown

#TAB:  US_New_York_NYC Deaths    6/1/2020    131    21607    21607    21837       10    21837    22945    22452
#  1                 2     3             4     5        6        7        8        9       10       11       12
#GP: Deaths    US_New_York_NYC 6/1/2020        131   21607   24606   21607   21837    10   150 6/20/2020 
#  1      2                  3        4          5       6       7       8       9     10   11        12

plot 'input.tab' u 5:6:xtic(4) w lp ls 2 title "Actual TYPE" axes x1y1,  \
     ''          u 5:7   w l ls 1 title "Maximum to Date",  \
     ''          u 5:8   w p ls 4 pt 4 ps 3. title "Select Predicted", \
     'input.gp'  u 5:7   w p ls 3 ps .4 title "All Predicted",  \
     'input.bes' u 14:25 w p ls 1 title "U Value (=1/K) in days" axes x1y2