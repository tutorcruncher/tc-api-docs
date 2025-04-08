[Agents](#agents), [Clients](#clients), [Contractors](#contractors), [Recipients](#recipients) all use the user's email 
address as a unique identifier when creating/updating using the API. If you use the email address when 
creating/updating, we will check for an email address in the user data and check if this user already exists.

You can create a user without an email address, however, you will not be able to update the user. You must also 
include the users last name when creating/updating as this field is required. Any other role specific required
fields are specified on the endpoint description.

Profile photos can optionally be added for all user roles  — [Agents](#agents), [Clients](#clients), [Contractors](#contractors), and [Recipients](#recipients) during creation — by providing a `photo` field with a valid image URL when creating or updating a user. If the URL points to a valid and accessible image, it will be downloaded and processed into thumbnails, and the response will include the processed photo URL. If the image is invalid, corrupted, or the URL is inaccessible, the request will fail with a `400 Bad Request` and an appropriate error message.

You can also update the photo for all user roles by providing a new image URL in the `photo` field when making an update request to the relevant role’s endpoint (e.g., updating via the [Client](#clients), [Contractor](#contractors), [Agent](#agents), or [Recipient](#recipients) update endpoint). If the image is valid and accessible, it will be processed and replace any existing photo. If the `photo` field is omitted, the current photo remains unchanged. To remove an existing photo, set the `photo` field to `null`. Invalid or inaccessible image URLs will result in a `400 Bad Request` response with a relevant error message.
