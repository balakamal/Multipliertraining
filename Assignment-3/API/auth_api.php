<?php

if($_SERVER['REQUEST_METHOD'] = 'POST') { 
	$username = $_POST["username"];
	$password = $_POST['password'];

	$con = mysqli_connect("localhost","$username","$password","test");

	$response = array();

	if($con) {

		$sql = "select * from data";

		$result = mysqli_query($con,$sql);

		if($result) {

			header("Content-Type: JSON");

			$i=0;

			while($row = mysqli_fetch_assoc($result)){

				$response[$i]['id'] = $row ['id'];
				$response[$i]['name'] = $row ['name'];
				$responsive[$i]['age'] = $row ['age'];
				$response[$i]['email'] = $row ['email'];

				$i++;

			}

			echo json_encode($response, JSON_PRETTY_PRINT);

		}

	}
}
else{

echo "Invalid user";
}
?>