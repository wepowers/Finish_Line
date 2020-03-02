Course: CS 30
Period: 1
Date created: 2020/03/01
Date last modified: 
Name: William Powers
Description: Pseudocode

BEGIN Finish_Line Game:
    BEGIN Menu
    END Menu

**MENU CODE**

BEGIN Menu:
    Print Begin Menu
    Input "What would you like to do?"
    CASEWHERE:
        1: "Start",  BEGIN Movement
        2: "Instructions", BEGIN HelpMe
        3: "Exit", END Menu
    END CASEWHERE
END Menu

**MOVEMENT CODE**

BEGIN Movement:
    INPUT "What would you like to do?"
    CASEWHERE:
    Go North: Move North
    Go South: Move South
    Go East: Move East
    Go West: Move West
    Get Help: BEGIN HelpMe
    Use Item: Begin Use
    Show Inv: Begin Inv
    END CASEWHERE
    IF INPUT is " Go North, Go South, Go East, or Go West"
        Make random number to decide if there is a positive item, negative
        item, or no item.
END Movement

**HelpMe Code**

BEGIN HelpMe
    PRINT Game Commands
    INPUT "Continue?"
END HelpMe

**Use Code**

BEGIN Use:
    PRINT Inv
    INPUT the item you want to use
    IF item is available
        Use Item
        
    ELSE:
        PRINT "Item is not in Inventory
END Use

**Inv Code**

BEGIN Inv:
    PRINT Inv
END Inv

**Show XP Code**

BEGIN Show XP:
    PRINT XP
END Show XP

        