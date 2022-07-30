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
            $result += $item->getPrice();
        }

        return $result;
    }


    /*
        Due to SPR we should move this method
        to the new Class

        We may have diffrent approaches to this problem
        so we should use interface to solve this problem
        and interface is a signiture of the method

        public function getFormattedPrices(): array
        {
            $result = [];
            foreach ($this->items as $item) {
                // $result[] is append to the array
                $result[] = sprintf('%01.2f USD', $item->getPrice());
            }

            return $result;
        }
    */
}
