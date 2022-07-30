<?php

class ItemWithDiscount
{
    public function __construct(
        private float $price,
        private float $discount = 0.0
    )
    {
    }

    public function getPrice(): float
    {
        return $this->price;
    }

    public function getDiscount(): float
    {
        return $this->discount;
    }
}
