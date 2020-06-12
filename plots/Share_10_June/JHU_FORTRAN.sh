#!/bin/sh

egrep 'Country' Select_COVID_data_PEAKS.ALL.csv | cut -d"," -f1,8,13,20,27-999 | sed 's/,,/,0,/g' | sed 's/,,/,0,/g' | sed 's/,/ /g' > step0a.tmp
egrep 'UNSM' Select_COVID_data_PEAKS.ALL.csv | cut -d"," -f1,8,13,20,27-999 | sed 's/,,/,0,/g' | sed 's/,,/,0,/g' | sed 's/,/ /g' | sed 's/__Federal_Correctional_Institution_FCI//' | sed 's/__Michigan_Department_of_Corrections_MDOC//' > step0b.tmp
cat step0a.tmp step0b.tmp >  step1.tmp

egrep 'Country|UNSM' Select_COVID_data_PEAKS.ALL.csv | cut -d"," -f1,8,13,20,27-999 | sed 's/,,/,0,/g' | sed 's/,,/,0,/g' | sed 's/,/ /g' | sed 's/__Federal_Correctional_Institution_FCI//' | sed 's/__Michigan_Department_of_Corrections_MDOC//' > step1T.tmp

diff step1.tmp step1T.tmp


cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_00.tmp
cat step2_00.tmp | head -2
cp -a step2_00.tmp Select_COVID_data_PEAKS.UNSM.ALL._00.ftxt

cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t-10;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_10.tmp
cat step2_10.tmp | head -2
cp -a step2_10.tmp Select_COVID_data_PEAKS.UNSM.ALL._10.ftxt

cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t-20;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_20.tmp
cat step2_20.tmp | head -2
cp -a step2_20.tmp Select_COVID_data_PEAKS.UNSM.ALL._20.ftxt

cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t-30;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_30.tmp
cat step2_30.tmp | head -2
cp -a step2_30.tmp Select_COVID_data_PEAKS.UNSM.ALL._30.ftxt

cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t-40;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_40.tmp
cat step2_40.tmp | head -2
cp -a step2_40.tmp Select_COVID_data_PEAKS.UNSM.ALL._40.ftxt

cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t-50;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_50.tmp
cat step2_50.tmp | head -2
cp -a step2_50.tmp Select_COVID_data_PEAKS.UNSM.ALL._50.ftxt

cat  step1.tmp | perl  -ne 'chop;@t=split(/ +/,$_);$n=$#t-90;printf("%4d %3d %-55s %-9s", $n, length($t[0]), substr($t[0],0,55), $t[1]);for($i=2;$i<=$n;$i++){printf(" %8s",$t[$i])};print"\n"' > step2_90.tmp
cat step2_90.tmp | head -2
cp -a step2_90.tmp Select_COVID_data_PEAKS.UNSM.ALL._90.ftxt

exit
