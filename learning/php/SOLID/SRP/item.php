<?php

class Item
{
    public function __construct(private float $price)
    {
        /*
            No need to do anything
            $this->price = $price;
            No need to define property 
            It will create automatically
        */
    }

    public function getPrice(): float // type hinting
    {
        /*
            $price = 'price'
            return $this->$price; // $this->price
        */
        return $this->price; // this and -> are required
    }
}