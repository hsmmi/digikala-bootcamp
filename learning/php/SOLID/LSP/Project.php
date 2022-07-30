<?php

class Project
{
    protected $documents;

    public function addDocument(Document $document)
    {
        $this->documents[] = $document;
    }

    public function openAll()
    {
        foreach ($this->documents as $document) {
            $document->open();
        }
    }

    public function saveAll()
    {
        foreach ($this->documents as $document) {
            if ($document instanceof ReadOnlyDocument) {
                continue;
            }
            $document->save();
        }
    }
}