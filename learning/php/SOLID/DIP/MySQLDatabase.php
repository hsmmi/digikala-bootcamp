<?php

class MySQLDatabase implements DatabaseInterface
{
    public function insert()
    {
        echo "insert row in MySQL";
    }

    public function update()
    {
        echo "update row in MySQL";
    }

    public function delete()
    {
        echo "delete row in MySQL";
    }
}
