<?php
    
$input = "66
10
18
11
21
28
31
38
40
55
60
62";

$lines = explode("\n", $input);
$lines = array_map('intval', $lines);

$sum = array_shift($lines);
$len = array_shift($lines);

$found = false;
foreach ($lines as $num) {
    $diff = $sum - $num;
    print_r($diff);
    print_r( $lines);
    if (in_array($diff, $lines)) {
        $found = true;
        print_r("yeap");
        break;
    }
}

// fwrite(STDOUT, intval($found));