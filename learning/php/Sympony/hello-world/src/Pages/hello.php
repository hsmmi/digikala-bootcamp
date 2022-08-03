<?php
$name = $request->query->get('name', 'World'); // default world

// check response based on request
// $response->prepare($request)->send();
$response = new Response('Hello '.$name.'!', 200);

return $response;