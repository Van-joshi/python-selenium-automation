# Created by 15712 at 5/17/2023
Feature: load amazon main page

  Scenario: User can load Amazon main page
    Given Open chrome
    When Open amazon url
    When Amazon main page is open
    When Click on Hello Sign In from popup
    Then Sign Inn header is visible

