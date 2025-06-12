# Created by krithikabalasundar at 6/11/25
Feature: Target Circle Benefits Display

  Scenario: Verify there are at least 10 benefit cells on the Target Circle page
    Given I open the Target Circle page
    Then I should see at least 10 benefit cells