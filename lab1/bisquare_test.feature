Feature: My first feature file using radish
    In order to test my awesome software
    I need an awesome BDD tool like radish
    to test my software.

    Scenario: 0 roots
        Given Coefs are 2, 4, 2
        When I solve the bisquare equation
        Then I expect the result to be []

    Scenario: 1 root
        Given Coefs are 1, 0, 0
        When I solve the bisquare equation
        Then I expect the result to be [0.0]

    Scenario: 2 roots
        Given Coefs are 2, -4, 2
        When I solve the bisquare equation
        Then I expect the result to be [1.0, -1.0]

    Scenario: 3 roots
        Given Coefs are 1, -1, 0
        When I solve the bisquare equation
        Then I expect the result to be [0.0, 1.0, -1.0]

    Scenario: 4 roots
        Given Coefs are 1, -5, 4
        When I solve the bisquare equation
        Then I expect the result to be [1.0, 2.0, -1.0, -2.0]