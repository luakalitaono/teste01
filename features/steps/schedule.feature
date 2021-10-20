Feature: Schedule
Scenario: Schedule appointment
    Given that I am on the schedule screen
    When clicking on a date
    AND filling in the fields
    Then the query is displayed on the listing date