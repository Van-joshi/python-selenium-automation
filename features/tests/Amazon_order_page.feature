# Created by 15712 at 5/20/2023
Feature: Go to Amazon orders sign in page
  # Enter feature description here

  Scenario:  Open amazon main page
    Given Open amazon main page
    When click on orders
    Then Sign in header is visible
    Then email input field is present
