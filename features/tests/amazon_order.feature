# Created by 15712 at 5/9/2023
Feature: Amazon order to sign in page
  # Enter feature description here

  Scenario: user searches Amazon
    Given Open amazon main page
    When Click on orders

    Then Sign In header is visible
    Then email input field is present


