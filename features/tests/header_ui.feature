# Created by krithikabalasundar at 6/11/25
Feature: Tests to verify Header UI elements

  Scenario: User can navigate to Sign In on Target
    Given Open target main page
    When Click Account
    When Click navigation menu, click Sign In
    Then Sign in form is opened


  Scenario: Verify header has correct amount of links
    Given Open target main page
    Then Verify header has 6 links