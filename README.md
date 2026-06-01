# Builder 
A Light Weight cli for your projects
Generate your project structures from your terminal.

## Quick Start
### Download
When you downloaded the project, make sure the CLI is working: 
```bash 
    builder --help
```
### Use


You can use this Cli like this:
```bash
    builder new --name [ProjectName] --template [Template]  --path [Path] --git
```
Or:

```bash
    builder new -n [ProjectName] -t [Template] -p [Path] -g 
```

## Templates
Currently, on version 0.1.0 these Templates are valid:
- [x] Pure-Python
- [x] flask-app
- [x] html
- [x] application bots
- [x] click-cli
- [x] php-basic
- [x] data-science
- [x] dashboard-ui
### Templates command
you can see templates by using this command:
```bash
    builder templates 
```


## Updates
New versions details:
### 0.1.0
The Base Version 
added some templates , main command , git support
### 0.2.0
On this version 
some templates are updated , some new templates are added , a new command named "templates" is also added to be able to see templates

