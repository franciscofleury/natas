<?php
	$data = file_get_contents("./out");
	echo $data;
	foreach (explode("\n", $data) as $line) {
		echo "read ".$line;
	}
?>
