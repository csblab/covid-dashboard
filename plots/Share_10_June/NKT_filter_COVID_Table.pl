#!/usr/bin/perl

use strict;
no warnings 'syntax';

my ( $col, $i, $nc, $nl, $verbose, $n, $lin1,
     @c, @t, @v1
    );

$_=$0;if(/\//){s/\/[^\/]+$//;@INC=($_,@INC);}
require "simple-io.plib.pl";

$verbose = &StringAfterOption("v","0");

# Read in the data from best file
$col = "18,20"; @c = split(/,/, $col);  $nc = $#c;
#AAA2     1 US_New_York_NYC Deaths    cc1=  .999446 cc2=  .697935 lx=  7.75637 if=  51 il=  61 3/23/2020  n=  10 now=   21362 end=       2343       328      2346 tc=     7.8 T=   66.3 p1= -89.0 p2=   911.7 ed=    84 4/15/2020   x1=  51. x2=  61. y1=  1.96 y2=   .68 BEST
#   0     1                      2       3        4    5        6   7        8   9  10 11   12        13  14  15   16      17   18         19        20        21 22       23
$nl = 0;
while ( <STDIN> ) {
    $lin1 = $_;
    chop;
    if ( /^#/ || /^$/ ) { next }
    @t = split ( /[\t ]+/, $_ );
    if ( $#t < abs($c[$nc]) ) { next }
    for ( $i = 0; $i <= $nc; $i++ ) { 
        $v1[$i] = $t[abs($c[$i])];
        # print "nl $nl i $i $c[$i] v1[$i] $v1[$i]\n";
    }
    if ( $v1[1] < 0.99*$v1[0] ) { print "$lin1" }
    $nl++;
}
