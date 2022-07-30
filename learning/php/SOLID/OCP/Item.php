<?php

class Item
{
    public function __construct(private float $price)
    {
    }

    public function getPrice(): float
    {
        return $this->price;
    }
}
