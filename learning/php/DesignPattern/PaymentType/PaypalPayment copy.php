<?php

class ZarinPalPayment implements PaymentOption
{
    public function getPaymentURL(array $paymentInfo): string{
        echo 'Connecting to zarinPal...' . PHP_EOL;
        var_dump($paymentInfo); // like print_r with extera information
    
        return 'https://zarinPal.com/x';
    }
}