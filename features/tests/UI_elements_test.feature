Feature: UI Elements test


  Scenario: User can go to settings and see the right number of UI elements
    Given Open the reely main page
    When Log in to the reely page
    When Click on reely settings option
    Then Verify the right reely page opens
    Then Verify there are 12 options for the settings
    Then Verify “Connect the company” button is available
