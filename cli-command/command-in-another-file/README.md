If you want to organize your code, 
you can put your command routines in another file or a folder.


In this example, `hello` command is moved to `commands/hello.py`. [Blueprint](https://flask.palletsprojects.com/en/2.0.x/blueprints/) is used to create a command group `custom` and assign `hello` command to it. In the end, the created group should be added to the `app.py`

Running `flask` will display your new cli group:
```
Commands:
  custom  My custom commands
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.

```

Running `flask custom` will display avaliable commands in this cli group:

```
Usage: flask custom [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  hello  Say hello to the personam named with {name}

```

Running `flask custom hello` will display:
```
Hello World!
```

While running `flask custom hello buddy` will display:
```
Hello buddy
```