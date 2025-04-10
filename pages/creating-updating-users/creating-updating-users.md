[Agents](#agents), [Clients](#clients), [Contractors](#contractors), [Recipients](#recipients) all use the user's email 
address as a unique identifier when creating/updating using the API. If you use the email address when 
creating/updating, we will check for an email address in the user data and check if this user already exists.

You can create a user without an email address, however, you will not be able to update the user. You must also 
include the users last name when creating/updating as this field is required. Any other role specific required
fields are specified on the endpoint description.

Profile photos can be optionally added or updated for all user roles — [Agents](#agents), [Clients](#clients), [Contractors](#contractors), and [Recipients](#recipients) — by including a `photo` field with a valid image URL when creating or updating a user. If the image is valid and accessible, it will be downloaded, processed into thumbnails, and included in the response. If the `photo` field is omitted during an update, the current photo remains unchanged. To remove an existing photo, set the `photo` field to `null`. Invalid, corrupted, or inaccessible image URLs will result in a `400 Bad Request` with an appropriate error message.
