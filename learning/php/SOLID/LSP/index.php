<?php

require __DIR__ . '/autoload.php';

$documents = [
    new Document(),
    new ReadOnlyDocument(),
    new Document(),
];

$project = new Project();
foreach ($documents as $document) {
    $project->addDocument($document);
}

$project->openAll();
