### Create a Contractor Skill

Associates a Skill with a Contractor by specifying the Contractor ID, Subject ID (see [Subjects](#subjects)), and Qualification Level ID (see [Qualification Levels](#qual-level)). 

If a Skill with the specified Subject and Qualification Level does not exist, a new Skill will be created.

If you add a Skill that has already been associated with a Contractor, a new Contractor Skill will not be created and you will get a normal 200 response.

The response will include the full Contractor Skill relationship object including the Contractor details, Subject information, and Qualification Level. 
