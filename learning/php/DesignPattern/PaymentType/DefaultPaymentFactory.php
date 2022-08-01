<?php
// In Iran we don't have PayPal

class DefaultPaymentFactory implements PaymentFactoryInterface
{
    private array $options = [
        'paypal' => PaypalPayment::class, 
        'zarinpal' => ZarinPalPayment::class,
    ];
    /*
        we create this array to dont have specific 
        config for every factory
    */
    public function create(string $type): PaymentOption
    {
        // check if exist
        // if(isset())
        if(!array_key_exists($type, $this->options)){
            throw new Exception('Invalid payment option');
        }
        return new $this->options[$type]();
        // () calls the constructor
    }
}