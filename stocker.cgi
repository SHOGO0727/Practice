#! /usr/bin/perl

print "Content-type: text/plain\n\n";

use CGI;

my $input = $ENV{'QUERY_STRING'};
my @inputPairs = split('&',$input);
my @name;
my @value;
my $aaa;
my $num;
my @rname;
my @rnum;
my $aaa=1;
my $chch=0;
my $cnt=0;

for(my $i=0; $i<@inputPairs+1; $i++){
  ($name[$i],$value[$i]) = split('=',$inputPairs[$i]);
}

my @ch = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
for(my $i=2;$i<=3;$i++){
  $cnt=0;
  if($value[$i]){
    my @c = split //, $value[$i];
    $lng = length $value[$i];
    for(my $j=0;$j<$lng;$j++){
      for(my $k=0;$k<10;$k++){
        if($c[$j] eq $ch[$k]){
          $cnt++;
        }
      }
    }
    if($cnt != $lng){
      $chch = 1;
    }
  }
}
if($chch==1){
  print "ERROR";
}
else{
if($value[0] eq 'addstock'){
#############################################
if($value[2]){$num = $value[2];}
else{$num = 1;}

open(READ,"< nmvl.txt");
my @read = <READ>;
chomp (@read);
for(my $i=0; $i<@read; $i++){
  ($rname[$i],$rnum[$i]) = split('=',$read[$i]);
  if($rname[$i] eq $value[1]){
    $rnum[$i] = $rnum[$i] + $num;
    $aaa=0;
  }
}
close(READ);
open(OWRITE,"> nmvl.txt");
if(@read){
  for(my $i=0; $i<@read; $i++){
    print OWRITE $rname[$i],"=","$rnum[$i]\n";
  }
  if($aaa==1){
    print OWRITE $value[1],"=","$num\n";
  }
}
else{
  print OWRITE $value[1],"=",$num;
}
close(OWRITE);
#############################################
}

if($value[0] eq 'checkstock'){
#############################################
open(READ,"< nmvl.txt");
my @read = <READ>;
@read = sort {$a cmp $b} @read;
chomp (@read);
if($value[1]){
  for(my $i=0; $i<@read; $i++){
    ($rname[$i],$rnum[$i]) = split('=',$read[$i]);
    if($rname[$i] eq $value[1]){
      print $rname[$i],": ",$rnum[$i];
    }
  }
}
else{
  for(my $i=0; $i<@read; $i++){
    ($rname[$i],$rnum[$i]) = split('=',$read[$i]);
    if($rnum[$i]!=0){
      print $rname[$i],": ","$rnum[$i]\n";
    }
  }
  }
#############################################
}

if($value[0] eq 'sell'){
#############################################
if($name[2]eq"amount"){$num = $value[2];}
else{$num = 1;}

###stock##################
open(READ,"< nmvl.txt");
my @read = <READ>;
chomp (@read);
for(my $i=0; $i<@read; $i++){
  ($rname[$i],$rnum[$i]) = split('=',$read[$i]);
  if($rname[$i] eq $value[1]){
    $rnum[$i] = $rnum[$i] - $num;
  }
}
close(READ);
open(OWRITE,"> nmvl.txt");
if(@read){
  for(my $i=0; $i<@read; $i++){
    print OWRITE $rname[$i],"=","$rnum[$i]\n";
  }
}
close(OWRITE);
##########################

#####sales################
my $money=0;
if($name[2]eq"price"){$money = $num*$value[2];}
if($name[3]eq"price"){$money = $num*$value[3];}
if($money!=0){
  open(OWRITE,">> sales.txt");
  my @read = <OWRITE>;
  chomp (@read);
  print OWRITE "$money\n";
  close(OWRITE);
}
##########################

#############################################
}

if($value[0] eq 'deleteall'){
#############################################
open(WRITE,"> nmvl.txt");
print WRITE ;
close(WRITE);
open(WRITE,"> sales.txt");
print WRITE "0";
close(WRITE);
#############################################
}

if($value[0] eq 'checksales'){
#############################################
open(OWRITE,"< sales.txt");
my @read = <OWRITE>;
chomp (@read);
my $ans=0;
for($i=0;$i<@read;$i++){
  $ans = $ans + $read[$i];
}
close(OWRITE);
print "sales: ",$ans;
#############################################
}

}
