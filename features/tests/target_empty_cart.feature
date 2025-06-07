# Created by krithikabalasundar at 6/7/25
Feature: Tests for Target site

  Scenario: User can navigate to Cart page on Target
    Given Open target main page
    When Click on Cart
    Then Verify 'Your cart is empty' is shown

  Scenario: User can navigate to Sign In on Target
    Given Open target main page
    When Click Account
    When Click navigation menu, click Sign In
    Then Sign in form is opened
