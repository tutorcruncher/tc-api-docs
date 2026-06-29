### Updating an Appointment

Updating an Appointment is similar to [Creating an Appointment](#create-an-appointment). One major difference is
that you cannot add, edit or delete Recipients or Contractors on the Appointment — any `rcras` or `cjas`
in the request body are **ignored**. To manage them, use [Add/Edit Recipient on Appointment](#create-update-rcra),
[Remove Recipient from Appointment](#remove-rcra), [Add/Edit Contractor on Appointment](#create-update-cja)
or [Remove Contractor from Appointment](#remove-cja). Note that only Appointments with status `Planned` can be updated.
