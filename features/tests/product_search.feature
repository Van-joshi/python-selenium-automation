Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input shoes into search field
    And Click on search icon
    Then Product results for shoes are shown


  Scenario: User can search item by department
    Given Open Amazon page
    When Select department books
    When Search for faust
    When Click on search icon
    Then Verify correct result is shown


  Scenario: User can search item by department baby
    Given Open Amazon page
    When Select department baby
    When Search for baby swing
    When Click on search icon
    When Hover over nursery
    Then Verify baby department is shown
    Then All nursery items are seen