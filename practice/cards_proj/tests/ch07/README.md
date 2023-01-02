# Testing strategy

## Commands:
- add: Add a card to db.
- config: List the path to the Cards db.
- count: Return number of cards in db.
- delete: Remove card in db with given id.
- finish: Set a card state to 'done'.
- list: List cards in db.
- start: Set a card state to 'in prog'.
- update: Modify a card in db with given id with new info.
- version: Return version of cards application

### Count the database entries
For count we’ve got these test cases:
- count from an empty database
- count with one item
- count with more than one item

### Add a card
Here are the test cases we have for add:
- add to an empty database, with summary
- add to a non-empty database, with summary
- add a card with both summary and owner set
- add a card with a missing summary
- add a duplicate card

### Remove a card
Here are the test cases we have for delete:
- delete one from a database with more than one
- delete the last card
- delete a non-existent card

### Change card state
- start from “todo,” “in prog”, and “done” states
- start an invalid ID
- finish from “todo”, “in prog”, and “done” states
- finish an invalid ID

### Other cases
For the remaining features:
- update the owner of a card
- update the summary of a card
- update owner and summary of a card at the same time
- update a non-existent card
- list from an empty database
- list from a non-empty database
- config returns the correct database path
- version returns the correct version

