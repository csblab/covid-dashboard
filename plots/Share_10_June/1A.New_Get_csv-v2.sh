#!/bin/sh

# Copy the primary data file dropboxfrom Dropbox
# ----------------------------------------------
curl https://raw.githubusercontent.com/csblab/covid19-data/master/output/Data_COVID-19.csv > Data_COVID-19.csv 
cp -a  Data_COVID-19.csv /Users/levitt/levitt/tmp/covid19-KEEP/covid19/output 

cp -a /Users/levitt/Dropbox/covid19_data_conduit/Data_COVID-19_v2.csv .

# Fix the file
# ------------
cat Data_COVID-19_v2.csv | perl -i.bk -pe 's/[^[:ascii:]]//g;' | sed 's/, /__/g' | sed 's/ /_/g' | sed "s/'//g" | sed 's/"//g' | sed 's/(/_/g' | sed 's/)/_/g' | sed 's/^US,US,New_York,New_York,New_York,New_York/US,US,New_York,New_York,New_York,NYC/' > Data_COVID-19_v2_FIX.csv

# Sanity checks on key csv file
# -----------------------------
cat Data_COVID-19_v2_FIX.csv | number_tokens_comma.pl | grep 'Line' | cut -d" " -f5 | sort | uniq -c
cat Data_COVID-19_v2_FIX.csv | head -1 | number_tokens_comma.pl | tail -1

# Process Step 1
# --------------
Process_JHU_COVID_v3_Step1.pl > Process_JHU_COVID_v3_Step1=.log

cat Process_JHU_COVID_v3_Step1=.log | egrep '^DATES|^Country|Confirmed|Deaths' > Data_COVID-19_SMOO_UNSM_Space_Sep_data.txt.2.CURRENT

exit
