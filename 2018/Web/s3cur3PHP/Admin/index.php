<?php

include('flag.php');

$msg = "Jycuam9pbihjaHIob3JkKGkpXjkwKSAgZm9yIGkgaW4gJyk/ND56PT8ueig/Ky8/KS56LykzND16LDM/LSk1Lyg5P3oqOyg7Nz8uPygnKQ==";

if(!isset($_GET['viewsource']))
{
	die($msg);
}

echo "<h2>s3cur3 PHP</h2>";
echo "Hack your way to the flag (^_^)<br><br>";

highlight_file(__FILE__);

if(!isset($_GET['flag']))
{
	die("Bye bye hacker");
}

if((strcmp($_GET['flag'],$flag)))
{
	die("Gimme flag first, then enter!!!");
}

echo "Thanks for the flag :P<br><br>";

if(!isset($_GET['secret']))
{
	die("Bye bye hacker");
}

$_p = 1729;
$_l = 13;

$l = strlen($_GET['secret']);
$_i = intval($_GET['secret']);

if($l !== $_l || $_i !== $_p)
{
	die("System Failure Detected...");
}

echo "<h3>Yaaay...you have breached the most s3cur3 PHP code</h3>";
echo "<h3>Here is your flag: ⚑ </h3>";

echo "<!--$flag-->";

?>


