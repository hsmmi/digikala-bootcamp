<?php
require_once dirname(__DIR__).'/vendor/autoload.php';
require_once dirname(__DIR__).'/src/app.php';

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Exception\ResourceNotFoundException;

$request = Request::createFromGlobals();
$response = new Response();

dump($request->getPathInfo()); // get url pat

// $map = [
//     '/hello' => dirname(__DIR__).'/src/pages/hello.php',
//     '/bye' => dirname(__DIR__).'/src/pages/bye.php',
// ];

use Symfony\Component\Routing\Matcher\UrlMatcher;
use Symfony\Component\Routing\RequestContext;

$requestContext = new RequestContext();
$requestContext->fromRequest($request);
$matcher = new UrlMatcher($routes, $request);

function render_template($request)
{
    // Global the variables with extract
    extract($request->attributes->all());

    return include sprintf(dirname(__DIR__).'/src/pages/'.'/src/pages/'.$request->attributes->get('_route').'.php', $name);
}

// Can do try catch globally

try {
    // dump($matcher->match($request->getPathInfo())); 
    // $attributes = dump($matcher->match($request->getPathInfo())); 

    // Request object has the ability to add parameters to them
    $request->attributes->add($matcher->match($request->getPathInfo()));

    $respone = render_template($request);
} catch (ResourceNotFoundException $e) {
    $response->setContent('Page not found', 404);
} catch (Exception $e) {
    $response->setContent('Internal error', 500);
}

// if(isset($map[$request->getPathInfo()])) {
//     $response = require $map[$request->getPathInfo()];
// } else {
//     $response = new Response('Not Found', 404);
// } 

$response->prepare($request)->send();