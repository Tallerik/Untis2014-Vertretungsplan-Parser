<?php



echo substr(substr(json_encode(exec("python3.5 parser.py")), 1), 0, -1);

