<?php

interface CDNProviderInterface
{
    public function createServer($region);

    public function listServers($region);

    public function getCDNAddress();
}
