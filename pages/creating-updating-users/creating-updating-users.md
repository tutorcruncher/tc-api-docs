[Agents](#agents), [Clients](#clients), [Contractors](#contractors), [Recipients](#recipients) all use the user's email 
address as a unique identifier when creating/updating using the API. If you use the email address when 
creating/updating, we will check for an email address in the user data and check if this user already exists.

You can create a user without an email address, however, you will not be able to update the user. You must also 
include the users last name when creating/updating as this field is required. Any other role specific required
fields are specified on the endpoint description.

Please note when creating/updating a user with custom fields, you must format the payload as follows:
`'extra_attrs': {'custom_field_machine_name_1': 'value_1', 'custom_field_machine_name_2': 'value_2'},`
You can find the machine name of a custom field by clicking on it in your 
[custom field settings](https://secure.tutorcruncher.com/setup/attrs/). See [creating a client](#3-create-a-client)
 for an example which sets a custom field for the Client's date of birth.

