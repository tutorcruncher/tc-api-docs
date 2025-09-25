### Creating a Balance Update

Creating a Balance Update can be completed by simply supplying the `client`, `credit_amount` and `method` as the 
`description` field is optional. The `credit_amount` field must always be a positive value, however if the method is 
set to `"correction"` then `credit_amount` can be a negative value. 

The possible values for the `method` field are:
`cash`, `cheque`, `credit_card`, `transferwise`, `debit_card`, `bank_transfer`, `direct_debit`, `bonus_credit`, 
`manual`, `voucher`, `correction`.
