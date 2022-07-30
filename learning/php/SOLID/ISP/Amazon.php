<?php

class Amazon implements CloudProviderInterface
{
    public function storeFile($name)
    {
        echo 'store a file on Amazon' . PHP_EOL;
    }

    public function getFile($name)
    {
        echo 'get a file from Amazon' . PHP_EOL;
    }

    public function createServer($region)
    {
        echo 'create server on Amazon' . PHP_EOL;
    }

    public function listServers($region)
    {
        echo 'list servers from Amazon' . PHP_EOL;
    }

    public function getCDNAddress()
    {
        echo 'get CDN address on Amazon' . PHP_EOL;
    }
}
