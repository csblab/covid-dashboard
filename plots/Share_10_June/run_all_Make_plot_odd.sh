cat ../Select_COVID_data_PEAKS.ALL.table | sort -k7nr | sed 's/_SMO5//' | cut -d" " -f1 | list_lines_n:m.pl 1:30 | do_all "Make_plot_10.sh %%"

cat ../Select_COVID_data_PEAKS.ALL.table | sort -k7nr | sed 's/_SMO5//' | cut -d" " -f1 | list_lines_n:m.pl 1:30 | do_all "Make_plot_30.sh %%"

cat ../Select_COVID_data_PEAKS.ALL.table | sort -k7nr | sed 's/_SMO5//' | cut -d" " -f1 | list_lines_n:m.pl 1:30 | do_all "Make_plot_50.sh %%"