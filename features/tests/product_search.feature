Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input shoes into search field
    And Click on search icon
    Then Product results for shoes are shown