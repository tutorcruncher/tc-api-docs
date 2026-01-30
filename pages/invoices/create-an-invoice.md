### Create an Invoice

Create invoices from Appointments and/or Ad Hoc Charges. This endpoint generates invoices for the specified items
and optionally raises (sends) them immediately.

#### Required Fields

You must provide at least one of:
- `appointments`: Array of Appointment IDs
- `adhoc_charges`: Array of Ad Hoc Charge IDs

#### Optional Fields

- `raise_behaviour`: Controls what happens after invoice creation. Options:
  - `dont-raise` (default): Creates draft invoices only
  - `raise`: Raises invoices with autopayment (uses client credit if available, schedules autocharge)
  - `raise-no-autopayment`: Raises invoices without using client credit or scheduling autocharge
  - `raise-and-send`: Raises invoices and sends notification emails to clients
  - `raise-and-send-no-autopayment`: Raises and sends notifications without autopayment logic

#### Item Eligibility

**Important:** Not all Appointments and Ad Hoc Charges are available for invoice creation. Items are filtered based on the following criteria:

**Appointments must:**
- Be in a chargeable status (`complete`, `cancelled-chargeable`)
- NOT use the EA (Employment Agency) workflow (`use_ea_workflow` must be false)
- NOT already have charges on a live invoice (unpaid, payment-pending, paid, or failed)
- Have at least one Recipient (student) assigned with a paying client

**Ad Hoc Charges must:**
- NOT use the EA workflow (`use_ea_workflow` must be false)
- NOT already have charges on a live invoice
- NOT have a foreign currency set (`currency` must be null)
- Have a client assigned

If an item does not meet these criteria, it will not be found and you will receive a validation error stating
the object does not exist.

#### Validation Rules

- **Maximum 8 items** per request (appointments + ad hoc charges combined)
- All items must be linked to the **same client**
- Appointments with students linked to **multiple different clients** cannot be invoiced via this endpoint

#### Response

The response includes all created invoices. If split payments are enabled and configured, payment orders may also
be returned. If you have the branch setting "Invoice Grouping" set to "Separate Invoices by student", then there may 
be multiple invoices.
