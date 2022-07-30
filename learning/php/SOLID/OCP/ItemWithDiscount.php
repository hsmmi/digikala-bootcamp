<?php

class ItemWithDiscount
{   
    /*
        private float $price;
        private float $discount;

        public function __construct(float $price, float $discount = 0.0)
        {
            $this->price = $price;
            $this->discount = $discount;
        }
    */

    public function __construct(
        private float $price, // promoted constructor
        private float $discount = 0.0
    )
    // Don't use float for price
    {
    }

    public function getPrice(): float
    {
        return $this->price * (1 - $this->discount);
        // was: return $this->price;
        
    }

    public function getDiscount(): float
    {
        return $this->discount;
    }
}
