<?php

include('config.php');

include('flag.php');

highlight_file('index.php');

$blacklist = '/_|\.|\(\)|=|\||_|<|>|sqlauth|_|\.|\(\)|and|if|database|where|concat|insert|having|limit|mid|substr|by|mid|not|ascii|char|greatest|benchmark|%00|sleep/i';

if(preg_match($blacklist, $_GET['pass'])) exit("No Hack ~_~");

$a = $_GET['pass'];

$rp = array("union", "like", "select", "hostname", "admin", "char");

for ($i=0; $i<6; $i++)
{
    $a = str_ireplace($rp[$i], '', $a);
}

$sql = "select name from users where name='guest' and id='$a'";


$result = mysqli_fetch_array(mysqli_query($conn, $sql));

echo ("<br>".mysqli_error($conn));

echo $sql."<br>";

echo $result['name']."<br>";

if($result['name']==='admin')
{
    echo $flag;
} 
else 
{
    echo "Try hard";
}
 

?>
