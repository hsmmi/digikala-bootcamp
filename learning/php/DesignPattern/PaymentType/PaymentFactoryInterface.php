<?php

interface PaymentFactoryInterface
{
    public function create(string $type): PaymentOption;
}