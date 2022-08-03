<?php
require_once dirname(__DIR__).'/vendor/autoload.php';

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

$request = Request::createFromGlobals();
$response = new Response();

dump($request->getPathInfo()); // get url pat

$map = [
    '/hello' => dirname(__DIR__).'/src/pages/hello.php',
    '/bye' => dirname(__DIR__).'/src/pages/bye.php',
];

if(isset($map[$request->getPathInfo()])) {
    $response = require $map[$request->getPathInfo()];
} else {
    $response = new Response('Not Found', 404);
} 

$response->prepare($request)->send();