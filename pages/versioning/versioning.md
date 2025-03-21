## Zapier is now functional with Version 2 of the Roles API. To use them both together you will need to use the TutorCruncher (3.0.0) in zapier

### Zapier changes
Mostly things should be just about the same, some IDs may look different inside Zapier but the data should be the same.
This should appear as IDs being required to Update a user and the User layer in requests and responses being removed.

For moving from V1 to V2 of API, the best practice is to follow the following steps.

1. Clone an existing zap
2. Update to use the TutorCruncher(3.0.0) app
3. Switch API key to a Demo branch API key for testing
4. Check the create and update zaps are correct, check for data where it can no longer be retrieved from previous zaps
5. Test each step of the zap to ensure it is working correctly with the demo branch before moving back to live


### Version 2 API changes

Version 2 of the Roles API is on its way. The changes are mostly in the backend and to improve speed and set us up for better developments going forward.
We will be removing Version 1 of the Roles API on the 3rd July 2025 so please update your API integrations as needed before then.
While the changes will be very small for you, we recommend that you adapt your system to handle both Version 1 and Version 2 
simultaneously to allow you to have a smooth transition.

The core change that affects your endpoints is that we have removed the usage of the 'user' dictionary for roles. You will 
see in each of the Roles that there is now two versions and each displays the difference in usage. Note that when sending 
data in a request to TutorCruncher you will still be able to use the 'user' dictionary in Version 2 as it was used in Version 1
but the data we return will be dependent on the version set on your Branch. See difference ->

### Other changes include:
* Version 2 allows you to update the role by ID now instead of email or name by posting to the endpoint for that specific role. e.g. to update the Client with ID 1234 I can use post to `secure.tutorcruncher.com/api/clients/1234/` with a dictionary of data to update that client and its related user data.
* Version 2 will not match on a users first and last name.
* In Version 1 you could update a role by posting to the list page e.g. `secure.tutorcruncher.com/api/clients/` and update a role based on the email passed. In Version 2 this will return an error as it is expecting to create a user with that email. 
* In both Versions, if I have a client with the email `example@example.com` and I post to the list page for contractors with the same email then it will create a new contractor role that is linked to the existing client.
* We no longer send emails about failed requests, the errors are returned when the request fails and should be handled then.

### Recommendations for using Version 2:
* Retrieve: Use a GET request to the detail page for an individual role (e.g. `secure.tutorcruncher.com/api/clients/<role_id>/`)
* Create: Use a POST request to the list page for each role (e.g. `secure.tutorcruncher.com/api/clients/`)
* Update: Use a POST request to the detail page for an individual role (e.g. `secure.tutorcruncher.com/api/clients/<role_id>/`)
* Delete: Use a DELETE request to the detail page for an individual role (e.g. `secure.tutorcruncher.com/api/clients/<role_id>/`)

Note that the rest of the docs have been updated to reflect Version 2 usage. While you can still use Version 1 until the 3rd July 2025
we recommend that your refrain from doing so and update your integrations to use Version 2 as soon as possible.