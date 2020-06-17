### Creating an Appointment

Creating an Appointment can be completed by simply supplying the `topic`, `start`, `finish`, `status` and `service`. 
Currently the `status` can only be set to `"planned"`. This will then create a basic Appointment on the service with
no Users applied to it. To do this, post a list of user IDs in the cjas and rcras fields. Other fields 
can be posted to override the branches default settings.
