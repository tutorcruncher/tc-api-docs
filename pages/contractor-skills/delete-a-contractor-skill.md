### Delete a Contractor Skill

Deletes a Contractor Skill using its unique ID. Only Contractor Skills associated with the API key's Branch can be deleted. Attempts to delete a skill that belongs to a different Branch or references a Subject or Qualification Level hidden or restricted for the Branch will result in a `400 Bad Request` response. For more information about Branch-specific restrictions, see [Subject](#subjects) and [Qualification Level](#qual-levels).
