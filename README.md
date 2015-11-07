Python Reliability Testing Pipeline Demo
========================================

The [packaged ios app](/bin) brings up https://fast-shore-1824.herokuapp.com/ on safari when the launch button is clicked. The web page has a button app-switch with an on click handler. When clicked, it updates broswer with url appiumdemo:// which is an url scheme that the ios app registered so on iOS simulator it will bring back the app.

### System requirements
-- XCode
-- Node
-- Appium
-- Python
-- ElasticSearch
-- Kibana

### Dependencies

(We strongly recommend that you set up a [virtualenv](http://www.virtualenv.org/) for this project, and you may also want to check out [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) for convenience)

#### Instructions

1. `$ sudo pip install virtualenv virtualenvwrapper`
2. add `source /usr/local/bin/virtualenvwrapper.sh` to you your `.profile`
3. create a testing environment: `$ mkvitualenv reliability-demo`
4. Switch to using that environment: `$ workon reliability-demo`

## Automate app using appium 

-- [Install appium from appium.io](http://appium.io/)

###Instructions

#### Start appium server
```bash
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
