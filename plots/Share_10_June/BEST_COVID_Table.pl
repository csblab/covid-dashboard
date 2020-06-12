#!/usr/bin/perl

use strict;
no warnings 'syntax';

my ( $col, $i, $il, $key, $nc, $nl, $v1, $verbose, $frac, $n1,
     %vsort_h, 
     @c, @nbar, @t, @t0, @v, @vbar, @vbar2, @vmax, @vmin, @f05, @f95
    );

$_=$0;if(/\//){s/\/[^\/]+$//;@INC=($_,@INC);}
require "simple-io.plib.pl";

$verbose = &StringAfterOption("v","0");
$col = &StringAfterOption("c","1");

@c = split(/,/, $col);  $nc = $#c;

printf ( STDOUT "
  # Usage: histogram.pl -w<column width> -c<column number> < <input file>
  # Desc: Histogram column specified with width specified
  # Desc: Last editted 3Jun97.
");

# cycle over the log files

# Read in the *.best files
#AAA2     1 Sweden Confirmed cc1=  .936596 cc2=  .635080 lx=  6.60840 if=  30 il=  40 3/2/2020   n=  10 now=   44730 end=        819        15       826 tc=    19.3 T=   66.8 p1= -98.2 p2=  5461.5 ed=   112 5/13/2020   x1=  30. x2=  40. y1=  1.90 y2=  1.39 BEST

for ( $i = 0; $i <= $nc; $i++ ) { 
    $vmax[$i] = -10000000; $vmin[$i] = -$vmax[$i];
    $vbar[$i] = 0; $vbar2[$i] = 0; $nbar[$i] = 0;
}

$nl = 0;
while ( <STDIN> ) {
    chop;
    if ( /^#/ || /^$/ ) { next }
    @t = split ( /[\t ]+/, $_ );
    if ( $#t < abs($c[$nc]) ) { next }
    if ( $nl == 0 ) { @t0 = @t }
    for ( $i = 0; $i <= $nc; $i++ ) { 
        if ( $verbose || $nl < 0 ) { printf ("%5d %5d %3d %10.4f line= '%s'\n", $i, $nl, $c[$i], $t[abs($c[$i])], $_ ) }
        $v1 = $t[abs($c[$i])];
        $v[$nl][$i] = $v1;
    }
    $nl++;
}

print "n = $nl, i = $i, vmin = @vmin\n";

# Get percentile limits by sorting
for ( $i = 0; $i <= $nc; $i++ ) {
 
    undef ( %vsort_h );
    for ( $il = 0; $il < $nl; $il++ ) { 
        $v1 = $v[$il][$i];
        $key = $v1+0.000000001*$il;
        $vsort_h{$key} = $il;
    }
    $n1 = 0; $f05[$i] = -99999.99999; $f95[$i] =  -99999.99999;
    foreach $v1 ( sort { $a <=> $b } ( keys ( %vsort_h ) ) ) { 
        $n1++;
        $frac = 100*$n1/$nl;
        if ( $f05[$i] == -99999.99999 && $frac > 5.00 ) { $f05[$i] = $v1 }
        if ( $f95[$i] == -99999.99999 && $frac > 95.0 ) { $f95[$i] = $v1 }
        #printf ( "sort: %2d %6.2f %10.5f %10.5f %10.5f\n", $i, $frac, $v1, $f05[$i], $f95[$i] );
        if ( $f05[$i] == -99999.99999 || $f95[$i] != -99999.99999 ) { next }

        $vbar[$i]  += $v1; $vbar2[$i] += $v1**2; $nbar[$i]++;
        if ( $vmax[$i] < $v1 ) { $vmax[$i] = $v1 }
        if ( $vmin[$i] > $v1 ) { $vmin[$i] = $v1 }
    }
}


print "nl = $nl, i = $i, vmin = @vmin\n";

for ( $i = 0; $i <= $nc; $i++ ) {
    if ( $nbar[$i] <= 0 ) { exit }
    $vbar[$i]  /= $nbar[$i]; $vbar2[$i] /= $nbar[$i];
    $vbar2[$i]  = sqrt ( abs($vbar2[$i] - $vbar[$i]**2) );
}

printf ( "STB: %-20s %3d %8.1f     ",$t0[0], $t0[2], 100.0*$nbar[0]/$nl );

$i = 0; printf ( "N= %7.0f %7.0f %7.0f %7.1f     ", $vbar[$i], $f05[$i], $f95[$i], $vbar2[$i] );
$i = 1; printf ( "u= %8.1f %8.1f %8.1f %8.1f     ", $vbar[$i], $f05[$i], $f95[$i], $vbar2[$i] );
$i = 2; printf ( "T= %6.1f %6.1f %6.1f %6.1f",$vbar[$i], $f05[$i], $f95[$i], $vbar2[$i] ); print "\n";

for ( $i = 0; $i <= $nc; $i++ ) {
    printf ( "STA: %-30s %2d %-6s %12.4f %12.4f %12.4f %12.4f  %5d %12.4f %12.4f \n",$t0[0]."_".$t0[1]."_".$t0[2]."_".$t0[3], $c[$i], @t0[$c[$i]-1], $vbar[$i], $f05[$i], $f95[$i], $vbar2[$i], $nbar[$i], $vmin[$i], $vmax[$i] )
}
