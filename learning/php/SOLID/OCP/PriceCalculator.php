<?php

class PriceCalculator
{
    public function __construct(private array $items)
    {
    }

    public function calculateItemsPrices(): float
    {
        $result = 0;
        foreach ($this->items as $item) {
            if ($item instanceof ItemWithDiscount) {
                $result += $item->getPrice() * (1 - $item->getDiscount());
            } elseif ($item instanceof Item) {
                $result += $item->getPrice();
            }
        }

        return $result;
    }
}

