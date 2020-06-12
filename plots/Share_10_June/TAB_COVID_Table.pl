#!/usr/bin/perl

use strict;
no warnings 'syntax';

my ( $i, $il, $nt, $name, $nl, $p1, $verbose, $n1, $s1, $s2, $sd,
     $frac, $np, $pav, $limit, $i_limit, $mode, $il_OK,
     @data, @t, @err, @rat, @mode_k
    );

$_=$0;if(/\//){s/\/[^\/]+$//;@INC=($_,@INC);}
require "simple-io.plib.pl";

#"TAB:  Korea_South Deaths    Dates Day  Current   Real     MAX  Predict    Count      Min      Max      Med" 

# Set "Start_Day" as day when number of cases (or deaths) exceeds some threshold (100 for cases, 20 for deaths).  
# Also calculate the "Final_Prediction" as the average prediction for the last five days.  
# If is has a small, SD, score all the earlier predictions  and plot the %error vs Start_Day.  
# Does this make sense?  There are many *.tab files in the dropbox.  I could look as all locations that are classified as "cCdD"

$verbose = &StringAfterOption("v","0");

printf ( STDOUT "
  # Process COVID TAB data
");

# cycle over the TAB files

#TAB:  Sweden Confirmed      Date   Day     Real      MAX  Predict    Count      Min      Max      Med
#TAB:  Sweden Confirmed 1/23/2020     1        0    44730        0        0        0        0        0
#   0       1         2         3              5        6        7        8        9       10       11
#TAB:  Sweden Confirmed .           136    43887    44730    53708       19    53708   296634    81801
#TAB:  Sweden Confirmed 6/7/2020    137    44730    44730    55360       15    53708   308202    81801

$nl = 0; $i_limit = 0;
$limit = 20;  # default for Deaths
while ( <STDIN> ) {
    chop;
    if ( /^#/ || /^$/ || /MAX/ ) { next }
    @t = split ( / +/, $_ ); $nt = $#t; 
    if ( / Confirmed/ ) { $limit = 100 }
    for ( $i = 0; $i <= $nt; $i++ ) { $data[$i][$nl] = $t[$i] }
    if ( $data[5][$nl] > $limit && !$i_limit) { $i_limit = $nl }
    $nl++;
}
$name = $data[1][0]."=".$data[2][0];
# print "$name nl = $nl, nt = $nt\n";

# Get everage and SD of last 5 Predict values ($t[7])
$s1 = 0; $s2 = 0; $n1 = 0;
#for ( $il = $nl-5; $il < $nl; $il++ ) {
for ( $il = $nl; $il >= 0; $il-- ) {
    $p1 = $data[7][$il];
    if ( !$p1 ) { next }
    print "p1= $p1 il= $il\n";
    $s1  += $p1; $s2 += $p1**2; $n1++;
    if ( $n1 == 5 ) { last }
}
if ( $n1 <= 0 ) { print STDERR "$name n1 is zero so STOP\n"; exit }

$s1 /= $n1; $s2 /= $n1; $sd = sqrt(abs($s2-$s1*$s1));
if ( $s1 <= 0 ) { print STDERR "$name s1 is zero so STOP\n"; exit }
$frac = 100*$sd/$s1;
print "$name nl = $nl, n1= $n1 s1= $s1 s2= $s2 SD= $sd frac%= $frac\n";
$pav = $s1;

$il_OK = 0;
for ( $il = 0; $il < $nl; $il++ ) {
    $p1 = $data[7][$il];
    if ( $p1 ) { 
        $err[$il] = 100*( $p1 - $pav )/$pav;
        $rat[$il] = 100*( $p1/$pav );
        $np++;
        $mode = "  "; if ( abs($err[$il]) < 15.0 ) { $mode = "OK"; if ( !$il_OK ) { $il_OK = $il; $mode = "OK 1st" } }
        $mode_k[$il] = $mode;
        printf ( "%s i: %3d %3d %3d %10s p: %7d %7d e: %5.1f r: %5.1f %s\n",$name, $il, $il-$il_OK, $il-$i_limit+1, $data[3][$il], $p1, $pav, $err[$il], $rat[$il], $mode );
    }
}
