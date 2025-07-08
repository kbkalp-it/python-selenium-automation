# Created by krithikabalasundar at 6/25/25
Feature: Tests for product page

  Scenario: User can select colors for Wrangler pants
    Given Open target product page 'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718'
    Then Verify user can click through colors
      |Navy Denim|
      |Dark Wash |
      |Light Wash|

  Scenario Outline: User can select expected colors from product
    Given Open target product page '<product_url>'
    Then Verify user can click through colors "<expected_colors>"

  Examples:
    | product_url                                                                                     | expected_colors                         |
    | https://www.target.com/p/men-s-every-wear-athletic-fit-chino-pants-goodfellow-co/-/A-52520861   | Black,Dapper Brown,Khaki                |
    | https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718             | Navy Denim,Dark Wash,Light Wash         |