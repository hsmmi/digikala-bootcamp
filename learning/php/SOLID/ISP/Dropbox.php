<?php

class Dropbox implements CloudProviderInterface
{
    public function storeFile($name)
    {
        echo 'store a file on Dropbox' . PHP_EOL;
    }

    public function getFile($name)
    {
        echo 'get a file from Dropbox' . PHP_EOL;
    }

    public function createServer($region)
    {
        // Not supported by Dropbox
    }

    public function listServers($region)
    {
        // Not supported by Dropbox
    }

    public function getCDNAddress()
    {
        // Not supported by Dropbox
    }
}
