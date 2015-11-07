Feature: App Switch Demo

    Switch from app to web and back

    @mobile
    Scenario: Simple app switch use case
        Given we have appium installed
        When user runs app, clicks on "Launch" button in app
        Then user clicks on "app-switch" button in website
        Then it switches back to app