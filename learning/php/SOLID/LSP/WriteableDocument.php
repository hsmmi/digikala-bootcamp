<?php

interface WriteableDocument
{
    /*
        All the file can read
        Writeable document is a any document
        which can write
    */
    public function save();
}