<?php

include 'connection.php';

if(isset($_POST['submit_button']))
{
	$name = $_POST['name'];
	$email = $_POST['email'];
	$pass = $_POST['password'];
	

	if( (!$name) or (!$email) or (!$pass) )
	{
		header("Location:signup.php?Field is empty!");
		exit();
	}

	$_SESSION['name'] = $_POST['name'];

	$sql = "SELECT * FROM `user` where email='$email' and password='$pass'";
	$rs = mysqli_query($conn, $sql);
	$rows=mysqli_num_rows($rs);


	if($rows==0)
	{
		$sql = "INSERT INTO user(name, email, password) VALUES ('$name', '$email', '$pass')";
		mysqli_query($conn, $sql);

		header("Location: home.php?Successfullysignedup");
		exit();
	}
	else
	{
		header("Location: signin.php ? You have already registered. please Sign in...");
		exit();
	}
}

?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">


<link rel="stylesheet" type="text/css" href="css/main.css">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&family=Raleway:wght@100;400& family=Marck+Script&family=Sofia&family=Tangerine:wght@700&display=swap" rel="stylesheet">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<script src="js/tab.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.js"></script>

<script async src="https://www.googletagmanager.com/gtag/js?id=G-PS831XYXNB"></script>
<script>
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());

	gtag('config', 'G-PS831XYXNB');
</script>

<title class="text-responsive">DSi Assignment : Problem 2</title>

<style>
	span{
		color: indigo;
	}
</style>
</head>


<body data-spy="scroll" data-target=".navbar" data-offset="50">

	<!-- Navigation Bar -->
	<nav class="navbar navbar-expand-md navbar-light bg-white justify-content-end fixed-top nav_menu">

		<div class="container-fluid">

			<a class="navbar-brand" href="index.html" style="font-family: 'Dancing Script', cursive;"><img src="img/logo.png" alt="" width="30" height="24" class="d-inline-block align-text-top">    Problem 2</a>

			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>


			<div class="collapse navbar-collapse flex-grow-0" id="navbarSupportedContent">
				<ul class="navbar-nav text-right">
					<li class="nav-item"> <a class="nav-link" href="index.php">Home</a> </li>
					<li class="nav-item"> <a class="nav-link" href="about.html">About Us</a> </li>
					<li class="nav-item"> <a class="nav-link" href="signin.php">Sign In</a> </li>
					<li class="nav-item"> <a class="nav-link" href="signup.php">Sign Up</a> </li>
					<li class="nav-item"> <a class="nav-link" href="cart.php">Cart</a> </li>
					<li class="nav-item"> <a class="nav-link" href="mailto:faisal2408rcc@gmail.com">Contact</a> </li>
				</ul>
			</div>
		</div>
	</nav>


	<!-- Sign Up Form -->
	<section id="aboutme" class="fullpage d-flex align-items-center justify-content-center" style="height: 80%;">
		<div class="container" align="center">
			<h1 class="title">Sign Up Form</h1>
		</div>
	</section>
