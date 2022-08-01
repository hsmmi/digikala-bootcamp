<?php
// File name diffrent because we don't have code here

return [
    'paypal' => PaypalPayment::class, // scope resolution operator
    // which return string of class name
    'zarinpal' => ZarinPalPayment::class, // have comma in last item 
    // to prevent future error
];