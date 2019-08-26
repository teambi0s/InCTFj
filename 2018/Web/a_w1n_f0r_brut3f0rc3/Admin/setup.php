<?php
$servername = "localhost";
$username = "root";
$password = "JyothirmayeE@77";

// Creating a connection
$conn = new mysqli($servername, $username, $password);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
// Creating a database named HCALL
$sql = "CREATE DATABASE SQL_AUTH";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully with the name SQL_AUTH"."<br>";
} else {
    echo "Error creating database: " . $conn->error;
}
//Select db
$sql = "use SQL_AUTH";

if ($conn->query($sql) === TRUE) {
    echo "Successfully selected SQL_AUTH"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}



//Inserting data
$sql = "CREATE TABLE sqlauth (user varchar(10),pw varchar(30))";
if ($conn->query($sql) === TRUE) {
    echo "Table sqlauth created successfully"."<br>";
} else {
    echo "Error creating table: " . $conn->error;
}
$sql = "INSERT INTO sqlauth VALUES ('guest','73915728')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


$sql = "INSERT INTO sqlauth VALUES ('admin','61741729')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully"."<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// closing connection
$conn->close();
?>
