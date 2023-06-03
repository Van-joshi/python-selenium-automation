# Created by 15712 at 6/3/2023
Feature: window handling

  Scenario: User can open and close Amazon privacy policy

    Given Amazon main page is open
    When Click on orders
    Then Sign In header is visible
    And Store Original window
    And Click on Privacy Notice
    And Switch to new window
    And TC Page is Open
    And Close TC page
    And Return to original window



