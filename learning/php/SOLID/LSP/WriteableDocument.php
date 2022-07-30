<?php

class WriteableDocument extends Document
{
    /*
        All the file can read
        Writeable document is a any document
        which can write
    */
    public function save()
    {
        echo 'open document and save it' . PHP_EOL;
    }
};