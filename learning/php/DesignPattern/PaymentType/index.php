<?php

$config =  require __DIR__ . '/payment_config.php';
var_dump($config); // programmers use this for more info

// autoload
spl_autoload_register(function ($class_name) {
    require __DIR__ . '/' . $class_name . '.php';
}); // get function

$factory = new DefaultPaymentFactory();
$option = $factory->create('zarinpal');
$option->getPaymentURL([
    'order_id' => 123,
]);