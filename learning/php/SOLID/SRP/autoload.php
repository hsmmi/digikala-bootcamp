<?php

spl_autoload_register(function ($class_name) {
    // spl: Standard PHP Library
    /*
        Register the autoloader for the classes
        created by cpp
        When we call the class for the first time
        it will automatically be loaded
        $class_name is the name of the class
        . is concatenation in php
        require raise error but include raise warning
    */
    require __DIR__ . '/' . $class_name . '.php';

    /*
        If we want to know that the class was loaded
        we can use the following code
        echo $class_name . ' loaded<br>';
        to log the class name
    */
});