<?php 
error_reporting(0); 
include "./config.php"; 
include "./flag.php"; 

$black_list = "/admin|guest|limit|by|substr|mid|or|not|ascii|char|union|select|greatest|%00|\"|benchmark|"; 
$black_list .= "=|_|in|<|>|sqlauth|_|\.|\(\)|and|if|database|where|concat|insert|having|sleep/i"; 

if(preg_match($black_list, $_GET['pass'])) exit(":P"); 

$query = "select user from sqlauth where user='guest' and pw='{$_GET[pass]}'"; 
echo "<h2>query : {$query}</h2>"; 
$result = @mysqli_fetch_array(mysqli_query($con,$query)); 
$admin_info =  @mysqli_fetch_array(mysqli_query($con,'select * from sqlauth where user="admin"')); 

if($result['user']) echo "<h2>Welcome {$result[user]}</h2>"; 

if(($admin_info['pw'])&& $admin_info['user']===$_GET['user'] && $admin_info['pw']===$_GET['pass']){ 
        echo $flag; 
        } 

highlight_file(__FILE__); 
?> 