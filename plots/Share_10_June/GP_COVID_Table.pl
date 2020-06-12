#!/usr/bin/perl

use strict;
no warnings 'syntax';

my ( $col, $i, $il, $key, $keyp, $nc, $nl, $v1, $verbose, $n1, $err,
     @c, @nbar, @t, @t0, @v, @vbar, @vbar2, @vmax, @vmin,
    );

$_=$0;if(/\//){s/\/[^\/]+$//;@INC=($_,@INC);}
require "simple-io.plib.pl";

$verbose = &StringAfterOption("v","0");

printf ( STDOUT "
  # Usage: histogram.pl -w<column width> -c<column number> < <input file>
  # Desc: Histogram column specified with width specified
  # Desc: Last editted 3Jun97.
");

# Read in the data from GP file
#GP: Confirmed Sweden Dates           Day     Max  Predict Current    Bpred  Count eDay EndDate
#GP: Confirmed Sweden 6/7/2020        137   44730    -       44730    55360    15   495 5/31/2021 

$col = "4,5,6"; @c = split(/,/, $col);  $nc = $#c;

$nl = 0;
while ( <STDIN> ) {
    chop;
    if ( /^#/ || /^$/ || !/GP:/ ) { next }
    @t = split ( /[\t ]+/, $_ );
    if ( $#t < abs($c[$nc]) ) { next }
    if ( $nl == 1 ) { @t0 = @t }
    $v[$nl][0] = $t[1]."_".$t[2]." ".sprintf(" %3d",$t[4]);  # this key
    for ( $i = 0; $i <= $nc; $i++ ) { 
        $v1 = $t[abs($c[$i])];
        $v[$nl][$i] = $v1;
    }

    if ( $verbose || $nl < 0 ) { printf ("%5d %5d %3d %10.4f line= '%s'\n", $i, $nl, $c[$i], $t[abs($c[$i])], $_ ) }

    $nl++;
}
# Add 1 for key
# $nc++;
print "n = $nl, nc= $nc i = $i, vmin = @vmin t0= @t0\n";

# Get average for each ilp value
$keyp = "";
for ( $il = 0; $il <= $nl; $il++ ) { 
    if ( $il < $nl ) { $key = $v[$il][0] }
    print "key= $key il= $il\n";
    if ( $key ne $keyp || $il == $nl ) { 
	if ( $keyp || $il >= $nl ) { 
            for ( $i = $nc; $i <= $nc; $i++ ) {
                if ( $nbar[$i] <= 0 ) { next }
                $vbar[$i]  /= $nbar[$i]; $vbar2[$i] /= $nbar[$i];
                $vbar2[$i]  = sqrt ( abs($vbar2[$i] - $vbar[$i]**2) );
            }
            $i = 2; 
            $err =  $vbar[$i] - $t0[5];
            printf ( "STC: %-20s %6d  %4d %8d  %7.0f %7.1f %7.0f %7.0f  e: %7d\n", $keyp, $nl, $nbar[$i], $t0[5], $vbar[$i], $vbar2[$i], $vmin[$i], $vmax[$i], $err );
            
	}   # if keyp
       for ( $i = $nc; $i <= $nc; $i++ ) { 
          $vmax[$i] = -10000000; $vmin[$i] = -$vmax[$i]; $vbar[$i] = 0; $vbar2[$i] = 0; $nbar[$i] = 0;
       }
    }

    $keyp = $key;

    for ( $i = $nc; $i <= $nc; $i++ ) {
        $v1 = $v[$il][$i];
        print "TE: $il $i $v1\n";
        $vbar[$i] += $v1; $vbar2[$i]+= $v1**2; $nbar[$i]++;
        if ( $vmax[$i]< $v1 ) { $vmax[$i]= $v1 }
        if ( $vmin[$i]> $v1 ) { $vmin[$i]= $v1 }
    }
}


