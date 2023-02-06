Many objects in TutorCruncher can be filtered.
These filters can be used in two ways:

1. Using the 'Filter' button on the list page of the [Browsable API](https://secure.tutorcruncher.com/api)

2. Filtering against Query Parameters in the URL

#####One Parameter
To Filter against Query Parameters in the URL, you must add the following format:
`?filter=value` to the end of the URL.

for example:

`https://secure.tutorcruncher.com/api/clients/?user__first_name=Anthony`

This will return all clients where the user's first name is 'Anthony'

#####Multiple Parameters
You can also apply multiple filters to the URL by adding an ampersand (&) between each filter.

for example:

`https://secure.tutorcruncher.com/api/clients/?user__first_name=Anthony&user__last_name=Clay`

This will return all clients where the user's first name is 'Anthony' and last name is 'Clay'

You can use as few or little filters as you like as long as they are available on that endpoint.

