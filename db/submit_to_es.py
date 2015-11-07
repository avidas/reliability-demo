import json
import sys
import os
import json
import time
import datetime
import subprocess
import shutil
from elasticsearch import Elasticsearch


def convert_behave_results_to_elastic_format(behaveResults):
    """
    Flatten behave output results for elasticsearch mapping format
    """
    results = []
    for behaveResult in behaveResults:
        for element in behaveResult["elements"]:
            if element["keyword"] == "Scenario":
                step_number = 1
                environment = "mock"
                for behaveStep in element["steps"]:
                    result = {}
                    # Grab the environment name if we're on the first step.
                    if step_number == 1:
                        for argument in behaveStep["match"]["arguments"]:
                            if argument["name"] == "env_name":
                                environment = argument["value"]
                    result["environment"] = environment
                    result["scenario"] = element["name"]
                    result["scenario_status"] = element["status"]
                    result["step"] = behaveStep["name"]
                    if "date" in behaveStep:
                        result["date"] = behaveStep["date"]
                    else:
                        result["date"] = datetime.datetime.utcnow().strftime(
                            '%Y-%m-%dT%H:%M:%S')
                    result["step_number"] = step_number
                    result["status"] = "skipped"
                    if "result" in behaveStep:
                        result["status"] = behaveStep["result"]["status"]
                        if "duration" in behaveStep["result"]:
                            result["duration"] = behaveStep[
                                "result"]["duration"]
                    results.append(result)
                    step_number = step_number + 1
    return results


def publish_results(config, results):
    """
    Take formatted results and submit to elasticsearch
    """
    total = 0
    succeeded = 0
    es = Elasticsearch([config["elasticsearch_url"]])
    doc_type = config["elasticsearch_index"]

    for result in results:
        result['feature'] = 'app-switch-demo'
        r = es.index(
            index=config["elasticsearch_index"], doc_type=doc_type, body=result)
        if r["created"]:
            sys.stdout.write('.')
            succeeded = succeeded + 1
        else:
            sys.stdout.write('x')
        total = total + 1
    print ""
    print str(succeeded) + "/" + str(total) + " test results submitted successfully."
    print ""

if __name__ == '__main__':
    behaveResults = json.load(open('data/results.json'))
    results = convert_behave_results_to_elastic_format(behaveResults)
    config = {
        'elasticsearch_url': 'http://localhost:9200',
        'elasticsearch_index': 'reliability',
        'elasticsearch_mapping': 'behave'
    }
    publish_results(config, results)
