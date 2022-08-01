<?php

class DB
{
    public static $instanceCount = 0;
    private static $instance;

    /*
        we don't have pubclic constructor because we
        want to make it a singleton class.
        So we can't use new on it.
    */
    private function __construct()
    {
        self::$instanceCount++;
    }

    public static function getInstance()
    {
        /*
            In static we can use self::$instance or
            static::$instance. but when we use static
            we bind it to the static instance of the class
            in the runtime.
            self is the same as static but bind it to the class.

            We use :: instead of -> because we don't have object
            and we are in the class scope.
        */
        if (is_null(static::$instance)) { 
            static::$instance = new static();
            // Create a new object of the class.
            // here static = self = DB.
        }
        return self::$instance;
    }
}

$db = DB::getInstance();
$db = DB::getInstance();
$db = DB::getInstance();
echo DB::$instanceCount; // 1