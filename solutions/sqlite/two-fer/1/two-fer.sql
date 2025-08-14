-- Schema: CREATE TABLE "twofer" ("input" TEXT, "response" TEXT);
-- Task: update the twofer table and set the response based on the input.
CREATE TABLE IF NOT EXISTS twofer (
    input TEXT,
    response TEXT
);

INSERT INTO twofer(input, response) VALUES 
    ("", "One for you, one for me."),
    ("Alice", "One for Alice, one for me."), 
    ("Bob", "One for Bob, one for me.");