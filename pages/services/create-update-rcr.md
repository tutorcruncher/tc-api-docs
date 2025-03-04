### Add/Edit Recipient on Service

To add a new Recipient or edit an existing Recipient's `charge_rate`, simply supply the Recipient's ID and 
the `charge_rate`. The `charge_rate` is not required and if no value is passed we will use the Service's 
`dft_charge_rate` or keep their existing `charge_rate`.
This will not update any charge rates on existing appointments and will not be able to add recipients to existing 
appointments. To add a recipient to an existing appointment, use the `Add/Edit Recipient on Appointment` endpoint.
