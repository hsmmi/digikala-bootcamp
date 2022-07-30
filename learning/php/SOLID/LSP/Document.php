<?php

class Document
{
    protected $data;
    protected $filename;

    public function open()
    {
        echo 'open document' . PHP_EOL;
    }

    public function save()
    {
        echo 'save document' . PHP_EOL;
    }
}
