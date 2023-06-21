# Created by 15712 at 5/20/2023
Feature: Open Amazon Bestsellers

  Scenario: Navigate to amazon main page
    Given Open amazon main page
    When Click on Best Sellers

    
    Then Amazon Best Sellers text is visible
    Then New Releases text are seen
    Then Movers & Shakers text are seen
    Then Most Wished For texts are seen
    Then Gift Ideas text are seen
