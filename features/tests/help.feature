# Created by krithikabalasundar at 6/12/25
Feature: Tests for help feature

  Scenario: User can identify the elements on the help page
    Given Open target main page
    When Click on Help
    Then Verify the elements present on Help page