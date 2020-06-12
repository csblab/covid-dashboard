set terminal pngcairo  transparent enhanced font "arial,20" fontscale 1.0 size 2000, 900 
set output 'LOCATION_TYPE_VERSION_KTL.png'

set key bottom right
set key spacing 2. font ",16" w 2
set key box opaque

set style increment default
set datafile missing '-'
set xtics border 1,0.5 rotate by -90 autojustify font ",14"
set ytics nomirror
set y2tics nomirror

set title "Predicted TYPE LOCATION DATE" noenhanced font ",24"
set ylabel "Predicted K, T, End-Day for TYPE" font ",24"
set y2label "Total Number of TYPE" font ",24"

set xrange [0:140] noreverse writeback
set y2range [ * : * ] noreverse writeback
set yrange [0:150] noreverse writeback
set y2range [ * : * ] noreverse writeback

set grid ytics lt 0 lw 1 lc rgb "black"
set grid xtics lt 0 lw 1 lc rgb "black"

set style line 1 lc rgb 'black'   pt 6 ps 2 lt 1 lw 3   # --- black
set style line 2 lc rgb '#ff0000' pt 6 ps 1 lt 1 lw 2   # --- red
set style line 3 lc rgb '#0000ff' pt 6 ps 2 lt 1 lw 2   # --- blue
set style line 4 lc rgb '#00aa00' pt 6 ps 2 lt 1 lw 2   # --- dark green

#TAB:  US_New_York_NYC Deaths    Dates Day  Current   Real     MAX  Predict    Count      Min      Max      Med
#TAB:  US_New_York_NYC Deaths    6/1/2020    131    21607    21607    21837       10    21837    22945    22452
#  1                 2     3             4     5        6        7        8        9       10       11       12

 plot 'input.tab' u 5:6:xtic(4) w lp ls 1 title "Actual TYPE on y2-axis" axis x1y2, \
      'input.bes' u 14:(5*($25)) w p ls 2 title "U Value (=1/K) in day Value X5", \
       ''         u 14:27 w p ls 3 title "T Value",  \
       ''         u 14:33 w p ls 4 title "End-Day"

