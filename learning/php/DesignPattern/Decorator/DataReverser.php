<?php

require __DIR__ . '/DataProcessorInterface.php';

class DataReverser implements DataProcessorInterface
{
    private ?DataProcessorInterface $decoratedProcessor;
    // Data type can be null, so use ?

    public function __construct(?DataProcessorInterface $processor = null)
    {
        $this->decoratedProcessor = $processor;
    }

    public function process(string $data): string
    {   
        /*
            In decotrator, first we run decorated object,
            then we run decorator.
        */
        if ($this->decoratedProcessor !== null) {
            $data = $this->decoratedProcessor->process($data);
        }

        return strrev($data);
    }
}

$processor = new DataReverser();
echo $processor->process('Hello World');
