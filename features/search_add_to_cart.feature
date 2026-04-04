Feature: Search for a product and add it to the cart successfully

  Scenario: User is able to search for a product and add the product to cart
    Given User navigates to adnabu store
    Given User enters store password "AdNabuQA"
    Then User clicks on enter button
    When User is on adnabu store homepage
    Then User clicks on shop products button
    Then User clicks on search icon
    Then User searches for "The Multi-location Snowboard"
    Then User validates the search result
    When User clicks on the search result
    Then User clicks on add to cart button
    Then User verifies the product is successfully added to cart

