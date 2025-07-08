# Created by krithikabalasundar at 6/7/25
Feature: Tests for Target site

  Scenario: User can navigate to Cart page on Target
    Given Open target main page
    When Click on Cart
    Then Verify 'Your cart is empty' is shown


  Scenario: User can add a product to the cart in Target
    Given Open target main page
    When Search for tea
    And Click on Add to Cart
    And Store product name
    And Click on 'Add to Cart' from side navigation
    And Open cart page
    Then Verify Cart item is present
    And Verify cart has correct product
