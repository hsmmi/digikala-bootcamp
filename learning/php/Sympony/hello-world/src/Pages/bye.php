<?php
$response = $response->setContent('bye');

// check response based on request
$response->prepare($request)->send();
