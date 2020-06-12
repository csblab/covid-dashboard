#!/bin/sh

# Process Step 2
# --------------
#cat Data_COVID-19_SMOO_UNSM_Space_Sep_data.txt.2.CURRENT | Process_JHU_COVID_v3_Step2_SEL.pl >  Process_JHU_COVID_v3_Step2_SEL.pl=.log
cat Data_COVID-19_SMOO_UNSM_Space_Sep_data.txt.2.CURRENT | Process_JHU_COVID_v3_Step2_SEL_World.pl >  Process_JHU_COVID_v3_Step2_SEL.pl=.log

# Make data for Andrea's plotting
# -------------------------------
echo.pl UNSM SMO1 SMO2 SMO3 SMO4 SMO5 | do_all "egrep '^DATE |^%% ' Process_JHU_COVID_v3_Step2_SEL.pl=.log | cut -c6-99999 > %%.csv"

cp -a UNSM.csv SMO[1-5].csv /Users/levitt/levitt/tmp/covid19-KEEP/covid19/output/
cp -a Data_COVID-19_v2.csv /Users/levitt/levitt/tmp/covid19-KEEP/covid19/output/

# cd /Users/levitt/levitt/tmp/covid19-KEEP/covid19/notebooks/01_plotting
# jupyter notebook COVID19-Data-Plotter_v7.ipynb
# or
# jupyter nbconvert --ExecutePreprocessor.timeout=9000 --execute COVID19-Data-Plotter_v7.ipynb

cat Process_JHU_COVID_v3_Step2_SEL.pl=.log | egrep '^DATE|^UNSM|^SMO1|^SMO2 |^SMO3 |^SMO4 |^SMO5' > All_Step2_SEL.csv

# Process Step 3
# --------------

cat All_Step2_SEL.csv | cut -c 6-9999 | Process_JHU_COVID_v3_Step3.pl | grep -v '^ML' | sed 's/Country_Region_Safe/Country_Region_Safe,Smoothing/' | sed 's/_SMO1/_SMO1,SMO1/' | sed 's/_SMO2/_SMO2,SMO2/' | sed 's/_SMO3/_SMO3,SMO3/' |sed 's/_SMO4/_SMO4,SMO4/' |sed 's/_SMO5/_SMO5,SMO5/' |sed 's/_UNSM/_UNSM,UNSM/' > Select_COVID_data_PEAKS.SEL.csv

# Make SEL data for Excel
# ----------------------
egrep '^Country|UNSM' Select_COVID_data_PEAKS.SEL.csv | sort -t"," -k8,8 -k1,1 > Select_COVID_data_PEAKS.UNSM.SEL.csv 
cp -a Select_COVID_data_PEAKS.UNSM.SEL.csv ~/win1

# Make text table
# --------------
egrep 'Smoothing|SMO5' Select_COVID_data_PEAKS.SEL.csv | egrep '^Country|Confirmed' | cut -d"," -f2,3,11,13-15,20-22,26 | sed 's/,/ /g' | tokens_tabulate.pl | sort -k3,3r -k5,5n > Select_COVID_data_PEAKS.SEL.table

# Deploy SEL data with old name
# -----------------------------
cp -a Select_COVID_data_PEAKS.SEL.csv covid19/April_28_2020/covid-app-deploy/data/Select_COVID_data_PEAKS.csv
cp -a Select_COVID_data_PEAKS.SEL.csv ~/Dropbox/covid19_data_conduit/Select_COVID_data_PEAKS.csv

# Make data for Andrea's app using SEL data
# -----------------------------------------
cat Select_COVID_data_PEAKS.SEL.csv | egrep -v 'SMO1|SMO2|SMO4' | grep -v '^ML|missing' > Select_COVID_data_PEAKS.1.SEL.csv
cp -a Select_COVID_data_PEAKS.1.SEL.csv ~/Dropbox/covid19_data_conduit/Select_COVID_data_PEAKS.1.csv

# Get data for Andrea's plotter_for_Michael_v1.ipynb
# --------------------------------------------------
cp -a Select_COVID_data_PEAKS.1.SEL.csv /Users/levitt/levitt/tmp/covid19-KEEP/covid19/notebooks/data/Select_COVID_data_PEAKS.csv
cp -a Select_COVID_data_PEAKS.1.ALL.csv /Users/levitt/levitt/tmp/covid19-KEEP/covid19/notebooks/data/Select_COVID_data_PEAKS.csv



# Repeat what was done for SEL data for ALL data
# ==============================================
# Process Step 2
# --------------
cat Data_COVID-19_SMOO_UNSM_Space_Sep_data.txt.2.CURRENT | Process_JHU_COVID_v3_Step2_ALL_World.pl >  Process_JHU_COVID_v3_Step2_ALL.pl=.log

cat Process_JHU_COVID_v3_Step2_ALL.pl=.log | egrep '^DATE|^UNSM|^SMO1|^SMO2 |^SMO3 |^SMO4 |^SMO5' > All_Step2_ALL.csv

# Process Step 3
# --------------

cat All_Step2_ALL.csv | cut -c 6-9999 | Process_JHU_COVID_v3_Step3.pl | egrep 'Country|UNSM|SMO' | sed 's/Country_Region_Safe/Country_Region_Safe,Smoothing/' | sed 's/_SMO1/_SMO1,SMO1/' | sed 's/_SMO2/_SMO2,SMO2/' | sed 's/_SMO3/_SMO3,SMO3/' |sed 's/_SMO4/_SMO4,SMO4/' |sed 's/_SMO5/_SMO5,SMO5/' |sed 's/_UNSM/_UNSM,UNSM/' | grep -v missing > Select_COVID_data_PEAKS.ALL.csv

# Make AKK data for Excel
# ----------------------
egrep '^Country|UNSM' Select_COVID_data_PEAKS.ALL.csv | sort -t"," -k8,8 -k1,1 > Select_COVID_data_PEAKS.UNSM.ALL.csv  
cp -a Select_COVID_data_PEAKS.UNSM.ALL.csv ~/win1

# Make text table
egrep 'Smoothing|SMO5' Select_COVID_data_PEAKS.ALL.csv | egrep '^Country|Confirmed' | cut -d"," -f2,3,11,13-15,20-22,26 | sed 's/,/ /g' | tokens_tabulate.pl | sort -k3,3r -k5,5n > Select_COVID_data_PEAKS.ALL.table

cp -a Select_COVID_data_PEAKS.ALL.csv /Users/levitt/levitt/tmp/covid19-KEEP/covid19/notebooks/data/Select_COVID_data_PEAKS.csv

# Sanity checks
cat Select_COVID_data_PEAKS.SEL.csv | number_tokens_comma.pl | grep 'Line' | cut -d" " -f5 | sort | uniq -c
cat Select_COVID_data_PEAKS.SEL.csv | head -1 | number_tokens_comma.pl | tail -1

exit
