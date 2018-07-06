Feature: sign in to e-mail account
     As a user I want to log in
     and check my e-mails

    Scenario Outline: Log in with valid data
        Given user is on Poczta Onet website
        When user fills valid username <username> and valid password <password> and submits it
        Then User can see email list

        Examples:
      | username | password |
      | przykladowymail1t@onet.pl | haslo1 |
      | przykladowymail2@onet.pl  | haslo2 |


    Scenario Outline: Log in with invalid data
        Given user is on Poczta Onet website
        When user fills invalid username <invalidusername> and invalid password <invalidpassword> and submits it
        Then User can see alert about invalid date

      Examples:
      | invalidusername | invalidpassword |
      | zly_login       | zlehaslo        |
      | blednedane@onet.pl | blednehaslo  |

