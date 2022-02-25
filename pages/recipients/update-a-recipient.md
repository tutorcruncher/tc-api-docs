### Update a Recipient

Update a Recipient object by supplying the email address as the unique identifier. You must also supply the required
fields like `last_name` even if they are not being updated. You only need to post information that you want to change
and not the whole Recipient object.

If the Recipient doesn't have an email address, if you supply a `first_name`, `last_name` and `paying_client`,
we will update a Recipient if the names match an existing Recipient linked to the Client ID you supply
for `paying_client`.

Check out [Creating/Updating Users](#creating-updating-users) for more information on linking to a specific user.
