# Created by Udit Hari Mehta at 23/09/2020
Feature: Login

  Scenario: Log me in
    Given I have filled in correct username and password
    When I hit login
    And My credentials have been authenticated
    Then I should be directed to profile home page
