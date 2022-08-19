[Agents](#agents), [Clients](#clients), [Contractors](#contractors), [Recipients](#recipients) all use the user's email 
address as a unique identifier when creating/updating using the API. If you use the email address when 
creating/updating, we will check for an email address in the user data and check if this user already exists.

You can create a user without an email address, however, you will not be able to update the user. You must also 
include the users last name when creating/updating as this field is required. Any other role specific required
fields are specified on the endpoint description.

