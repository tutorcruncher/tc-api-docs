# TutorCruncher API Documentation - Agent Guide

This document describes how the TutorCruncher API documentation is structured and how to write documentation for new endpoints.

## Overview

This repository contains the source files for TutorCruncher's public API documentation, hosted at [api.tutorcruncher.com](https://api.tutorcruncher.com). The documentation is built using [Harrier](https://harrier.dev/) and uses YAML configuration files with Markdown content.

## Project Structure

```
tc-api-docs/
├── harrier.yml           # Main site configuration
├── pages/
│   ├── api.yml           # Master API layout - defines all sections
│   ├── index.md          # Home page (uses api.jinja template)
│   ├── <endpoint>/       # One folder per API endpoint type
│   │   ├── <endpoint>.yml          # Section layout for this endpoint
│   │   ├── <endpoint>-object.yml   # Attributes/schema definition
│   │   ├── <endpoint>-object.md    # Object description
│   │   ├── <endpoint>-object.json  # Example response object
│   │   ├── list-all-<endpoint>.md  # List endpoint description
│   │   ├── list-all-<endpoint>.py  # List endpoint code example
│   │   ├── list-all-<endpoint>.json# List endpoint response example
│   │   ├── get-a-<endpoint>.md     # Get single item description
│   │   ├── get-a-<endpoint>.py     # Get single item code example
│   │   ├── get-a-<endpoint>.json   # Get single item response example
│   │   └── ... (create, update, delete, etc.)
│   └── ...
└── theme/                # Jinja templates for rendering
```

## File Types and Their Purpose

### Section Layout Files (`<endpoint>.yml`)

Each endpoint folder has a main YAML file that defines all documentation sections for that endpoint. Structure:

```yaml
sections:
  -
    title: Object Name Object          # Section title
    id: object-name-object             # Unique HTML anchor ID
    description: /path/to/description.md
    attributes: /path/to/attributes.yml   # Schema definition
    response: /path/to/example.json
    response_title: OBJECT             # Label for response section
  -
    title: List all Objects
    id: list-all-objects
    description: /path/to/list.md
    code: /path/to/list.py             # Python example code
    code_type: GET                      # HTTP method
    code_url: /api/objects/            # API endpoint URL
    response: /path/to/list-response.json
```

### Attributes/Schema Files (`-object.yml`)

Define the API response object structure:

```yaml
attributes:
  -
    name: id
    type: integer
    description: Unique identifier for the object.
  -
    name: nested_object
    type: object
    description: Description of nested object.
    children:
      -
        name: child_field
        type: string
        description: Description of child field.
  -
    name: items
    type: array
    description: Array of items.
    children:
      - ... (define array item structure)
```

### Description Files (`.md`)

Markdown files containing human-readable descriptions. Use level 3 headers:

```markdown
### Create an Invoice

Description of what this endpoint does, any important notes about behaviour,
validation rules, and edge cases.

**Important notes should be bold and highlighted.**
```

### Code Example Files (`.py`)

Python code examples showing how to call the API:

```python
import pprint, requests

headers = {'Authorization': 'token <API KEY>'}
data = {
    'field1': 'value1',
    'field2': 123,
}
r = requests.post('https://secure.tutorcruncher.com/api/endpoint/', json=data, headers=headers)
pprint.pprint(r.json())
```

### Response Example Files (`.json`)

Example JSON responses (formatted for readability):

```json
{
  "id": 123,
  "status": "success",
  "data": {
    "field": "value"
  }
}
```

## Adding a New Endpoint Section

### Step 1: Add to Master Layout (`pages/api.yml`)

If creating a new endpoint type, add it to `endpoint_sections`:

```yaml
endpoint_sections:
  # ... existing endpoints ...
  -
    title: New Endpoint
    id: new-endpoint
    layout: /new-endpoint/new-endpoint.yml
```

### Step 2: Create Endpoint Folder

Create `pages/new-endpoint/` with required files.

### Step 3: Create Section Layout

Create `new-endpoint.yml` defining all documentation sections.

### Step 4: Create Content Files

Create all referenced `.md`, `.py`, `.json`, and `.yml` files.

## Adding a New Action to Existing Endpoint

### Step 1: Add Section to Layout

Edit `<endpoint>/<endpoint>.yml` and add a new section:

```yaml
sections:
  # ... existing sections ...
  -
    title: New Action
    id: new-action
    description: /endpoint/new-action.md
    code: /endpoint/new-action.py
    code_type: POST
    code_url: /api/endpoint/action/
    response: /endpoint/new-action.json
```

### Step 2: Create Content Files

Create the referenced `.md`, `.py`, and `.json` files.

## Writing Guidelines

### Markdown Descriptions

- Use `###` (h3) headers for section titles
- Explain what the endpoint does in plain language
- Document required vs optional fields
- Highlight important restrictions or behaviours in **bold**
- Document validation rules and error conditions
- Explain any filtering or scoping that affects what data is available

### Python Code Examples

- Import `pprint` and `requests`
- Show realistic data values
- Use the correct HTTP method (GET, POST, PUT, DELETE)
- Include headers with API key placeholder: `{'Authorization': 'token <API KEY>'}`
- Use `json=data` for POST/PUT requests with JSON body

### JSON Response Examples

- Use realistic but fake data
- Include all fields that would be returned
- Format with 2-space indentation
- Match the structure defined in the attributes YAML

### Attribute Definitions

- Use clear, concise descriptions
- Document the type accurately (string, integer, decimal, boolean, object, array)
- For objects and arrays, define `children` with their structure
- Note when fields can be null

## Local Development

```bash
# Install dependencies
make install

# Run local development server
harrier dev
```

The site will be available at `http://localhost:8000`.

## Deployment

The documentation auto-deploys on merge to main. Create a new tag/release after significant changes.

## Important Notes

1. **All paths are relative** - Use `/endpoint/file.md` format in YAML files
2. **IDs must be unique** - The `id` field is used for HTML anchors
3. **Match code_type to HTTP method** - GET, POST, PUT, DELETE
4. **Test locally before pushing** - Run `harrier dev` to preview changes
5. **Document filtering/validation** - Users need to know why their data might not appear
