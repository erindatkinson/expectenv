# Expectenv

A simple python package to manage env var expectations

![image of cabin in apline mountains](.github/assets/alpine.jpg)
Image by [FelixMittermeier](https://pixabay.com/users/felixmittermeier-4397258) from Pixabay

## Using

### Install

In the [github releases page](https://github.com/erindatkinson/expectenv/releases) download the wheel for the version you want and install it with the pip application of your choice.

### A simple example

With an env where we're expecting

* APP_DB_HOST
* APP_ELASTIC_HOST
* APP_SECRET_KEY

we could write something like this (or let the env error get raised)

```py
import logging
import expectenv

# ...

def initEnv() -> dict:
    parser = expectenv.Parser("app")
    parser.bind("db_host")
    parser.bind("elastic_host")
    parser.bind("secret_key")
    try:
        parser.parse()
    except expectenv.EnvError as ee:
        log.error(ee)
        exit(1)
    
    return parser.configs()

```
