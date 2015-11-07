from behave.formatter.json import PrettyJSONFormatter
from pprint import pprint

class RecordFormatter(PrettyJSONFormatter):
    name = "super"
    description = "Formatter for adding REST calls to JSON output."
    jsteps = {} # Contains an array of features, that contains array of steps in each feature

    # Overriding Background Function. This runs evertime a Background is ran.
    # This step
    def background(self, background):
        # Let the parent run first
        super(RecordFormatter, self).background(background)
        # Check if the current feature has a name - Could be removed
        if (self.isnotBackground()):
            # Remove all the background steps from our jsteps, as they are not required
            for step in background.steps:
                self.jsteps[self.current_feature_element.name].pop(0)

    # Overriding Step feature. This is called everytime a step is found in feature file. This happens before the feature/scenario are executed.
    def step(self, step):
        # Let the parent run first
        super(RecordFormatter, self).step(step)
        # Check if the current feature has a name - Could be removed
        if (self.isnotBackground()):
            # Append the step into our own collection of jsteps.
            self.jsteps[self.current_feature_element['name']].append(step);

    # Overriding End of Feature. This is ran once the entire feature has completed running
    def eof(self):
        # Iterate through each scenarios
        for scenario in self.current_feature_data['elements']:
            # Check if Scenario valid
            if (scenario['name'] != ''):
                steps = scenario['steps']
                jscenariosteps = self.jsteps[scenario['name']]
                status = "passed"   # Add Scenario status
                # Iterate through the jstep, and step results
                for (j, jstep) in enumerate(jscenariosteps):
                    # Check if any of the above status failed, if so, mark the status as failed
                    if ('result' in steps[j]):
                        if steps[j]['result']['status'] == 'failed':
                            status = 'failed'
                    # Add configurations in scenario level. generally used for sdk_language and sdk_version
                    if (hasattr(jstep, "details")):
                        scenario['details'] = jstep.details
                    if (hasattr(jstep, "date")):
                        steps[j]['date'] = jstep.date
                    # Check if jstep has attribute calls, where our custom data is stored - Could be generalized further
                    if (hasattr(jstep, "calls") and 'result' in steps[j]):
                        # add the calls to our step object, that would be later added to json output.
                        steps[j]['result']['calls'] = jstep.calls
                # Add feature name and Status as a part of scenario
                scenario['feature'] = self.current_feature.name
                scenario['status'] = status
        # Let the parent run last here
        super(RecordFormatter, self).eof()

    def isnotBackground(self):
        if(self.current_feature_element['name'] != ''):
            if(self.current_feature_element['name'] not in self.jsteps):
                self.jsteps[self.current_feature_element['name']] = []
            return True
        return False
