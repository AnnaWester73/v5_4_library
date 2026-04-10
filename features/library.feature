Feature: Bibliotek

  Scenario: Söka efter böcker baserat på titel
    Given att bibloteket innehåller följande böcker:
    | titel               |author             | borrowed    |
    | Pippi Långstrump    |Astrid Lindgren    | no          |
    | Emil i Lönneberga   |Astrid Lindgren    | no          |
    | Madicken            |Astrid Lindgren    | no          |

    When användaren söker efter böcker med titel " Pippi Långstrump"
    Then ska följande böcker hittas:
    | titel               |
    | Pippi Långstrump    |

  Scenario: Söka efter böcker baserat på författare
    Given att biblioteket innehåller följande böcker:
    | titel               |author             | borrowed    |
    | Pippi Långstrump    |Astrid Lindgren    | no          |
    | Emil i Lönneberga   |Astrid Lindgren    | no          |
    | Madicken            |Astrid Lindgren    | no          |

    When användaren söker efter böcker av författaren "Astrid Lindgren"
    Then ska följande böcker hittas:
      | titel              |
      | Pippi Långstrump   |
      | Emil i Lönneberga  |
      | Madicken           |

  Scenario: Användaren lånar en tillgänglig bok
  Given att biblioteket innehåller följande böcker:
    | titel               |author             | borrowed    |
    | Pippi Långstrump    |Astrid Lindgren    | no          |
    | Emil i Lönneberga   |Astrid Lindgren    | no          |
    | Madicken            |Astrid Lindgren    | no          |
  When användaren lånar boken "Pippi Långstrump"
  Then ska boken "Pippi Långstrump" vara utlånad

  Scenario: Användaren lämnar tillbaka en utlånad bok
    Given att biblioteket innehåller följande böcker:
    | titel               |author             | borrowed    |
    | Pippi Långstrump    |Astrid Lindgren    | yes         |
    | Emil i Lönneberga   |Astrid Lindgren    | no          |
    | Madicken            |Astrid Lindgren    | no          |
    When användaren lämnar tillbaka boken "Pipp Långstrump"
    Then ska boken "Pipp Långstrump" inte vara utlånad


  Scenario: Kontrollera om en viss bok inte är utlånad
    Given att biblioteket innehåller följande böcker:
    | titel               |author             | borrowed    |
    | Pippi Långstrump    |Astrid Lindgren    | no         |
    | Emil i Lönneberga   |Astrid Lindgren    | no          |
    | Madicken            |Astrid Lindgren    | no          |
  When användaren kontrollerar om boken "Pippi Långstrump" är utlånad
  Then ska svaret vara att boken inte är utlånad
