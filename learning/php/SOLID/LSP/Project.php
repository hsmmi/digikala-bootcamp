<?php

class Project
{
    protected array $documents;

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
            /*
                Change because prefering vertical code
                to horizontal code.


                if (!($document instanceof ReadOnlyDocument)) {
                    $document->save();
                }
            */


            /*
                For Liskov Substitution Principle
                we should be able to use document and 
                read-only document interchangebly.
                
                But we can't use document and read-only
                document interchangebly because we
                can't save read-only document.


                if ($document instanceof ReadOnlyDocument) {
                    continue;
                }
                $document->save();
            */
            if ($document instanceof WriteableDocument) {
                continue;
            }
            $document->save();

        }
    }
}