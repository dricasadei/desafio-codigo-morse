DROP TABLE IF EXISTS morseCodes;

CREATE TABLE morseCodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    code TEXT NOT NULL,
    translation TEXT NOT NULL
);