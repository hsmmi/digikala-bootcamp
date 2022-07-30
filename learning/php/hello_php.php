<?php

// To get object with fire method
interface GunInterface { // Abstraction
    public function fire(): string; // return string
    // public function fire($roo); // remember the input is important
}

class Soldier {
    public $gun;

    // public function __construct() {
    //     // soldier choose the gun and just can use one
    //     // specific gun and it's not single responsibility anymore
    //     // because when we want to change the gun, we need to
    //     // change the soldier class
    //     $this->gun = new Gun();
    // }

    // Dependency injection
    // public function __construct(Gun $gun) { // Wrong because of type input
    public function __construct(GunInterface $gun) { // Just check the input has required method(fire)
        // When we create a new Soldier, we pass in a Gun object.
        $this->gun = $gun;
    }

    public function kill() {
        $this->gun->fire(); // We can use the Gun object's fire() method.
    }
}

class Soldier2 {
    public $gun;
    public function __construct(GunInterface $gun) { // Just check the input has required method(fire)
        $this->gun = $gun;
    }

    public function kill() {
        echo $this->gun->fire(); // We can use the Gun object's fire() method.
    }
}

class Gun {
    public $catridge = 3; // object variable and we create copy
    // public static $catridge = 3; // class variable

    public function fire()
    {
        if ($this->catridge > 0) {
            $this->catridge--;
            echo "BANG!";
        } else {
            echo "Click!";
        }
    }
}

class ModernGun implements GunInterface {
    public $catridge = 3; // object variable and we create copy
    // public static $catridge = 3; // class variable

    public function fire()
    {
        if ($this->catridge > 0) {
            $this->catridge--;
            echo "BANG!";
        } else {
            echo "Click!";
        }
    }
}

$gun = new Gun();

$soldier1 = new Soldier($gun);
$soldier2 = new Soldier($gun);
// Now we have a Soldier object with a Gun object.

$soldier1->kill(); // BANG!
echo PHP_EOL;
$soldier1->kill(); // BANG!
echo PHP_EOL;
$soldier1->kill(); // BANG!
echo PHP_EOL;
$soldier1->kill(); // Click!
echo PHP_EOL;

echo PHP_EOL;

$soldier2->kill(); // Click!
echo PHP_EOL;
$soldier2->kill(); // Click!
echo PHP_EOL;
$soldier2->kill(); // Click!
echo PHP_EOL;
$soldier2->kill(); // Click!
echo PHP_EOL;

// So both soldier use same gun.


$gun2 = new ModernGun();

$soldier3 = new Soldier($gun);
$soldier4 = new Soldier($gun2);


// SOLID
// L: Liskov Substitution Principle