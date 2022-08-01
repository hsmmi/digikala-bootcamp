<?php

interface PaymentOption
{
    public function getPaymentURL(array $paymentInfo): string;
    
    // After peyment we get a URL
}