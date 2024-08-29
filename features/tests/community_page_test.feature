Feature: Community Page test


  Scenario: User can open the community page
    Given Open the main page
    When Log in to the page
    When Click on settings option
    When Click on Community option
    Then Verify the right page opens
    Then Verify “Contact support” button is available and clickable