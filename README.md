```
___________.__                                   
\_   _____/|  |  _____     ____    ____    ____  
 |    __)  |  |  \__  \   / ___\ _/ __ \  /    \ 
  |     \   |  |__ / __ \_/ /_/  >\  ___/ |   |  \
   \___  /   |____/(____  /\___  /  \___  >|___|  /
        \/               \//_____/       \/      \/ 
```

Flagen is a Flask Site/Blog generator.

### Installation
    $ git clone https:/github.com/jeffgodwyll/flagen.git
    $ cd flagen
    $ pip install -e .

### Usages
    $ flagen --help
    Usage: flagen [OPTIONS] COMMAND [ARGS]...

    Flagen is a simple static site generator built on top of Frozen Flask

    Options:
      --help  Show this message and exit.

    Commands:
      build  Build site and generate a `build` folder
      serve  Serve site

    $ flagen build --help
    Usage: flagen build [OPTIONS]

    Build site and generate a `build` folder

    Options:
    --template PATH  Pass a custom template directory
    --help           Show this message and exit.

    $ flagen serve --help
    Usage: flagen serve [OPTIONS]

      Serve site

    Options:
      --template PATH  Pass a custom template directory
      --help           Show this message and exit.

##### Examples
    $ flagen serve

    $ flagen serve --template templates/templates_material/ 
     
    $ flagen serve --template templates/simple/

    $ flagen build 

    $ flagen build --template templates/templates_material/

### As a blog

Content in the `pages` folder are rendered as blog posts

Each post takes the following format:
    
    title: Hello World
    date: 2014-11-29
    tags: [general, awesome, stuff]

    **Hello World**, from a *page*! etc, etc

The blog content will be in markdown. Look in the `pages` folder for example

### Feedback

Star this repo if you find it useful. Use the github issue tracker to give
feedback on this repo or to report an issue.

### Licensing

http://jeff.mit-license.org/
