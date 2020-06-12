cat ../Select_COVID_data_PEAKS.ALL.table | sort -k7nr | sed 's/_SMO5//' | cut -d" " -f1 | list_lines_n:m.pl 1:600 | do_all "Make_plot_00.sh %%"

cat ../Select_COVID_data_PEAKS.ALL.table | sort -k7nr | sed 's/_SMO5//' | cut -d" " -f1 | list_lines_n:m.pl 1:600 | do_all "Make_plot_20.sh %%"

cat ../Select_COVID_data_PEAKS.ALL.table | sort -k7nr | sed 's/_SMO5//' | cut -d" " -f1 | list_lines_n:m.pl 1:600 | do_all "Make_plot_40.sh %%"

