<?php

class BudgetReport
{
    private $db;

    // public function __construct(MySQLDatabase $db) "Lahim Doshakh"
    public function __construct(DatabaseInterface $db)
    {
        $this->db = $db;
    }

    public function open()
    {
        echo "open report";
    }

    public function save()
    {
        $this->db->insert();
    }
}
