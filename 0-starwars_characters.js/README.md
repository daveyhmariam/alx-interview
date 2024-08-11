# 0x06. Star Wars API

## Description

This project requires you to interact with the Star Wars API to fetch and display information about characters from a specific Star Wars movie, based on the movie ID provided as a command-line argument. The goal is to demonstrate your ability to work with external APIs, handle asynchronous operations in JavaScript, and manage command-line arguments.



## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 20.04 LTS
- **Node.js version:** 10.14.x
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/node`.
- A `README.md` file at the root of the project is mandatory.
- Code must adhere to the [semistandard](https://github.com/standard/semistandard) style guide.
- All files must be executable.
- No use of `var` is allowed.

## Setup

### Install Node.js 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

Tasks
0. Star Wars Characters
Mandatory

Write a script that prints all characters of a Star Wars movie.
The first positional argument passed is the Movie ID (e.g., 3 = "Return of the Jedi").
Display one character name per line in the same order as the characters list in the /films/ endpoint.