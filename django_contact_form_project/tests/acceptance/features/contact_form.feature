Feature: Contact Form
    Scenario: Submit contact form successfully
        Given User is on contact form page
         When User completes the form
          And User clicks submit button
         Then User sees no error

    Scenario: User forgets to fill in firstname
        Given User is on contact form page
         When User fills in only lastname
          And User clicks submit button
         Then User sees error

    Scenario: User forgets to fill in lastname
        Given User is on contact form page
         When User fills in only firstname
          And User clicks submit button
         Then User sees error

