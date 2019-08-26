<?php

include('flag.php');


$ref = $_SERVER['HTTP_REFERER'];

$url = 'https://google.com';

if(!preg_match("/[a-zA-Z\:\/]*google.com/", $ref))
{
	die("Access only for users coming from <a href='$url'>google</a>");
}

echo "Hi, I think I seem to know you :)<br><br>";
echo "Remember that google is your best friend :P<br><br>";
echo "Here's a flag for you:<br><br>";
echo "<b>$flag</b>";

?>
