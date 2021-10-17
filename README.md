<p align="center">
  <a href="" rel="noopener">
 <img width=300px height=200px src="https://i.morioh.com/2020/03/31/2f138436048a.jpg" alt="Project logo"></a>
</p>

<h3 align="center">serverless-python-example</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/mkubasz/serverless-python-example.svg)](https://github.com/mkubasz/serverless-python-example/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/mkubasz/serverless-python-example.svg)](https://github.com/mkubasz/serverless-python-example/pulls)
<!-- [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE) -->
</div>

---

<p align="center"> Serverless Python by example
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Folder Structure](#folder_structure)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Folder structure <a name = "folder_structure"></a>
```
.
├── Makefile
├── README.md
├── README_old.md
├── api
│   └── openapi.yml
├── docker-compose.yml
├── docs
│   └── adl
│       └── 0000_ADR_Create_serverless_app_1.10.2021.md
├── localstack.http
├── localstack_endpoints.json
├── package-lock.json
├── package.json
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── serverless.yml
└── src
    ├── __init__.py
    ├── config
    │   └── __init__.py
    ├── handlers
    │   ├── __init__.py
    │   └── handler.py
    ├── helpers
    │   └── __init__.py
    ├── models
    │   └── __init__.py
    ├── sources
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   └── test_handler.py
    └── utils
        └── __init__.py
```
### Prerequisites

There are a few essential tools that are required before you begin

- [Docker](https://www.docker.com/) 
- [Poetry](https://python-poetry.org/)
- [npm](https://www.npmjs.com/)

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Environment variables

| Environment name   | Default value |     Desription   |
|--------------------|:-------------:|-----------------:|
| EXAMPLE            |  True         | Some description |


## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
