<?php

class ReadOnlyDocument extends Document
{
    public function save()
    {
        throw new Exception('Unable to save read-only file');
    }
}
