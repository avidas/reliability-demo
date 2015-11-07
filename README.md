Python Reliability Testing Pipeline Demo
========================================

The [packaged ios app](/bin) brings up https://fast-shore-1824.herokuapp.com/ on safari when the launch button is clicked. The web page has a button app-switch with an on click handler. When clicked, it updates broswer with url appiumdemo:// which is an url scheme that the ios app registered so on iOS simulator it will bring back the app.

### System requirements
* XCode
* Node
* Appium
* Python and Pip
* ElasticSearch
* Kibana
* Homebrew (OSX)
* Java Runtime (for Elasticsearch)

### Dependencies

(We strongly recommend that you set up a [virtualenv](http://www.virtualenv.org/) for this project, and you may also want to check out [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) for convenience)

#### Instructions

1. `$ sudo pip install virtualenv virtualenvwrapper`
2. add `source /usr/local/bin/virtualenvwrapper.sh` to you your `.profile`
3. create a testing environment: `$ mkvitualenv reliability-demo`
4. Switch to using that environment: `$ workon reliability-demo`

## Automate app using appium 

* [Install appium from appium.io](http://appium.io/)

###Instructions

#### Start appium server
```bash
    appium --help # Check that appium is installed and available in your path
appium
```

#### Check out v0.1.0 tag

```bash
    git clone git@github.com:avidas/reliability-demo.git
    cd reliability-demo/
    git checkout v0.1.0
```

#### Install requirements using pip:

```bash
    pip install -r requirements.txt
```

Then run the script

```bash
    python run.py
```

## Describe Tests using Behave

#### Check out v0.2.0 of the repo

```bash
    git checkout v0.2.0
```

#### Install requirements

```bash
    pip install -r requirements.txt
```

Check that appium server is still running. Restart may be necessary.

#### Run behave from the root of the repo
```bash
    behave --help # Check that appium is installed and available in your path
    behave
```

#### Publish JSON formatted results of behave tests

```bash
    export PYTHONPATH=$PYTHONPATH:.; behave --no-capture  -f record --outfile=results.json -f pretty
```

## Storage and Visualization using ElasticSearch and Kibana

#### Install Elasticsearch

```bash
    # install via homebrew and check version
    brew install elasticsearch && brew info elasticsearch
    # Start Elasticsearch as a service
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.elasticsearch.plist
```

Then check Elasticsearch is running

```bash
    curl -XGET 'http://localhost:9200'
```

#### Install Kibana

```bash
    # install via homebrew and check version
    brew install kibana && brew info kibana
    # Start Kibana as a service
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.kibana.plist
```

Then navigate to http://localhost:5601/ in your browser

#### Set up Elasticsearch index


