### Add/Edit Contractor on Appointment

This endpoint is for existing `Planned` Appointments. To add a new Contractor or edit an existing 
Contractor's `charge_rate`, simply supply the Contractor's ID and the `charge_rate`. The `charge_rate` 
is not required and if no value is passed we will use the Service's `dft_pay_rate`.
