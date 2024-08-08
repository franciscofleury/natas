<?php
	$data = "name ";
	$request_data = "aaa"."\n"."admin true";
	$data .= $request_data."\n";
	file_put_contents("./out", $data);
?>
