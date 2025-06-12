# Created by krithikabalasundar at 6/7/25
Feature: Tests for Target site

  Scenario: User can navigate to Cart page on Target
    Given Open target main page
    When Click on Cart
    Then Verify 'Your cart is empty' is shown


  Scenario: User can add a product to the cart in Target
    Given Open target main page
    When Search for tea
    And Click on Add to Cart on search result
    Then Click on 'Add to Cart'
    And View Cart and Checkout
    And Verify Cart item is present
