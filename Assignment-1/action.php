<?php 
    $uname = $_POST["uname"]; 
    $pass = $_POST["pass"];
    if($pass == 'password')
    {
        session_start();
        echo("<h2>Session started</h2>");
    }
    else{
        header("Location:index.html");
        exit();
    } 
?>