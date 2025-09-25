### Creating a Balance Update

Creating a Balance Update can be completed by simply supplying the `client`, `credit_amount` and `method` as the 
`description` and `send_receipt` fields are optional. The `credit_amount` field must always be a positive value, 
however if the method is set to `"correction"` then `credit_amount` can be a negative value. If `send_receipt` is set 
to `True` then the `Payment receipt` email will be sent to the client if the email definition is enabled.

The possible values for the `method` field are:
`cash`, `cheque`, `credit_card`, `transferwise`, `debit_card`, `bank_transfer`, `direct_debit`, `bonus_credit`, 
`manual`, `voucher`, `correction`.
