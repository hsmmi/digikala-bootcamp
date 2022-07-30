<?php

require __DIR__ . '/autoload.php';

$items = [
    new Item(33.2),
    new ItemWithDiscount(55.2, 0.3),
    new ItemWithDiscount(133.2, 0.4),
    new Item(3.2),
    new Item(65.56),
];

$priceCalculator = new PriceCalculator($items);
echo sprintf('Order sum %01.2f' . PHP_EOL, $priceCalculator->calculateItemsPrices());
