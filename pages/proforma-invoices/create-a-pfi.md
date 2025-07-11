### Create a Proforma Invoice 

Creating a Proforma Invoice can be done by simply supplying the `amount`, the `client` who you want to create it for, 
and whether you want to send it immediately or not using the `raise_behaviour` variable. 

`send_pfi` is being replaced with `raise_behaviour`. The options are `dont-raise`,`raise` or `raise-and-send`. If no value is passed or `dont-raise` is passed then the 
PFI will be created as draft. If `raise` is passed then the PFI will be created and raised to the status 'Unpaid' but no notifcations will be sent to clients. If `raise-and-send` is passed then the PFI will be created and raised to the status 'Unpaid' and notifcations will be sent to clients to request payment.

**Note that, if a Proforma Invoice exists that is either Draft or Confirmed, TutorCruncher will simply add a 
new item to it and it will NOT be raised, even if `raise` or `raise-and-send` are passed.**