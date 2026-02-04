### Create a Proforma Invoice 

Creating a Proforma Invoice can be done by simply supplying the `amount`, the `client` who you want to create it for, 
and whether you want to send it immediately or not using the `raise_behaviour` variable. 

`send_pfi` is being replaced with `raise_behaviour`. The options are:
- `dont-raise` (default): Creates the PFI as a draft
- `raise`: Raises the PFI to 'Unpaid' status with autopayment (uses client credit if available, schedules autocharge) but no notifications sent
- `raise-no-autopayment`: Raises the PFI to 'Unpaid' status without using client credit or scheduling autocharge
- `raise-and-send`: Raises the PFI to 'Unpaid' status and sends notifications to clients to request payment
- `raise-and-send-no-autopayment`: Raises and sends notifications without autopayment logic

**Note that, if a Proforma Invoice exists that is either Draft or Confirmed, TutorCruncher will simply add a 
new item to it and it will NOT be raised, even if `raise` or `raise-and-send` are passed.**