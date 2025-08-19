# Ai Agent

An ai agent designed to help you code, made as part of a [boot.dev course](https://www.boot.dev/courses/build-ai-agent-python)  

> [!CAUTION]
> This program grants an ai the ability to run any code it writes on your computer!  
> **Use at your own risk!!!**

## Features

- The ability to prompt an ai agent.
- The ability for the agent to list directories.
- The ability for the agent to get the content of files.
- The ability for the agent to write to files.
- The ability for the agent to run python programs.

## Usage

### Command

```shell
uv run main.py "<Your prompt>" [--verbose]
```

### Arguments

- --verbose: provides extra debug info from the agent

## Requirements

- [python 3.10+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv) (For installing the dependencies)

## Installation

1. First you need to clone the repo:

```shell
git clone https://github.com/Gts-Dav/aiagent.git
cd aiagent
```

2. Then create a file called .env and add these fields:

```
GEMINI_API_KEY="your_api_key_here"
WORKING_DIRECTORY="the_directory_the_agent_will_work_in"
```

3. Finally run the project:

```shell
uv run main.py "<Your prompt>"
```
