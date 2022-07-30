<?php

require __DIR__ . '/autoload.php';

/*
    Array in php is hash map
*/

$items = [
    // Size isn't fix
    new Item(33.2),
    new Item(55.2),
    new Item(133.2),
    new Item(3.2),
    new Item(65.56),
];

$priceCalculator = new PriceCalculator($items);
echo sprintf('Order sum %01.2f' . PHP_EOL, $priceCalculator->calculateItemsPrices());


$priceFormatter = new USDPriceFormatter($items);
foreach ($priceFormatter->getFormattedPrices() as $i => $formattedPrice) { 
    /*
        => arrow when we want key, value
        Array in php is hash map or dictionary
        and when we want to print it we have
        access to just value and when we need key, value
        we use => 
    */
    echo sprintf('Item #%d - %s' . PHP_EOL, $i + 1, $formattedPrice);
}

?>