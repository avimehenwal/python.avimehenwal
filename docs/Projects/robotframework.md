---
title: Robot Framework
tags:
- robot
- framework
- automation
- testing
- accentance
- rpa
---

# Robot Framework

<TagLinks />

## Console Script

```mermaid
classDiagram
  Application <|-- RobotFramework : extends
  Application *-- ArgumentParser : composition

  class Application{
    +username: str
    +password: str
    +verify_login()
  }
  class RobotFramework{
      +update_profile()
  }
  class ArgumentParser{
  }
link Application "http://www.github.com" "This is a tooltip for Application"
```




## :chart: UML Diagram

[UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) - Unified Modelling Language
:   structure of a software system

    * [Class Diagrams](https://en.wikipedia.org/wiki/Class_diagram)


```mermaid
classDiagram
  User <|-- Customer : inheritance
  User <|-- Administrator
  class User{
    +username: str
    +password: str
    +verify_login()
  }
  class Customer{
      +update_profile()
  }
  class Administrator{
    +update_catalogue()
  }
link User "http://www.github.com" "This is a tooltip for a link"
```

<Footer />
