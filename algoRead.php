<html>


<head>

<style>
body {
  background-color: #ff0000;
}

#count {
    height: 100px;
    width: 200px;
    position: fixed;
    top: 50%;
    left: 50%;
    margin-top: -50px;
    margin-left: -100px;
}

p {
 text-align: center;
line-height: 100px;
font-size: 60px;
font-family: Arial;
color: white;
}

</style>


</head>
<body>
<div id="count">

<p id="time-display"><?php
$myfile = fopen("data.txt", "r") or die("err");
echo fread($myfile,filesize("data.txt"));
echo " mins";
fclose($myfile);
?></p>



</div>


</body>

</html>
