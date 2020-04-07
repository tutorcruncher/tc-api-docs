### Create a Proforma Invoice

Creating a Proforma Invoice can be done by simply supplying the `amount`, the `client` who you want to create it for, 
and whether you want to send it immediately (`send_pfi`). If you have `send_pfi` set to `True`, the PFI will have the 
status 'Unpaid', and an email will be sent to them with the details about the PFI including the PDF.
