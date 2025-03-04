### Add/Edit Contractor on Service

This endpoint is for existing Services. To add a new Contractor or edit an existing 
Contractor's `pay_rate`, simply supply the Contractor's ID and the `pay_rate`. The `pay_rate` 
is not required and if no value is passed we will use the Service's `dft_pay_rate` or keep their existing `pay_rate`. 
This will not update any pay rates on existing appointments and will not be able to add contractors to existing 
appointments. To add a contractor to an existing appointment, use the `Add/Edit Contractor on Appointment` endpoint.
