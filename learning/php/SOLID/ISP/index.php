<?php

require __DIR__ . '/autoload.php';

$provider1 = new Amazon();
$provider1->getCDNAddress();

$provider2 = new Dropbox();
$provider2->getCDNAddress();
