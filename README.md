# tc-api-docs
Documentation for TutorCruncher's API

## Local Installation

1. create virtual environment

2. Install dependencies
```bash
make install
```

3. Run Local
```bash
harrier dev
```

## Editing

The visual content is setup in the api-content.jinja template stype page

The content set by this template is referred to as sections, each section is set out in api.yml

## Deploying

This PR has automatic deploys, after merging a PR, it will be deployed. 

Please create a new tag/release after making changes.
