#!/bin/sh

echo $1

country=$1
dat1=`date +%d`; dat2=`date +%b`; dat3=`date +%Y`
date=$dat1"-"$dat2"-"$dat3
country=`echo $1|sed "s/_/ /"`
echo $country $date

cat ../Select_COVID_data_PEAKS.UNSM.ALL._50.ftxt | egrep "Country|$1 " | best_fit_line.new.exe > $1._50.log


cat $1._50.log | grep '^GP: '  | grep Confirmed > $1_Confirmed._50.gp
cat $1._50.log | grep '^GP: '  | grep Deaths    > $1_Deaths._50.gp

cat $1._50.log | grep '^TAB: ' | grep Confirmed > $1_Confirmed._50.tab
cat $1._50.log | grep '^TAB: ' | grep Deaths    > $1_Deaths._50.tab

cat $1._50.log | grep BEST | grep AAA2 | grep Confirmed | sort -k14n | NKT_filter_COVID_Table.pl > $1_Confirmed._50.best
cat $1._50.log | grep BEST | grep AAA2 | grep Deaths    | sort -k14n | NKT_filter_COVID_Table.pl > $1_Deaths._50.best

rm input.gp ; ln -s $1_Confirmed._50.gp input.gp     ; rm input.tab ; ln -s $1_Confirmed._50.tab input.tab 
cat Generic_BLP_plot.gnu | sed "s/LOCATION/$1/" | sed "s/TYPE/Confirmed/" | sed "s/DATE/$date/" | sed "s/VERSION/_50/" | gnuplot 

rm input.gp ; ln -s $1_Deaths._50.gp input.gp        ; rm input.tab ; ln -s $1_Deaths._50.tab input.tab 
cat Generic_BLP_plot.gnu | sed "s/LOCATION/$1/" | sed "s/TYPE/Deaths/"    | sed "s/DATE/$date/" | sed "s/VERSION/_50/" | gnuplot 

rm input.bes ; ln -s $1_Confirmed._50.best input.bes ; rm input.tab ; ln -s $1_Confirmed._50.tab input.tab 
cat Generic_BLP_plot.KTL.gnu | sed "s/LOCATION/$1/" | sed "s/TYPE/Confirmed/" | sed "s/DATE/$date/" | sed "s/VERSION/_50/" | gnuplot 

rm input.bes ; ln -s $1_Deaths._50.best input.bes    ; rm input.tab ; ln -s $1_Deaths._50.tab input.tab 
cat Generic_BLP_plot.KTL.gnu | sed "s/LOCATION/$1/" | sed "s/TYPE/Deaths/"    | sed "s/DATE/$date/" | sed "s/VERSION/_50/" | gnuplot 

# open $1_Deaths__50_plot.png
# open $1_Confirmed__50_plot.png

exit
