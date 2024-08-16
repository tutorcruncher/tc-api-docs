Many objects in TutorCruncher can be customised with custom fields.
These custom fields are stored in array called `extra_attrs`, you can see the shape of a custom field in an 
`extra_attrs` array in the response on the right. 

However, to update a custom field you must not post this whole array. Instead, you should assign 
`extra_attrs` with an object with keys equal to custom field machine names and values equal to the new values. For 
example a valid payload would be:
`'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'},`

You can find the machine name of a custom field by clicking on it in your 
[custom field settings](https://secure.tutorcruncher.com/setup/attrs/). See [creating a client](#3-create-a-client)
 for an example which sets a custom field for the Client's date of birth.

If you are using dropdown custom fields, you must post the slugified value of the dropdown option. 
For example, a value `Doesn't suit student` would be posted as `doesnt-suit-student`.

<details>
<summary>
  What is slugification?
</summary>

When you convert spaces or repeated dashes to single dashes. Remove characters that aren't alphanumerics, underscores, or hyphens. Convert to lowercase. Also strip leading and trailing whitespace, dashes, and underscores.

</details>


