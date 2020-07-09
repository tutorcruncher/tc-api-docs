### Add/Edit Recipient on Appointment

This endpoint is for existing `Planned` Appointments. To add a new recipient or edit an existing 
recipients `charge_rate`, simply supply the recipients ID and the `charge_rate`. The `charge_rate` 
is not required and if no value is passed we will use the Service's `dft_charge_rate`.
