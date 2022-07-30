<?php

interface WriteableDocumentRepository
{
    public function add(WriteableDocument $document);
}