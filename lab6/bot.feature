Feature: My first feature file using radish
    In order to test my awesome software
    I need an awesome BDD tool like radish
    to test my software.

    Scenario: power 1
        Given I choose power, 6, 3
        When I perform the operation
        Then I expect the result to be 216.0

    Scenario: power 2
        Given I choose power, 9, 0.5
        When I perform the operation
        Then I expect the result to be 3.0

    Scenario: log 1
        Given I choose log, 9, 3
        When I perform the operation
        Then I expect the result to be 2.0

    Scenario: log 2
        Given I choose log, 9, 81
        When I perform the operation
        Then I expect the result to be 0.5
