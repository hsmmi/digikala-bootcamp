<?php

interface DataProcessorInterface
{
    // Decorator which get a object with same interface
    public function __construct(?DataProcessorInterface $processor);
    // ? is like if else, if $processor is null,
    // then return null, else return $processor

    public function process(string $data): string;
}