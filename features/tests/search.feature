# Created by krithikabalasundar at 6/11/25
Feature: Test for Target search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

  Scenario: User can search for shampoo
    Given Open target main page
    When Search for shampoo
    Then Verify search worked for shampoo

  Scenario: User can search for table
    Given Open target main page
    When Search for table
    Then Verify search worked for table

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <search_word>
    Then Verify search worked for <search_word>
    Examples:
    |search_word  |
    |tea          |
    |mug          |
    |coffee       |
    |shampoo      |