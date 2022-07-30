<?php

class BudgetReport
{
    private $db;

    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }

    public function open()
    {
        echo "open report";
    }

    public function save()
    {
        echo "save report";
    }
}
