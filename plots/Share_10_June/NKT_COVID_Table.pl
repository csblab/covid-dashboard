#!/usr/bin/perl

use strict;
no warnings 'syntax';

my ( $col, $i, $il, $key, $keyp, $nc, $nl, $v1, $verbose, $n1, $n,
     $line, $s1, $s2, $s3, $s4, $aa, $ilp,
     @c, @nbar, @t, @t0, @v, @vbar, @vbar2, @vmax, @vmin,
    );

$_=$0;if(/\//){s/\/[^\/]+$//;@INC=($_,@INC);}
require "simple-io.plib.pl";

$verbose = &StringAfterOption("v","0");

# Read in the data from *.best file
#AAA2     1 Sweden Confirmed cc1=  .936596 cc2=  .635080 lx=  6.60840 if=  30 il=  40 3/2/2020   n=  10 now=   44730 end=        819        15       826 tc=    19.3 T=   66.8 p1= -98.2 p2=  5461.5 ed=   112 5/13/2020   x1=  30. x2=  40. y1=  1.90 y2=  1.39 BEST

$col = "13,16,24"; @c = split(/,/, $col);  $nc = $#c;

$nl = 0;
while ( <STDIN> ) {
    chop;
    if ( /^#/ || /^$/ ) { next }
    @t = split ( /[\t ]+/, $_ );
    if ( $#t < abs($c[$nc]) ) { next }
    if ( $nl == 1 ) { @t0 = @t }
    for ( $i = 0; $i <= $nc; $i++ ) { 
        $v1 = $t[abs($c[$i])];
        $v[$nl][$i] = $v1;
        if ( $verbose || $nl < 0 ) { printf ("%5d %5d %3d %10.4f line= '%s'\n", $i, $nl, $c[$i], $t[abs($c[$i])], $_ ) }
    }
    $v[$nl][0] = $t[2]."_".$t[3]." ".sprintf(" %3d",$t[13]);  # this key

    $nl++;
}
# Add 1 for key
# $nc++;
print "ML: n = $nl, nc= $nc i = $i, vmin = @vmin t0= @t0\n";

# Get average for each ilp value
$keyp = "";
for ( $il = 0; $il <= $nl; $il++ ) { 

    if ( $il < $nl ) { $key = $v[$il][0] }; if ( 0 ) { print "key= '$key' '$keyp' il= $il\n" }
    if ( $il == 0 ) { 
        ($aa,$ilp) = split(/ +/,$key );
        
        print "AAAAAA ilp= $ilp\n"; $line = sprintf("STX: DATE: %s ", $aa);
        # Pad line so it starts at Day 1
        if ( $ilp > 0 ) { for ( $i = 1; $i < $ilp; $i++ ) { $line = $line.sprintf("   -    ") } }
    }

    if ( $key ne $keyp || $il == $nl ) { 
	if ( $keyp || $il >= $nl ) { 
            for ( $i = $nc; $i <= $nc; $i++ ) {
                if ( $nbar[$i] <= 0 ) { next }
                $vbar[$i]  /= $nbar[$i]; $vbar2[$i] /= $nbar[$i];
                $vbar2[$i]  = sqrt ( abs($vbar2[$i] - $vbar[$i]**2) );
            }

            $i = 2; 
            $s1 = sprintf ( "%7.1f", $vbar[$i] );
	    $s2 = sprintf ( "%7.1f", $vbar2[$i] ); if ( $vbar2[$i] <= 0 ) { $s2 = "-" }
            $s3 = sprintf ( "%7.1f", $vmin[$i] );
            $s4 = sprintf ( "%7.1f", $vmax[$i] );

            if ( $nbar[$i] == 0 ) { $s1 = "-";  $s2 = "-";  $s3 = "-";  $s4 = "-" }
            printf ( "STC: %-20s %6d  %4d %7s %7s %7s %7s\n", $keyp, $nl, $nbar[$i], $s1, $s2, $s3, $s4 );

            $line = $line.sprintf(" %7s",$s1);

	}   # if keyp

       for ( $i = $nc; $i <= $nc; $i++ ) { 
           $vmax[$i] = -10000000; $vmin[$i] = -$vmax[$i]; $vbar[$i] = 0; $vbar2[$i] = 0; $nbar[$i] = 0;
       }
    }

    $keyp = $key;

    $n =  $v[$il][$nc-1];
    if ( $n > 15 ) { 
        for ( $i = $nc; $i <= $nc; $i++ ) {
            $v1 = $v[$il][$i];
        
            # print "TE: $il $i $v1\n";
            $vbar[$i] += $v1; $vbar2[$i]+= $v1**2; $nbar[$i]++;
            if ( $vmax[$i]< $v1 ) { $vmax[$i]= $v1 }
            if ( $vmin[$i]> $v1 ) { $vmin[$i]= $v1 }
	}
    }
}

print "$line\n";


