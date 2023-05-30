# Created by 15712 at 5/29/2023
Feature: User can pick elements

  Scenario: User can pick colors from selected item
    Given Amazon main page is open
    When Dress is serached on Amazon
    When User clicks on the dress

    Then All color options are displayed