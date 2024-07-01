<?php

echo "hello world!";
echo "<br>";
echo $_SERVER['REQUEST_URI'];
echo "<br>";
echo $_SERVER['QUERY_STRING'];
$qstr = $_SERVER['QUERY_STRING'];
echo "<br>";
echo "srv-qstring: $qstr";

$url = "https://7kal7z2fppfawmne5qtgjus2du0zknld.lambda-url.eu-west-2.on.aws/?tiny=";
echo "<br>";
$newurl = $url;

echo "<br>";
echo "url = $newurl$qstr";
echo "<br>";
$newurl = "$newurl$qstr";
echo $newurl;

redirect($newurl);

function redirect($url) {
        $url = str_replace("http://","",$url);
        $url = str_replace("https://","",$url);
        header('Location: http://' . $url);
        die();
}

?>
