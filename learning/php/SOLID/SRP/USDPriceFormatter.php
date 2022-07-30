<?php

class USDPriceFormatter implements PriceFormatter
{   
    public function __construct(private array $items)
    {
    }
    
    public function getFormattedPrices(): array
    {
        $result = [];
        foreach ($this->items as $item) {
            // $result[] is append to the array
            $result[] = sprintf('%01.2f USD', $item->getPrice());
        }

        return $result;
    }
}