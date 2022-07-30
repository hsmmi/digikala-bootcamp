<?php

interface CloudProviderInterface
{
    public function storeFile($name);

    public function getFile($name);
}
