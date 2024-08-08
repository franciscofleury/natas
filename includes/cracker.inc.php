<?php
    declare(strict_types=1);

    abstract class Cracker {
        protected $headers;
        protected $pw_n = 32;
        protected $possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        private $pw = "";
        public $max_fails = 3;

        public function crack(): string {
            $fails = 0;
            $i = 0;
            while ($i < $this->pw_n) {
                $pw_c = $this->crack_character();
                if ($pw_c == "!ERROR") {
                    $fails++;
                    if ($fails >= $this->max_fails) {
                        return "!ERROR";
                    }
                } else {
                    $this->pw .= $pw_c;
                    $i++;
                }
            }
            return $this->pw;
        }

        private function crack_character(): string {
            for ($i=0;$i < $this->count($possibilities);$i++) {
                $try = $this->pw . $this->possibilities[$i];
                $result = $this->makeRequest($try);
                if ($result) {
                    return $try;
                }
            }
            return "!ERROR";
        }
        abstract protected function makeRequest($try): boolean;
    }