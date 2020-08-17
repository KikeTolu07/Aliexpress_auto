# Created by tolani.oluwayemi at 8/8/2020
Feature: Guest Shopping

  As a shopper,
  I should be able to shop on any site,
  So that I can check out an item



  Scenario: Guest shopping on Aliexpress

    Given I am on "Aliexpress" site

      And I search and click on an item on "Aliexpress"

      And I select an item on "Aliexpress"

      And I added the "Aliexpress" item to cart

    When I proceed to check out on "Aliexpress"

    Then I should be redirected to "Aliexpress" sign in page





      Scenario: Guest shopping on Aliexpress

    Given I am on "ebay" site

      And I search and click on an item on "ebay"

      And I select an item on "ebay"

      And I added the "ebay" item to cart

    When I proceed to check out on "ebay"

    Then I should be redirected to "ebay" sign in page




