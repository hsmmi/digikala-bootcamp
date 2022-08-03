<?php
use Symfony\Component\Routeing\RouteCollection;
use Symfony\Component\Routing\Route;

$routes = new RouteCollection();

$routes->add('hello', new Route('/hello/{name}'));
$routes->add('bye', new Route('/bye'));