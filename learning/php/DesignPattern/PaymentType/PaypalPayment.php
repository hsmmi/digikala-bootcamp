<?php

class PaypalPayment implements PaymentOption
{
    public function getPaymentURL(array $paymentInfo): string{
        echo 'Connecting to PayPal...' . PHP_EOL;
        var_dump($paymentInfo); // like print_r with extera information
    
        return 'https://paypal.com/x';
    }
}