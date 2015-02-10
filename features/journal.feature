Feature: Journal Editing
    Implement the ability to edit posts in a rich manner

    Scenario: Entry Detail
        Given a journal entry list
        When I click on the link
        I get the detail page for that entry

    Scenario: Post Edit
        Given a journal entry
        When I click on the edit button
        I'm taken to the edit page for that entry

    Scenario: Markdown Entries
        Given a journal edit form
        When I type in the edit box
        I can use MarkDown to format my post

    Scenario: Code blocks
        Given a journal entry
        When I look at a post
        I can see colorized code samples